#!/usr/bin/env python

import sys

def main():
    try:
        if len(sys.argv) > 2 or len(sys.argv) < 1:
            raise Exception()
        else:
            executeAction(sys.argv[1])
    except Exception as e:
        print("Write just ONE action")


def executeAction(
    action: str,
):
    print("Let's " + action + "!")

if __name__ == '__main__':
    main()
