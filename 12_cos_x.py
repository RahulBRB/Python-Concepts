x=float(input("Enter the degree: "))
x1=x*3.1415926/180
n=int(input("Enter n: "))
term=1
sum1=0
for i in range(1,n+1):
    sum1=sum1+term
    term=(term*x1*x1)
    f=1
    for j in range(1,2*i+2):
        f=f*j
    term=((-1)**i)*term/f
print("cos(",x,") =",sum1)
    
