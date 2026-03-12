# Problem: B - How many?
# Platform: AtCoder
# Link: https://atcoder.jp/contests/abc214/tasks/abc214_b
# Difficulty: Beginner
# Language: Python
# Time Complexity: O(S^3)
# Space Complexity: O(1)

S = int(input())
T = int(input())

count = 0
for a in range(S + 1):
    for b in range(S - a + 1):
        for c in range(S - a - b + 1):
            if a * b * c <= T:
                count += 1

print(count)