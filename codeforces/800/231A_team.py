# Problem: Team
# Platform: Codeforces
# Link: https://codeforces.com/problemset/problem/231/A

n = int(input())
count = 0

for _ in range(n):
    p, v, t = map(int, input().split())
    if p + v + t >= 2:
        count += 1

print(count)