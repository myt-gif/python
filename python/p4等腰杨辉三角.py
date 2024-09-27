n = int(input())
a = [[0] * n for _ in range(n)]

for i in range(n):
    a[i][0] = 1
    for j in range(1, i + 1):
        a[i][j] = a[i - 1][j - 1] + a[i - 1][j]

for i in range(n):
    for j in range(n-i-1):
        print(end="  ")
    for j in range(i + 1):
        print(f'{a[i][j]:>5}', end='')
    print()