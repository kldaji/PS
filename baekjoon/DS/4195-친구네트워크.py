from sys import *


def find(friends, x):
    if friends[x] == x:
        return x

    friends[x] = find(friends, friends[x])
    return friends[x]


def union(friends, network, a, b):
    a = find(friends, a)
    b = find(friends, b)

    if a == b:
        print(network[a])
        return

    if a < b:
        friends[b] = a
        network[a] += network[b]
        print(network[a])
    else:
        friends[a] = b
        network[b] += network[a]
        print(network[b])


T = int(stdin.readline().rstrip())

for _ in range(T):

    N = int(stdin.readline().rstrip())

    friends = {}
    network = {}

    for _ in range(N):
        a, b = stdin.readline().rstrip().split()

        if a not in friends:
            friends[a] = a
            network[a] = 1
        if b not in friends:
            friends[b] = b
            network[b] = 1

        union(friends, network, a, b)
