from sys import stdin

T = int(stdin.readline().rstrip())

for _ in range(T):
    n = int(stdin.readline().rstrip())

    clothes = {}

    for _ in range(n):
        value, key = stdin.readline().rstrip().split()

        if key in clothes:
            # 동일한 key는 value를 계속 append해준다.
            clothes[key].append(value)
        else:
            clothes[key] = [value]

    case = 1
    for key, value in clothes.items():
        # 경우의 수
        case *= len(value) + 1

    print(case - 1)
