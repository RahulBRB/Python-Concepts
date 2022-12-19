#Take input n integers to a list and find the maximum value and minimum value from it

n = int(input("Enter the number of elements : "))
print("\nEnter elements : \n")
L1 = []
for i in range(0,n):
    x = int(input())
    L1.append(x)
maxNum= L1[0]
for i in range(0,n):
    if L1[i] > maxNum:
        maxNum = L1[i]
        
minNum = L1[0]
for i in range(1,n):
    if L1[i] < minNum:
        minNum = L1[i]
        
print("Max is : ",maxNum)
print("Min is : ",minNum)