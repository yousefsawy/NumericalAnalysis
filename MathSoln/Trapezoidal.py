from cmath import nan
import sympy as sp

#Description = "Trapezoidal Integration is a technique for numerical integration which works by taking intervals and approximating them into trapezoids then calculating its area.\n"
#"Its not as accurate as the rest of the numerical integration methods as its order of error is O(h^2). You can increase the accuracy of the calculations by increasing the number of intervals."

#Formula = "Integration from a to b f(x) = h/2 * (F(a) + 2 * summation from i = 1 to n-1 F(xi) + F(b))

def str2func(func):

     # Transforms the string to a mathematical function
     func = sp.sympify(func)

     # Return a lambda function that evaluates the sympy function
     return lambda x: func.subs("x", x).evalf()

# Integrates using the trapezoidal method if given function
def TrapezoidalFunction(f,a,b,n):
    h = (b-a)/n
    summation = 0
    fa = f(a)
    x = sp.symbols('x')
    # Checks if any of them is either undefined or infinity then calculates the limit.
    if fa == sp.nan or fa == sp.zoo:
        fa = sp.limit(f(x), x, a)
    fb = f(b)
    if  fb == sp.nan or fb == sp.zoo:
        fb = sp.limit(f(x), x, b)
    for i in range(1, n):
        val = f(a + i * h)
        # Checks if it is either undefined or infinity then calculates the limit.
        if val == sp.nan or val == sp.zoo:
            val = sp.limit(f(x), x, a + i * h)
        summation += val
    return h/2*(fa + fb + 2*summation)

# Integrates using the trapezoidal method if given table
def TrapezoidalTable(h,y):
    n = len(y)
    summation = 0
    for i in range(0, n):
        if i == 0 or i == n-1:
            summation += y[i]
        else:
            summation += 2*y[i]
    return h/2 * summation

# Calculates finite difference for error if given function
def FiniteDiff(f,a,h):
    x = sp.symbols('x')
    fxmin = f(a-h)
    # Checks if any of them is either undefined or infinity then calculates the limit.
    if fxmin == sp.nan or fxmin == sp.zoo:
        fxmin = sp.limit(f(x),x,a-h)
    fxmax = f(a+h)
    if fxmax == sp.nan or fxmax == sp.zoo:
        fxmax = sp.limit(f(x),x,a+h)
    return (fxmax-fxmin)/(2*h)

# Calculates the error of the integration if given function
def TrapErrorFunction(f,a,b,h):
    finite = FiniteDiff(f,b,h) - FiniteDiff(f,a,h)
    return h**2/12 * finite

# Simple Difference Table
def DifferenceTable(y):
    n = len(y)
    out = []
    for i in range(0,n-1):
        out.append(y[i+1] - y[i])
    return out

# Calculates the error of the integration if given table
def TrapErrorTable(y,a,b,h):
    try:
        dy = DifferenceTable(y)
        dy2 = DifferenceTable(dy)
        avgdy2 = sum(dy2)/len(dy2)
        return (h**2 * (b-a) * avgdy2)/12
    except ZeroDivisionError:
        return 0
    

try:
    choice = input("What type of data do you have (1 for function, 2 for table): ")
    if not choice:
        raise SyntaxError("You didnt enter a number.")
    choice = int(choice)
    if choice != 1 and choice != 2:
        raise ValueError("Wrong selection.")
except Exception as e:
    print(e)


# Function
if choice == 1:
    try:
        var = input("Enter your dependent variable: ")
        a = input("Enter your lower limit: ")
        b = input("Enter your upper limit: ")
        n = input("Enter your number of intervals: ")


        # Checks if any variable is empty
        if not var or not a or not b or not n:
            raise SyntaxError

        # Converts the variables to their respective types
        a = float(a)
        b = float(b)
        n = int(n)
        

        # Checks if the upper and lower limit are equal.
        if a == b:
            raise SyntaxError

        # Converts string to a mathematical function
        func_string = input("Enter your function: ")

        # Checks if the string is empty.
        if not func_string:
            print("Empty Function.")
        else:
            func = str2func(func_string)
            try:
                result = TrapezoidalFunction(func, a, b, n)
                if result == float('inf') or result == float('-inf'):
                    print("Numerical integration failed, because the integral is divergent.")
                else:
                    print(f"Approximate integral: {round(result,4)}")
                    error = TrapErrorFunction(func,a,b,(b-a)/n)
                    print(f"Error: {round(error,4)}")
            except Exception:
                print("Incorrect function, you either entered an undefined function or used multiple variables.")
    except SyntaxError:
        print("Wrong entry of data.")
    except ValueError:
        print("Wrong entry of data.")

# Table
elif choice == 2:
    try:
        ############################ done #############################
        a = input("Enter your lower bound: ")
        b = input("Enter your upper bound: ")
        n = input("Enter the number of intervals: ")

        # Checks if a,b or n are empty
        if not a or not b or not n:
            raise SyntaxError("Wrong entry of data.")

        a = float(a)
        b = float(b)
        n = int(n)
        y = []
        h = (b-a)/n
        # Inputs for f(x)
        for i in range(0,n+1):
            p = input(f"Enter f({a+i*h}): ")
            # Checks if p is empty
            while not p:
                p = input(f"Enter f({a+i*h}): ")
            y.append(float(p))
        # Calculates the integral.
        result = TrapezoidalTable(h,y)
        print(f"Approximate integral: {round(result,4)}")
        # Calculates the error.
        error = TrapErrorTable(y,a,b,h)
        print(f"Error: {round(error, 4)}")
    except Exception as e:
        print(e)
        ################################################################
