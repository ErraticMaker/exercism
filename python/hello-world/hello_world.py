#
# Skeleton file for the Python "Hello World" exercise.
#
import sys


def hello(name='World'):
    return 'Hello, {}!'.format(name)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(hello(sys.argv[1]))
    else:
        print(hello())
