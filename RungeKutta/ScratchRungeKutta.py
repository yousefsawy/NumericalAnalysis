import numpy as np
import sympy as sp

#Function that turns expression from string to mathematical function
def string_to_function_3parameters(expr):
    x, y, z = sp.symbols('x y z')
    func = sp.sympify(expr)
    func = sp.lambdify((x, y, z), func, "numpy")
    return func

def string_to_function_2parameters(expr):
    x, y = sp.symbols('x y')
    func = sp.sympify(expr)
    func = sp.lambdify((x, y), func, "numpy")
    return func

#To solve the problem using Runge Kutta Method, we enter the inputs:
#The ordinary differential equations
#The exact equations
#The current x
#The initial vector 
def Runge_Kutta(DE_Systems, Exact_Systems, x1, initialVector):

    #Calculating the step value
    h = x1 - initialVector[0] 
    
    #calculating the length of the array  DE_Systems
    num_equations = len(DE_Systems) 

    #turning each equation from string to mathematical functions
    if num_equations == 1:
        Diff_Eqns = [string_to_function_2parameters(expr) for expr in DE_Systems]
        Exact_Eqns = [string_to_function_2parameters(expr) for expr in Exact_Systems]
    elif num_equations == 2:
        Diff_Eqns = [string_to_function_3parameters(expr) for expr in DE_Systems]
        Exact_Eqns = [string_to_function_3parameters(expr) for expr in Exact_Systems]
    
    #Initializing needed arrays
    y = np.zeros(num_equations)
    True_Error = np.zeros(num_equations)
    constants1 = np.zeros(num_equations)
    constants2 = np.zeros(num_equations)
    constants3 = np.zeros(num_equations)
    constants4 = np.zeros(num_equations)

    #now we will calculate the runge kutta constants
    if num_equations == 1:
        for i in range(num_equations):
            constants1[i] = Diff_Eqns[i](initialVector[0], initialVector[1]) 

        x2=initialVector[0] + h/2
        y2=initialVector[1] + constants1[0]*h/2

        for i in range(num_equations):
            constants2[i] = Diff_Eqns[i](x2, y2)  

        x3=initialVector[0] + h/2
        y3=initialVector[1] + constants2[0]*h/2

        for i in range(num_equations):
            constants3[i] = Diff_Eqns[i](x3, y3)  
    
        x4=initialVector[0] + h
        y4=initialVector[1] + constants3[0]*h
    
        for i in range(num_equations):
            constants4[i] = Diff_Eqns[i](x4, y4)
        
        
    elif num_equations == 2:

     for i in range(num_equations):
       constants1[i] = Diff_Eqns[i](initialVector[0], initialVector[1], initialVector[2]) 

     x2=initialVector[0] + h/2
     y2=initialVector[1] + constants1[0]*h/2
     z2=initialVector[2] + constants1[1]*h/2

     for i in range(num_equations):
        constants2[i] = Diff_Eqns[i](x2, y2, z2)  

     x3=initialVector[0] + h/2
     y3=initialVector[1] + constants2[0]*h/2
     z3=initialVector[2] + constants2[1]*h/2

     for i in range(num_equations):
       constants3[i] = Diff_Eqns[i](x3, y3, z3)  

     x4=initialVector[0] + h
     y4=initialVector[1] + constants3[0]*h
     z4=initialVector[2] + constants3[1]*h

     for i in range(num_equations):
       constants4[i] = Diff_Eqns[i](x4, y4, z4)
    
    for i in range(num_equations):
     y[i] = initialVector[i+1] + h*(constants1[i] + 2*(constants2[i] + constants3[i]) + constants4[i])/6  
     if num_equations == 1:
        True_Error[i] = 100*abs((Exact_Eqns[i](x1, 0) - y[i])/Exact_Eqns[i](x1, 0))
     elif num_equations == 2:
        True_Error[i] = 100*abs((Exact_Eqns[i](x1, 0, 0) - y[i])/Exact_Eqns[i](x1, 0, 0))

    return y,True_Error