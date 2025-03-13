class A:
    def __init__(self):
        print("A")


class B(A):
    def __init__(self):
        print("B")
        super().__init__()


class C(A):
    def __init__(self):
        print("C")
        super().__init__()


class C1(C, B):
    def __init__(self):
        print("C1")
        super().__init__()


class D(B, C1):
    def __init__(self):
        print("D")
        super().__init__()


r"""
   A
  / \
 B   C
 | \ |
 |   C1
  \ /
   D
"""

"""
D

"""


def main():
    d = D()

    print(D.__mro__)


if __name__ == '__main__':
    main()
