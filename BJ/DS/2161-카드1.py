from sys import *
from collections import deque

n = int(stdin.readline().rstrip())

cards = deque([i for i in range(1, n + 1)])

while cards:
    print(cards.popleft(), end=" ")

    if cards:
        cards.append(cards.popleft())
