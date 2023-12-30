from re import X
import numpy as np
import sympy as sp
import math
import matplotlib.pyplot as plt
'''
---------------------------------------about section---------------------------------------
steps of solution: 
case 1: a and b not infinity where a is the upper limit and b is the lower limit 
y=mt+c, m=(a-b)/2, c=(a+b)/2, dy=mdt 
xnew= (((a - b) / 2) * arrX) + ((b + a) / 2)
I=sum(F(ti)*Ci)*dy
I = sum(arrC * Function(xnew)) * 0.5 * (a - b)

case 2: a is inf and b not 
x=1/y, dx=--1/x^2, bnew=1/b, anew=1/a=0 
y=mt+c, m=(bnew-anew)/2, c=(bnew+anew)/2, dy=m
xnew = (((1/b - 1 / a) / 2) * arrX) + ((1/b + 1 / a) / 2)
I=sum(F(ti)*Ci)*dy*-1/x^2
I = sum(arrC * Function(1 / xnew) * (-1 / (xnew ** 2))) * 0.5 * (1/a - 1 / b)

case 3: b is inf and a not 
x=1/y, dx=--1/x^2, bnew=1/b=0, anew=1/a 
y=mt+c, m=(anew-bnew)/2, c=(bnew+anew)/2, dy=m
xnew = (((1/a - 1 / b) / 2) * arrX) + ((1/b + 1 / a) / 2)
I=sum(F(ti)*Ci)*dy*-1/x^2
I = sum(arrC * Function(1 / xnew) * (-1 / (xnew ** 2))) * 0.5 * (1/b - 1 / a)
--------------------------------------------------------------------------------------------
'''
#input function from user need to be integrated used for testng
def Function(x):
    #return (2*x)/((((x**3)))+3)
    return (2)/((3*((x**3)))+1)

#input analytical function to calculate true error used for testing
def AnalyticalFunction(x):
    return (0.5)*(math.atan(x))

#input analytical function to calculate true error in case of either of the limits is infinity using for testing
def AnalyticalFunctionInf(x):
    FAn=AnalyticalFunction(1/x)
    return FAn


 #returns exact value
def Exact_Evaluator(a, b):
    if a != np.inf or b != np.inf:
        exact_a = AnalyticalFunction(a)
        exact_b = AnalyticalFunction(b)
        ex = exact_a - exact_b
        return ex
    elif (a == np.inf or a == -np.inf) and (b != np.inf and b != -np.inf):
        exact_a=AnalyticalFunctionInf(0)
        exact_b=AnalyticalFunctionInf(1/b)
        ex=exact_a-exact_b
        return ex
    elif (b == np.inf or b == -np.inf) and (a != np.inf and a != -np.inf):
        exact_a=AnalyticalFunctionInf(1/a)
        exact_b=AnalyticalFunctionInf(0)
        ex=exact_a-exact_b
        return ex

#upper limit -> a, lower limit -> b
#I in case n=2
def Gauss_Legendre_n2( a, b):
        arrX= np.array([-0.577350269,0.577350269])    #defining an array of the values of x
        arrC= np.array([1,1])                         #defining an array of the values of c

        if a != np.inf and a != -np.inf and b != np.inf and b != -np.inf:
            xnew = (((a - b) / 2) * arrX) + ((b + a) / 2)
            I = sum(arrC * Function(xnew)) * 0.5 * (a - b)
        elif (a == np.inf or a == -np.inf) and (b != np.inf and b != -np.inf):
            xnew = (((1/b - 1 / a) / 2) * arrX) + ((1/b + 1 / a) / 2)
            I = sum(arrC * Function(1 / xnew) * (-1 / (xnew ** 2))) * 0.5 * (1/a - 1 / b)
        elif (b == np.inf or b == -np.inf) and (a != np.inf and a != -np.inf):
            xnew = (((1 / a - 1/b) / 2) * arrX) + ((1 / b + 1/a) / 2)
            I = sum(arrC * Function(1 / xnew) * (-1 / (xnew ** 2))) * 0.5 * (1 / b - 1/a)
        else:
            xnew = (((1 / b - 1 / a) / 2) * arrX) + ((1 / b + 1 / a) / 2)
            I = sum(arrC * Function(1 / xnew) * (-1 / (xnew ** 2))) * 0.5 * (1 / a - 1 / b)
        return I

#I in cas n=3
def Gauss_Legendre_n3(a, b):
    arrX = np.array([-0.774596669, 0, 0.774596669])
    arrC = np.array([0.5555556, 0.8888889, 0.5555556])

    if a != np.inf and a != -np.inf and b != np.inf and b != -np.inf:
        xnew = (((a - b) / 2) * arrX) + ((b + a) / 2)
        I = sum(arrC * Function(xnew)) * 0.5 * (a - b)
    elif (a == np.inf or a == -np.inf) and (b != np.inf and b != -np.inf):
        xnew = (((1/a - 1 / b) / 2) * arrX) + ((1/b + 1 / a) / 2)
        I = sum(arrC * Function(1 / xnew) * (-1 / (xnew ** 2))) * 0.5 * (1/a - 1 / b)
    elif (b == np.inf or b == -np.inf) and (a != np.inf and a != -np.inf):
        xnew = (((1 / b - 1/a) / 2) * arrX) + ((1 / b + 1/a) / 2)
        I = sum(arrC * Function(1 / xnew) * (-1 / (xnew ** 2))) * 0.5 * (1 / b - 1/a)
    else:
        xnew = (((1 / b - 1 / a) / 2) * arrX) + ((1 / b + 1 / a) / 2)
        I = sum(arrC * Function(1 / xnew) * (-1 / (xnew ** 2))) * 0.5 * (1 / b - 1 / a)

    return I

#final output
def Final(a, b, n):
    if n == 3:
        In = Gauss_Legendre_n3(a, b)
        return In
    elif n==2:
        In=Gauss_Legendre_n2(a,b)
        return In
    else:
        print("Error: enter valid range for n either 2 or 3")
        new = input("Enter valid value for n:")
        while new != '2' and new != '3':
            print("Error: Invalid value for n")
            new = input("Enter valid value for n:")
        print(" n= " + new)
        In=Final(a,b,int(new))
        return In



#lower b upper a
#In = Final(np.inf, 5, 3)
In = Final(1/5, 0, 3)
print("Result = " + str(round(In, 4)))

def ChosenExactMethod (choice,a,b):
 ChoosenExactMethod=choice # 1 if given analytical function ,, 2 if given exact value
 if ChoosenExactMethod == 1:
    def GetExact(a, b):
        exact_Analytical=Exact_Evaluator(a, b)
        return exact_Analytical

    def True_Error(exact_Analytical, In):
        Error = abs((exact_Analytical - In)) * 100 / exact_Analytical
        return Error

    exact_Analytical=GetExact(np.inf, 2)
    Error=True_Error(exact_Analytical, In)
    print("True error = " + str(round(Error, 2)) + " %")

 elif ChoosenExactMethod ==2:
    def True_Error(exact_given, In):
        Error = abs((exact_given - In)) * 100 / exact_given
        return Error

    exact_given=2.4
    Error=True_Error(exact_given, In)
    print("True error = " + str(round(Error, 2)) + " %")



#Plot of the input function
def GraphIn():
    x = np.linspace(-10, 10, 1000)
    y = Function(x)
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Plot of equation')
    plt.show()

#lower b upper a for testing
#In = Final(np.inf, 2, 3)
#print("Result = " + str(round(In, 4)))


