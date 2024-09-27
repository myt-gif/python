def solve(n):
    if n==0:
        return 1
    else:
        return n*solve(n-1)

n=(int)(input())
print(solve(n))