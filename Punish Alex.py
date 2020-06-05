for _ in range(int(input())):
    n,k=map(int,input().split())
    if n==1:
        print(1)
    else:
        div=2*(n-1)
        rem=k%div
        #print((div%n)+(div//2))
        if rem==0:
            print(n-((div%n)+(div//n))+1)
        elif rem<=n:
            print(rem)
        else:
            rem2=rem%n+rem//n
            print(n-rem2+1)
