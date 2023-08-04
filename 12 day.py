t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    A=(a/10)*100
    B=(b/20)*100
    if(A==B):
        print("Any")
    elif(A>B):
        print("First")
    else:
        print("Second")
    
