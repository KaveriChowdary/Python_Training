n,m,w=map(int,input().split())
flower=list(map(int,input().split()))
minh=min(flower)
print(minh+abs(m-w))
    