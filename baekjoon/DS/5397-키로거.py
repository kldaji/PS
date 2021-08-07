from sys import stdin, stdout

# Test Case
T = int(stdin.readline().rstrip())

for _ in range(T):
    s1 = []
    s2 = []

    stats = stdin.readline().rstrip()

    for stat in stats:
        if stat == "<":  # Move Left
            if s1:
                s2.append(s1.pop())
        elif stat == ">":  # Move Right
            if s2:
                s1.append(s2.pop())
        elif stat == "-":  # Remove Left one
            if s1:
                s1.pop()
        else:  # Add
            s1.append(stat)

    while s2:  # aggregate s2 to s1
        s1.append(s2.pop())

    # print s1
    print("".join(s1))
