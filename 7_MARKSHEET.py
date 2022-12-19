n=int(input("Enter your number: "))

if(n>100):
    print("INVALID!!")
elif(n>=90):
    print("E")
elif(n>=80):
    print("A++") 
elif(n>=70):
    print("A")
elif(n>=60):
    print("B") 
elif(n>=50):
    print("C")
elif(n>=40):
    print("D")
elif(n>=0):
    print("FAIL") 
else:
    print("INVALID!!")