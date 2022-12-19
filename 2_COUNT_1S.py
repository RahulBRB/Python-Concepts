# Count no. of 1's in the binary of a number
a=int(input("Enter a No.: "))
n=a
c=0
while n!=0:
    n=n&(n-1)
    c+=1
print("No. of 1's in the binary of",a,"=",c)
