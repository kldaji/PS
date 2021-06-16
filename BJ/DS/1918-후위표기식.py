from sys import stdin, stdout

expr = stdin.readline().rstrip()

s1 = []
s2 = []

for ex in expr:
    if ex == "(":
        s2.append(ex)
    elif ex == "*" or ex == "/":
        # 우선순위가 같은 *, / 일때만 append
        while s2 and (s2[-1] == "*" or s2[-1] == "/"):
            s1.append(s2.pop())
        s2.append(ex)
    elif ex == "+" or ex == "-":
        # 우선순위가 낮은 ( 을 제외하고 모두 append
        while s2 and s2[-1] != "(":
            s1.append(s2.pop())
        s2.append(ex)
    elif ex == ")":
        while s2 and s2[-1] != "(":
            s1.append(s2.pop())
        s2.pop()
    else:
        s1.append(ex)

while s2:
    s1.append(s2.pop())

print("".join(s1))
