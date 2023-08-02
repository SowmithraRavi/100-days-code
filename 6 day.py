n=int(input())
for i in range(n):
    n,m,k=map(int,input().split())
    a=m*k
    if(a>=n):
        print("yes")
    else:
        print("No")
