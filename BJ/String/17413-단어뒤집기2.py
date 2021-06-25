"""
<String>
"""

from sys import *

S = stdin.readline().rstrip()

"""
<SIMPLE VERSION>
"""



"""
<CORRECT>

words = []

while True:
    # init
    left = -1
    right = -1

    # find "<"
    left = S.find("<", left + 1)

    if left > 0:
        # find word
        word = S[:left]
        words.append(word)
    elif left == 0:
        # find ">"
        right = S.find(">", left + 1)
        words.append(S[left : right + 1])
    elif left == -1:
        # no tag
        break

    # update S only one word
    S = S.replace(words[-1], "", 1)

if S:  # leftover
    words.append(S)

for word in words:
    if "<" in word:
        print(word, end="")
    else:
        if " " in word:
            # split space
            temp = word.split()
            for i in range(len(temp)):
                if i != len(temp) - 1:
                    print(temp[i][::-1], end=" ")
                else:
                    print(temp[i][::-1], end="")
        else:
            # no space
            print(word[::-1], end="")
"""