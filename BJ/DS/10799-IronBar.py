import sys

s = sys.stdin.readline().rstrip()

bar = 0
total = 0

i = 0
while i < len(s):
    if s[i] == "(" and s[i + 1] == ")":  # laser
        total += bar
        i += 1
    elif s[i] == "(":  # start bar
        bar += 1
    elif s[i] == ")":  # end bar
        bar -= 1
        total += 1
    i += 1

print(total)