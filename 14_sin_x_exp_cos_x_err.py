#Sin x expression

theta=[0,30,45,60,90]
ref=[0,0.5,0.707106,0.866025,1]

def factorial(a):
    t=1
    while a!=1:
        t=t*(a)
        a=a-1
    return t

sinl=[]
for n in theta:
    n1=n*(3.14159265/180)
    sinv=[]
    for t in range(2,7,2):
        sum1=0
        term=n1
        for i in range(1,t+1):
            sum1=sum1+term
            term=n1**(2*i+1)
            #term=(term**(2*i+1))
            term=((-1)**i)*term/factorial(2*i+1)
        sinv.append(sum1)
    sinl.append(sinv)

#Cos X Error

error=[]
for i in range(0,len(sinl)):
    ep=[]
    for j in range(0,len(sinl[i])):
        if i==0:
            ep.append(0)
        else:
            ep.append((abs(ref[i]-sinl[i][j])/ref[i])*100)
            #ep.append(delta)
    error.append(ep)

for i in range(0,len(error)):
    print("For angle",theta[i],": ")
    print("\tValues:\t\t\t",end="")
    for j in range(0,len(error[i])):
        print(sinl[i][j],end="\t")
    print()
    print("\tError Percentages:\t",end="")
    for j in range(0,len(error[i])):
        print(error[i][j],end="\t")
    print("\n")

