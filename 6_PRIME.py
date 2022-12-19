a=int (input('Enter a number: '))

s=0

for i in range (1,a+1):
    if (a%i==0):
        s=s+1
if(s==2):
    print("Number is prime")
else:
    print("the number is not prime")         
       