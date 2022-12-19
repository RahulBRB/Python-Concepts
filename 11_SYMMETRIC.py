#SYMMETRIX OR NOT

def isSymmetric(mat, N):
    for i in range(N):
        for j in range(N):
            if (mat[i][j] != mat[j][i]):
                return False
    return True
 
 
# Driver code
mat = [[1, 3, 5], [3, 2, 4], [5, 4, 1]]
if (isSymmetric(mat, 3)):
    print ("Yes")
else:
    print ("No")