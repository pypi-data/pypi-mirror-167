"""
The MIT License (MIT)

Copyright (c) 2022-present The Master

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

import argparse
import sys
from . import __author__, __doc__, __license__, __name__, __version__, BF


def main() -> int:
    if not sys.orig_argv[1].endswith("zombies.exe"):
        if sys.platform == "win32":
            python_command = "py"
        else:
            python_command = "python3"
        usage = f"{python_command} -m zombies filename"
    else:
        usage = None

    parser = argparse.ArgumentParser(prog=__name__, usage=usage, description=__doc__)
    parser.add_argument(
        "filename",
        help="The name of the file to run (Optional)",
        nargs="?",
        default=None,
    )
    args = parser.parse_args()

    interpreter = BF()

    if args.filename:
        try:
            interpreter.run_file(args.filename)
        except FileNotFoundError:
            print(f"Path '{args.filename}' does not exist")
    else:
        print(
            f"Brainfuck REPL made in Python | {__name__} {__version__} by {__author__} | License {__license__}"
        )
        print('Type "cells" view the the current cells')
        print('Type "stop" to exit')

        try:
            while True:
                print("\\\\\\", end=" ")

                line = input()
                if line == "stop":
                    break
                if line == "cells":
                    interpreter.print_cells()

                interpreter.run(line)
                print()
        except KeyboardInterrupt:
            pass

    return 0
