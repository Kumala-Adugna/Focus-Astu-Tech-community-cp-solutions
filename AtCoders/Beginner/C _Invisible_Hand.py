import bisect

# Read input
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Sort both arrays
A.sort()
B.sort()

# Binary search for minimum X
lo, hi = 1, 10**9 + 1
answer = hi

while lo <= hi:
    mid = (lo + hi) // 2

    # Count sellers ≤ mid
    s_count = bisect.bisect_right(A, mid)
    # Count buyers ≥ mid
    b_count = M - bisect.bisect_left(B, mid)

    if s_count >= b_count:
        answer = mid
        hi = mid - 1  # try smaller X
    else:
        lo = mid + 1  # need bigger X

print(answer)