import sys
import random

while True:
    line = input()

    h = int(line.split()[1])

    for i in range(h):
        line = input()

    n = int(input())

    for i in range(n):
        line = input()

    m = int(input())
    for i in range(m):
        line = input()

    # use file=sys.stderr to print for debugging
    print("debug code", file=sys.stderr, flush=True)

    # this will choose one of random actions
    actions = ["left", "up", "bomb", "right", "down"]
    random_index = random.randint(0, len(actions) - 1)

    print(actions[random_index], flush=True)
