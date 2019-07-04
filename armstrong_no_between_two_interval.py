a,b=map(int,input("").split())
for i in range(a,b+1):
  num=i
  r=0
  while(i>0):
    digit=i%10
    r=r+digit**3
    i=i//10
  if(i==r):
    print(i)
