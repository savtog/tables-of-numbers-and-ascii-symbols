#!/usr/bin/python3
  
"""  Tables of numbers and ascii symbols (nstub.py).

A console application for Linux that displays the values of numbers
from 0 to 15 and ascii symbols in binary, decimal and hexadecimal formats.

Copyright 2025 Aleksandr Senkevich <savtog@mail.ru>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>."""


import sys

_SYMBOLS_LIST = [
    'NUL (null)',
    'SOH (start of heading)',
    'STX (start of text)',
    'ETX (end of text)',
    'EOT (end of transmission)',
    'ENQ (enquiry)',
    'ACK (acknowledge)',
    'BEL (bell)',
    'BS  (backspace)',
    'TAB (horizontal tab)',
    'LF  (NL line feed, new line)',
    'VT  (vertical tab)',
    'FF  (NP form feed, new page)',
    'CR  (carriage return)',
    'SO  (shift out)',
    'SI  (shift in)',
    'DLE (data link escape)',
    'DC1 (device control 1)',
    'DC2 (device control 2)',
    'DC3 (device control 3)',
    'DC4 (device control 4)',
    'NAK (negative acknowledge)',
    'SYN (synchronous idle)',
    'ETB (end of trans. block)',
    'CAN (cancel)',
    'EM  (end of medium)',
    'SUB (substitute)',
    'ESC (escape)',
    'FS  (file separator)',
    'GS  (group separator)',
    'RS  (record separator)',
    'US  (unit separator)',
    'Space']
_SYMBOLS_LIST.extend([chr(i) for i in range(33, 127)])
_SYMBOLS_LIST.append('DEL')


def main(args):
    """Main method"""

    print(args)

    print_table_numbers()
    print_table_ascii()

def print_table_numbers():
    """Shows numbers from 0 to 15 in binary,
    decimal and hexadecimal formats."""
    
    print('\tTable of numbers')
    print('\t' + '-' * 22)
    print('Bin\tDec\tHex\t' * 2)
    for i in range(8):
        print('{0:04b}\t{0:>3d}\t{0:>3x}\t{1:04b}\t{1:>3d}\t{1:>3x}'.format(i, i + 8))

def print_table_ascii():
    """Shows table of ASCII symbols."""
    print('\n\tTable ASCII')
    print('\t' + '-' * 11)
    print('Bin       Dec  Hex  Symbol                       Bin       Dec  Hex  Symbol  Bin       Dec  Hex  Symbol  Bin       Dec  Hex  Symbol')
    for i in range(len(_SYMBOLS_LIST)//4):
        print('{0:08b}  {0:3d}  {0:3x}  {1:28s} {2:08b}  {2:3d}  {2:3x}  {3:6s}  {4:08b}  {4:3d}  {4:3x}  {5:6s}  {6:08b}  {6:3d}  {6:3x}  {7:6s}'.format(i, _SYMBOLS_LIST[i], i + 32, _SYMBOLS_LIST[i + 32], i + 32 * 2, _SYMBOLS_LIST[i + 32 * 2], i + 32 * 3, _SYMBOLS_LIST[i + 32 * 3]))


if __name__ == '__main__':
    sys.exit(main(sys.argv))
