from sys import *

N = int(stdin.readline().rstrip())

# 좋은 단어
good_word = 0

for _ in range(N):
    # 단어
    word = stdin.readline().rstrip()

    # 스택
    stack = []

    # 좋은 단어 인가?
    is_good_word = True

    for i in range(len(word)):
        if not stack:
            stack.append(word[i])
        else:
            if word[i] == stack[-1]:
                # 같은 알파벳일 때 pop
                stack.pop()
            else:
                stack.append(word[i])

    if stack:  # empty가 아니라면 좋은 단어가 아니다.
        is_good_word = False

    if is_good_word:
        good_word += 1

print(good_word)
