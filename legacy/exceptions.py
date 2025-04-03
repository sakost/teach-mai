# exceptions ≈ error
import contextlib
import pytest



def main():
    f = open("sdflkhsdf", "w")
    with pytest.raises(ValueError):
        print('test')

    print('test2')


if __name__ == '__main__':
    main()
