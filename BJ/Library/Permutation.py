from itertools import permutations

example = [1, 2, 3]

per = permutations(example)

for p in per:
    print(p)

"""
(1, 2, 3)
(1, 3, 2)
(2, 1, 3)
(2, 3, 1)
(3, 1, 2)
(3, 2, 1)
"""