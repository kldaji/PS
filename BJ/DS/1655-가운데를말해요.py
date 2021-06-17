from sys import stdin, stdout
import heapq

N = int(stdin.readline().rstrip())

# MAX HEAP
A = []

# MIN HEAP
B = []

# A에서의 최댓값은 B에서의 최솟값보다 커야한다.
# n(A) == n(B) || n(A) = n(B) + 1


for _ in range(N):
    num = int(stdin.readline().rstrip())

    if len(A) == len(B):
        # A에 추가
        heapq.heappush(A, -num)
    else:
        # B에 추가
        heapq.heappush(B, num)

    if B and -A[0] > B[0]:
        # A의 최대값이 B의 최솟값보다 클 때
        m = -heapq.heappop(A)
        n = heapq.heappop(B)
        heapq.heappush(A, -n)
        heapq.heappush(B, m)

    print(-A[0])
