t=int(input())
for i in range(t):
    x,a,b=map(int,input().split())
    total=(1*a)+(2*b)
    if (total>= x):
        print("Qualify")
    else:
        print("Not Qualify")






