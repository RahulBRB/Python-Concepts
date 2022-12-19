# Convert to binary w/o diving by 2
a=int(input('Enter a No.: '))
n=a
l1=[]
while n!=0:
    l1.append(n&1)
    n=n>>1
l1=list(reversed(l1))
for i in range(0,len(l1)):
    print(l1[i],end="")
