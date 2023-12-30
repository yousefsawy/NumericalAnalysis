import numpy as np
from numpy.linalg import eig

#Get the maximum eigenvalue and its corresponding eigenvector 
def maxeigen(matrix1, matrix2, iterations):
    lamda_max = 0
    for i in range(iterations):
        x = np.matmul(matrix1, matrix2)
        temp = abs(x)
        x = x / temp.max()
        lamda_max = temp.max()
    return (lamda_max, x)
#Get the minimum eigenvalue and its corresponding eigenvector
def mineigen(matrix1, matrix2, iterations):
    inv = np.linalg.inv(matrix1)
    lamda_min = 0
    for i in range(iterations):
        x = np.matmul(inv, matrix2)
        temp = abs(x)
        x = x / temp.max()
        lamda_min = 1 / temp.max()
    return (lamda_min, x)
#Get the maximum deflation matrix
def max_deflation_matrix(matrix1, matrix2, lamda_max):
    matrix2_norm_sq = np.linalg.norm(matrix2)**2
    matrix2_t = np.transpose(matrix2)
    result_matrix=[[element*lamda_max for element in row] for row in matrix2]
    max_deflation_matrix = matrix1 -  result_matrix @ matrix2_t / matrix2_norm_sq
    return max_deflation_matrix

#Get the minimum deflation matrix
def min_deflation_matrix(matrix1, matrix2,lamda_min):
    matrix2_norm_sq = np.linalg.norm(matrix2)**2
    matrix2_t = np.transpose(matrix2)
    matrix1_inv=np.linalg.inv(matrix1)
    result_matrix=[[element*lamda_min for element in row] for row in matrix2]
    min_deflation_matrix = matrix1_inv - result_matrix @ matrix2_t / matrix2_norm_sq
    return min_deflation_matrix
#Get the second maximum eign value 
def secondmax(max_deflation_matrix, matrix2, iterations):
    second_max = 0 
    for i in range(iterations):
        x = np.matmul(max_deflation_matrix, matrix2)
        temp = abs(x)
        x = x / temp.max()
        second_max = temp.max()
    return (second_max, x)
#Get the second minimum eign value 
def secondmin(min_deflation_matrix, matrix2, iterations):
    inv = np.linalg.inv(min_deflation_matrix)
    second_min = 0 
    for i in range(iterations):
        x = np.matmul(inv, matrix2)
        temp = abs(x)
        x = x / temp.max()
        second_min = 1 / temp.max()
    return (second_min, x)
def startApp():  
    #ask user to enter the dimensions of a matrix
    r1 = int(input("Enter number of rows in Matrix: "))
    c1 = int(input("Enter number of columns in Matrix: "))
    matrix1 = []
    #enter the elements of each index in the matrix
    for i in range(r1):
        c = []
        for j in range(c1):
            element = float(input("Enter element in row " + str(i) + ", column " + str(j) + ": "))
            c.append(element)
        matrix1.append(c)
    
    for i in range(r1):
        for j in range(c1):
            print(matrix1[i][j], end=" ")
        print()
    #ask user to enter the initial eigenvector dimensions
    r2 = int(input("Enter number of rows in vector: "))
    c2 = int(input("Enter number of columns in vector: "))
    matrix2 = []
    #enter the elements of each index of the matrix
    for i in range(r2):
        c = []
        for j in range(c2):
            element = float(input("Enter element in row " + str(i) + ", column " + str(j) + ": "))
            c.append(element)
        matrix2.append(c)
    
    for i in range(r2):
        for j in range(c2):
            print(matrix2[i][j], end=" ")
        print()
    #check if the matrices are multiplicable
    if c1 == r2:
        print("Valid")
    else:
        print("Invalid. Please try again")
        startApp()
        return
    #ask the user to enter a stopping criteria
    iterations = int(input("Enter number of iterations "))
    #ask the user to enter a requirement
    print("required output:")
    print("1- maximum eigen value")
    print("2- minimum eigen value")
    print("3- max def matrix")
    print("4- min def matrix")
    print("5- second max")
    print("6- second min")
    print("0- Exit")
    choices1 = ["1 maximum eigen value", "2 minimum eigen value", "3 max def matrix", "4 min def mat", "5 second max",
                 "6 second min"]
    choice1 = int(input("Enter your Choice: "))
    while choice1 !=0:
        if choice1 == 1:
            print("Maximum Eigen value",maxeigen(matrix1, matrix2, iterations))
        elif choice1 == 2:
            print("Minimum Eigen value",mineigen(matrix1, matrix2, iterations))
        elif choice1 == 3:
            print("Maximum deflated matrix",max_deflation_matrix(matrix1, matrix2, maxeigen(matrix1, matrix2, iterations)[0]))
        elif choice1 == 4:
            print("Minimum deflated matrix",min_deflation_matrix(matrix1, matrix2, mineigen(matrix1, matrix2, iterations)[0]))
        elif choice1 == 5:
            print("Second maximum eigen value",secondmax(max_deflation_matrix(matrix1, matrix2, maxeigen(matrix1, matrix2, iterations)[0]), matrix2, iterations))
        elif choice1 == 6:
            print("Second minimum eigen value",secondmin(min_deflation_matrix(matrix1, matrix2, mineigen(matrix1, matrix2, iterations)[0]), matrix2, iterations))
        else:
            print("Invalid choice. Please try again.")
        choice1 = int(input("Enter your Choice: "))
startApp()