import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from scipy.integrate import quad
import math
import MathSoln.errorCalc as errorCalc

def str2func(func):
    # Transforms the string to a mathematical function
    func = sp.sympify(func)
    # Return a lambda function that evaluates the sympy function
    return func

def simpsons_3_8_rule(f, a, b, n, mode):
    func = f
    f = sp.lambdify('x', f, 'numpy')
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)

    integral = y[0] + y[-1]
    for i in range(1, n):
        if i % 3 == 1:
            integral += 3 * y[i]
        elif i % 3 == 2:
            integral += 3 * y[i]
        else:
            integral += 2 * y[i]

    integral *= (3 * h / 8)

    if mode == 1:
        z = sp.symbols('x')
        third_derivative = sp.diff(func, z, 3)
        fourth_derivative = (third_derivative.subs(z, x[-1]) - third_derivative.subs(z, x[0])) / (x[-1] - x[0])
        error = ((x[-1] - x[0]) ** 5 * fourth_derivative) / (
                    6840 * n **4)  # Error calculation using scipy's quad function
    else:
        error = errorCalc.get_error(a, b, y)

    return integral, error

def get_user_input():
    choice = int(input("Enter 1 to input a function, or 0 to input points: "))
    return choice

def main():
    user_choice = get_user_input()

    if user_choice == 1:
        # Example 1: Using function equation
        fstring = input("Enter the Function: ")
        a = float(input("Enter the lower bound: "))
        b = float(input("Enter the upper bound: "))
        n = int(input("Enter the number of Intervals: "))

        if n % 3 != 0 or n <= 0:
            print("Invalid Number of Intervals")

        else:
            func = str2func(fstring)
            integral_result, error_result = simpsons_3_8_rule(func, a, b, n, user_choice)
            print(f"Integral result: {integral_result}, Error: {error_result}")

    elif user_choice == 0:
        # Example 2: Using array of pair points
        a = float(input("Enter the lower bound: "))
        b = float(input("Enter the upper bound: "))
        n = int(input("Enter the number of Intervals: "))
        if n < 1 or n % 3 != 0:
            print("Invalid Number of Intervals")
        else:
            h = (b - a) / n
            points = []
            for i in range(0, n + 1):
                y = float(input(f"Enter y({a + i * h}): "))
                point = [a + i * h, y]
                points.append(point)

            points = np.array(points)

            a_points, b_points = points[0, 0], points[-1, 0]
            integral_result_points, error_result_points = simpsons_3_8_rule(
                lambda x: np.interp(x, points[:, 0], points[:, 1]), a_points, b_points, n, user_choice
            )
            print(f"Integral result: {integral_result_points}, Error: {error_result_points}")

    else:
        print("Invalid choice. Please enter 0 or 1.")

main()