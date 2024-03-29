import numpy as np

def PCA(A):
    #Get the mean values of each column
    Mean = np.mean(A.T,axis = 1)
    #Centering the columns
    Center = A - Mean
    #Calculating the covaraince matrix
    V = np.cov(Center.T)
    print("\nCovariance matrix:")
    print(V)
    #Eigendecomposition of covariance matrix
    values,vectors = np.linalg.eig(V)
    P = vectors.T.dot(Center.T)
    proj = (vectors.T[:][:2]).T
    # projecting the data
    P = proj.T.dot(Center.T)
    return P

def matrix():
    n, m = map(int, input("\nEnter the number of rows and column of matrix : ").split()) 
  #defining the matrix and taking input.
    print("Enter elements row by row : \n")
    matri = np.array([input().strip().split() for _ in range(n)], int)
    print("\nMatrix:")
    print(matri)
  
    P = PCA(matri)
    print("\nPCA of matrix : ")
    print(P)
    print("\nAfter rounding off : ")
    for i in P :
        for j in i:
            print(round(j,2),end="\t")
        print("\n")
matrix()