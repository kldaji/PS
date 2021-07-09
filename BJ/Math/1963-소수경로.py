"""
<Math>
<BFS>
<Eratosthenes' sieve>
"""
from sys import *
from collections import deque

# <Eratosthenes' sieve> START
# max number
MAX = 10000

# check wether prime or not
CHECK = [True] * MAX

# init
CHECK[1] = False
CHECK[2] = True

# prime set
PRIME = set()

for i in range(2, MAX):
    if CHECK[i]:
        # prime
        if i >= 1000:
            PRIME.add(i)

        # check false not prime number
        for j in range(i * 2, MAX, i):
            CHECK[j] = False
# <Eratosthenes' sieve> END

# <BFS> START
def bfs(src, dest):
    # init queue
    queue = deque()
    # start
    queue.append((src, 0))
    VISIT[int(src)] = True

    while queue:
        curr, cnt = queue.popleft()

        # END condition
        if curr == dest:
            return cnt

        # 0 ~ 9
        for i in range(10):
            # j+1(th) position
            for j in range(4):
                tempList = list(curr)  # str -> list
                tempList[j] = str(i)  # change number
                tempNum = int("".join(tempList))  # list -> int
                if tempNum in PRIME and not VISIT[tempNum]:
                    queue.append((str(tempNum), cnt + 1))
                    VISIT[tempNum] = True
    # IMPOSSIBLE
    return -1


# <BFS> END

# TEST CASE
T = int(stdin.readline().rstrip())

for _ in range(T):
    # INPUT
    A, B = stdin.readline().rstrip().split()

    # VISIT
    VISIT = [False] * 10000

    # call BFS
    RET = bfs(A, B)

    # OUTPUT
    print("Impossible") if RET == -1 else print(RET)
