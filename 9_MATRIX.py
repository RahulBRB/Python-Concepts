#Take 2 matrix as input nd perform matrix addition

r = int(input("Enter number of rows : "))
c = int(input("Enter number of columns : "))
mat1 = []
mat2 = []
#1st matrix input
print("Enter elements of 1st matrix : ")
for i in range(0,r):
    a = []
    for j in range(0,c):
        x = int(input())
        a.append(x)
    mat1.append(a)
print("1st matrix is : ")
for i in range(0,r):
    for j in range(0,c):
        print(mat1[i][j],end = " ")
    print()
#2nd matrix input
print("Enter elements of 2nd matrix : ")
for i in range(0,r):
    b = []
    for j in range(0,c):
        y = int(input())
        b.append(y)
    mat2.append(b)
print("2nd matrix is : ")
for i in range(0,r):
    for j in range(0,c):
        print(mat2[i][j],end = " ")
    print()
#Matrix addition
result = []
for i in range(0,r):
    d = []
    for j in range(0,c):
        d.append(mat1[i][j] + mat2[i][j])
    result.append(d)
print("The matrix is : ")
for i in range(0,r):
    for j in range(0,c):
        print(result[i][j],end = " ")
    print()
#Matrix multiplication
