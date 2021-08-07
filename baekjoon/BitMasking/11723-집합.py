"""
<Bit Masking>
"""

from sys import *

# 0000 ... 0000
S = 0


def getBit(idx):
    global S
    ret = (S & (1 << idx)) != 0

    return ret


def setBit(idx):
    global S

    S = S | (1 << idx)


def clearBit(idx):
    global S

    S = S & ~(1 << idx)


def toggleBit(idx):
    global S

    S = S ^ (1 << idx)


# M (1 ~ 3,000,000)
M = int(stdin.readline().rstrip())

for _ in range(M):
    cmds = stdin.readline().rstrip().split()

    if cmds[0] == "add":
        # update bit
        idx = int(cmds[1])
        setBit(idx - 1)
    elif cmds[0] == "remove":
        # clear bit
        idx = int(cmds[1])
        clearBit(idx - 1)
    elif cmds[0] == "check":
        # get bit
        idx = int(cmds[1])
        if getBit(idx - 1):
            print(1)
        else:
            print(0)
    elif cmds[0] == "toggle":
        # change bit
        idx = int(cmds[1])
        toggleBit(idx - 1)
    elif cmds[0] == "all":
        # update all bits
        # 1111 1111 1111 1111 1111
        S = (1 << 21) - 1
    elif cmds[0] == "empty":
        # clear all bits
        S = 0
