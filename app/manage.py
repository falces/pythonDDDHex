#!/usr/bin/env python

import sys
import re

allowedActions = [
    "actions",
    "create_entity",
]

def main():
    try:
        if len(sys.argv) > 2 or len(sys.argv) < 2:
            raise Exception("Write just ONE action")
        else:
            action = sys.argv[1]
            if action not in allowedActions:
                raise Exception("Action not allowed")
            execute = getattr(sys.modules[__name__], action)
            execute()

    except Exception as e:
        print(e)

def actions():
    print(f'Allowed actions: {allowedActions}')

def create_entity():
    try:
        print('Let\'s create a new entity.')
        entity = input('Entity name: ')
        pattern = r"^[a-zA-Z]+$"
        if not re.fullmatch(pattern, entity):
            raise Exception(entity + " is not a valid name.")
        entity = entity.capitalize()
        print(f"Let's create the entity {entity}")

    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
