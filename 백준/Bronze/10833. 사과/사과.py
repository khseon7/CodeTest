import sys
N=int(sys.stdin.readline())
sum=0
for _ in range(N):
  a,b=map(int,sys.stdin.readline().split())
  sum+=b%a
print(sum)