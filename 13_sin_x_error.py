L =[0,0.5,0.707106,0.866025,1]
X = [0,30,45,60,90]
n1 = [2,4,6]
valmat = []
errmat = []
for a in range(0,5):
    x1=X[a]*3.1415926/180
    errlist = []
    vallist = []
    for b in range(0,3):
        n=n1[b]
        term=x1
        sum1=0
        for i in range(1,n+1):
            sum1=sum1+term
            term=x1**(2*i+1)
            f=1
            for j in range(1,2*i+2):
                f=f*j
            term=((-1)**i)*term/f
        vallist.append(sum1)
        if(L[a]==0):
            errlist.append(0)
        else:
            errlist.append((abs(L[a]-sum1)/L[a])*100)
    errmat.append(errlist)
    valmat.append(vallist)
for j in range(0,5):
    print("Sin(",X[j],"):")
    print("\tValues:\t\t",valmat[j])
    print("\tError %age:\t",errmat[j])
    print("\n")
