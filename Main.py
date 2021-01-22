# --------------- Main.py ---------------
# Supplied main function implementation for Scanner.
#
# Version:  Python 3.8
# Author:   Alex Hoke
# Date:		01/20/2021

from Scanner import Scanner
from Core import Core
import sys


def main():
    # Initialize the scanner with the input file
    in_file = Scanner(sys.argv[1])
    # Print the token stream
    while in_file.currentToken() != Core['EOF'] and in_file.currentToken() != Core['ERROR']:
        # Print the current token, with any extra data needed
        print(in_file.currentToken().name, end='')
        if in_file.currentToken() == Core['ID']:
            value = in_file.getID()
            print("[" + value + "]", end='')
        elif in_file.currentToken() == Core['CONST']:
            value = in_file.getCONST()
            print("[" + str(value) + "]", end='')
        print()
        # Advance to the next token
        in_file.nextToken()


if __name__ == "__main__":
    main()
