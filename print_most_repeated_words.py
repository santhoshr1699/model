n=input()
x=n[0]
for y in n:
    if (n.count(x)<n.count(y)):
        x=y
print(x)
