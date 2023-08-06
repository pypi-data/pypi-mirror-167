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

import sys
from math import ceil
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._types import Readable, Writable


__all__ = ("BF",)


class BF:
    def __init__(self, stdin: "Readable" = sys.stdin, stdout: "Writable" = sys.stdout):
        self.__cells = [0]
        self.__index = 0

        self.stdin = stdin
        self.stdout = stdout

    def print_cells(self) -> None:
        spaces = -1
        for list_index, cell_value in enumerate(self.__cells):
            if list_index == self.__index:
                spaces = len(str(self.__cells[: self.__index])) + ceil(
                    len(str(cell_value)) / 2
                )
                if list_index == 0:
                    spaces -= 2
                break

        assert spaces != -1
        print(self.__cells, " " * spaces + "^", sep="\n", file=self.stdout)

    def run(self, code: str) -> None:
        iterator = iter(enumerate(code))
        for pos, char in iterator:
            if char == ">":
                self.__index += 1
                if self.__index >= len(self.__cells):
                    self.__cells.append(0)
            elif char == "<":
                if self.__index <= 0:
                    self.__cells.insert(0, 0)
                else:
                    self.__index -= 1
            elif char == "+":
                self.__cells[self.__index] += 1
            elif char == "-":
                self.__cells[self.__index] -= 1
            elif char == ",":
                input_char = self.stdin.read(1)
                self.__cells[self.__index] = ord(input_char[0])
            elif char == ".":
                output_char = chr(self.__cells[self.__index])
                self.stdout.write(output_char)
            elif char == "[":
                end = -1
                for next_pos, next_char in enumerate(code[pos:]):
                    if next_char == "]":
                        end = pos + next_pos
                        break
                if end == -1:
                    raise RuntimeError("Unclosed bracket")

                pos += 1
                while self.__cells[self.__index] != 0:
                    self.run(code[pos:end])

                while pos < end:
                    try:
                        pos, _ = next(iterator)
                    except StopIteration:
                        return

    def run_file(self, filename: str) -> None:
        with open(filename, "r") as file:
            code = file.read()
        self.run(code)
