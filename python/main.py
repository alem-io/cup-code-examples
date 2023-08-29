import sys
import random

while True:
    line = input()

    n = int(line.split()[0])

    for i in range(n):
        line = input()

    m = int(input())

    for i in range(m):
        line = input()

    # use file=sys.stderr to print for debugging
    print("debug code", file=sys.stderr, flush=True)

    # this will choose one of random actions
    print("100 100 200 200", flush=True)
