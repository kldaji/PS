import sys

n = int(sys.stdin.readline().rstrip())

n_list = map(int, sys.stdin.readline().rstrip().split())

n_dict = {}

for nl in n_list:
    if nl not in n_dict:
        n_dict[nl] = 1
    else:
        n_dict[nl] += 1

m = int(sys.stdin.readline().rstrip())

m_list = map(int, sys.stdin.readline().rstrip().split())

for ml in m_list:
    if ml not in n_dict:
        print(0, end=" ")
    else:
        print(n_dict[ml], end=" ")
