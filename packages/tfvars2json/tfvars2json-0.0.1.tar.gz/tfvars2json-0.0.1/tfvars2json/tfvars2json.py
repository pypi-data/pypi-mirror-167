#!/usr/bin/env python

import sys
import argparse
import hcl
import json
import functools
import operator


def to_json(string, indent):
    return json.dumps(hcl.loads(string), indent=indent)


def to_tfvars(payload, indent):
    if not isinstance(payload, dict):
        return

    def recurse(item, level=0):
        if isinstance(item, dict):
            if level > 0:
                yield "{"

            for key, value in item.items():
                yield "\n"
                yield indent * level * " "
                yield "{} = ".format(key)

                for token in recurse(value, level=level+1):
                    yield token

            if level > 0:
                yield "\n"
                yield indent * (level-1) * " "
                yield "}"

        elif isinstance(item, list):
            if level > 0:
                yield "["

            for index, value in enumerate(item):
                yield "\n"
                yield indent * level * " "

                for token in recurse(value, level=level+1):
                    yield token

                if index < len(item)-1:
                    yield ","

            if level > 0:
                yield "\n"
                yield indent * (level-1) * " "
                yield "]"

        elif isinstance(item, bool):
            yield "true" if item else "false"

        else:
            yield "\"{}\"".format(item)

        if level-1 == 0:
            yield "\n"

    return functools.reduce(operator.add, recurse(payload), "")


def main():

    parser = argparse.ArgumentParser(description="TFVars 2 Json")
    parser.add_argument("-r", "--reverse", dest="reverse", action="store_true", help="expects Json input")
    parser.add_argument("-I", "--indent", dest="indent", type=int, metavar="N", default=2, help="adjust identation levels")
    parser.add_argument("-i", "--in", dest="input_stream", default=sys.stdin, type=argparse.FileType("r"), help="input stream")
    parser.add_argument("-o", "--out", dest="output_stream", default=sys.stdout, type=argparse.FileType("w", encoding="UTF-8"), help="output stream")
    args = parser.parse_args()

    result = None
    if args.reverse:
        result = to_tfvars(json.load(args.input_stream), indent=args.indent)
    else:
        result = to_json(args.input_stream.read(), indent=args.indent)

    if result:
        args.output_stream.write(result)
        args.output_stream.flush()
