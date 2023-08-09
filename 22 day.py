t = int(input())
for i in range(t):
    n = int(input())
    coefficients = list(map(int, input().split()))
    degree = 0
    for i in range(n):
        if coefficients[i] != 0:
            degree = i
    print(degree)
