t = int(input())
for _ in range(t):
    x = int(input())
    coins_5= 0
    coins_10= 0
    coins_10 = x // 10
    x %= 10
    coins_5 = x // 5
    x %= 5
    if x != 0:
        print(-1)
    else:
       print(coins_5 + coins_10)
