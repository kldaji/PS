import sys

n = int(sys.stdin.readline().rstrip())

stack = []
seq = []
op = []

for i in range(n):
    num = int(sys.stdin.readline().rstrip())
    seq.append(num)

curr_val = 0
not_equal_flag = False

for i in range(len(seq)):
    target_val = seq[i]
    if target_val > curr_val:
        for j in range(curr_val + 1, target_val + 1):
            stack.append(j)
            op.append("+")
        curr_val = target_val
        stack.pop()
        op.append('-')
    else:
        pop_value = stack.pop()
        if pop_value != seq[i]:
            not_equal_flag = True
            break
        else:
            op.append("-")


if not not_equal_flag:
    print("\n".join(op))
else:
    print("NO")