m,r = map(int,input().split())
ans=(m*(m+1)*(m+2)/3-m)*2
ans+=(2.0**0.5-2)*((m*m-m)+(m*m-m-(m-1)*2))
ans/=(m**2)
ans*=r
print("{:.10f}".format(round(ans,10)))