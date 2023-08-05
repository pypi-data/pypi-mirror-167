#!/usr/bin/env python3
"""
for testing some stuff on pypi
"""


class Example():
    """
    example class
    """
    def __init__(self, name: str):
        self.name = name


    def identify(self) -> None:
        print(self.name)


    def invert_name(self) -> str:
        return self.name[::-1]


if __name__ == '__main__':
    e = Example("random")
    print(e.invert_name())

