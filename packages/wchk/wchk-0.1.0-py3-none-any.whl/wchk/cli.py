#!/usr/bin/env python
# -*- coding: utf-8 -*-
# SPDX-FileCopyrightText: 2022-present Ramiro Gómez <code@ramiro.org>
# SPDX-License-Identifier: MIT
import argparse
import sys
import timeit

from rich import print

from wchk import check


def log(url, output_file=None, verbose=None):
    result = check(url)
    if (result.get('status') != 200) or verbose:
        print('\t'.join(str(v) for v in result.values()), file=output_file)


def main():
    start_time = timeit.default_timer()
    parser = argparse.ArgumentParser(description='Check the status web pages.')
    parser.add_argument('url', type=str, nargs='?', help='Input URL to check.')
    parser.add_argument('--input-file', '-i', type=argparse.FileType('r'), default=sys.stdin,
                        help='Read URLs from a local text file.')
    parser.add_argument('--output-file', '-o', type=argparse.FileType('w'), default=sys.stdout,
                        help='Write output to file.')
    parser.add_argument('--verbose', '-v', action='store_true', help='Turn on verbose output.')
    cli_args = parser.parse_args()

    if cli_args.url:
        log(cli_args.url, output_file=cli_args.output_file, verbose=cli_args.verbose)
    elif cli_args.input_file:
        for line in cli_args.input_file.readlines():
            log(line.strip(), output_file=cli_args.output_file, verbose=cli_args.verbose)

    cli_args.verbose and print(f'Script runtime: {timeit.default_timer() - start_time:.3f} sec', )


if __name__ == '__main__':
    main()
