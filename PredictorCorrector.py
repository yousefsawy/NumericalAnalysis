import numpy as np
import math
from scipy.interpolate import interp1d
import sympy as sp


print("choose 1 for first order in a x, y \n")
print("choose 2 for first order x,y,z\n")
print("choose 3 for second order x,y,z\n")
tv = input()

if tv == "1":
    print(1)


    def convert_to_function(input_string):
        # Replace sin, cos, ln, exp with math.sin, math.cos, math.log, math.exp respectively
        input_string = input_string.replace('sin', 'np.sin')
        input_string = input_string.replace('cos', 'np.cos')
        input_string = input_string.replace('ln', 'np.log')
        input_string = input_string.replace('exp', 'np.exp')

        def func(x, y):
            return eval(input_string)

        return func


    # The Adams–Bashforth methods allow us explicitly to compute the approximate solution at an instant time from the solutions in previous instants
    # Adams methods are based on the idea of approximating the integrand with a polynomial within the interval (tn, tn+1).
    # Using a kth order polynomial results in a k+1th order method. There are two types of Adams methods, the explicit and the implicit types.
    # The explicit type is called the Adams-Bashforth (AB) methods and the implicit type is called the Adams-Moulton (AM) methods.
    # it is conditionally stable

    # constant step size is  used for simplicity, the method can also accommodate adaptive step sizes, adjusting dynamically based on the solution behavior.
    # Adaptive step sizes may be particularly beneficial for handling stiff equations or regions of rapid change in the solution.

    # define the function
    # dont enter division by zero
    def predictor(F, R, Q, n):
        # Define the ODE function
        z = R[-1] - Q[-2]
        x_end = R[-1] + z

        if len(R) > 3 and len(Q) > 3:
            if len(R) == len(Q):

                x_start = R[-4]
                # Set up initial values and parameters
                A = x_start  # starting time
                B = x_end  # ending time

                N = 4  # number of subintervals which is always 4 because the the adam bashforth formula with 4 used

                # Provide initial arrays for t and y (not necessarily at the same intervals)
                # put x array in t_intial
                t_initial = R
                # put y array in y_intial
                y_initial = Q

                # Interpolate the initial values to match the desired time steps

                # we could remove the interpolate and just substiute give function but
                # we interpoleted to check things in between  the values because we found out at first we substuited wrong
                # so we used inter polition and just didnt want to change it
                y_interpolated = interp1d(t_initial, y_initial, kind='linear', fill_value="extrapolate")

                # Initialize arrays
                # T is the x/time intervel array with the t or x that u want to calculate at

                T = np.linspace(A, B, N + 1)

                # W is the the value of the function  with the y  and x that you want to calculate value of the function
                W = np.zeros(N + 1)

                # Output file setup

                # Initialize using interpolated initial values
                # W is the y/y intervel array with the y that you want to calculate value of the function
                for i in range(N + 1):
                    W[i] = y_interpolated(T[i])
                #    print(f"{i + 1}   {T[i]:.3f} {W[i]:.7f}")

                # time end-time end/number of intervels
                # Calculate step size
                H = (B - A) / N

                # Predictor-corrector method for the remaining steps

                # Predictor step
                Part1 = 55.0 * F(T[-2], W[-2]) - 59.0 * F(T[-3], W[-3]) + 37.0 * F(T[-4], W[-4])
                Part2 = -9.0 * F(T[-5], W[-5])
                Wn = W[-2] + H * (Part1 + Part2) / 24.0

                # corrector step
                for i in range(n):
                    Part1 = 9.0 * F(T[-1], Wn) + 19.0 * F(T[-2], W[-2]) - 5.0 * F(T[-3], W[-3]) + F(T[-4], W[-4])
                    W[-1] = W[-2] + H * Part1 / 24.0
                    Wn = W[-1]

                    # print(F(T[-1],W[-1]))
                print("this is the y corrected")
                print(W[-1])
            else:
                print("not equal array sizes")
        else:
            print("minimum array size is 4")

        # print(f"{i + 2}   {T[i + 1]:.3f} {W[i + 1]:.7f}")


    # (y+(x*2+y*2)**0.5)/x
    # 1,1.2,1.4,1.6,1.8,2
    # 0,0.221,0.479,0.784,1.123,1.521

    func = convert_to_function("sin(x)+ln(y)*cos(x*2)")
    x_values = [0 0.5 1 1.5]
    y_values = [2 2.636 3.595 4.968]
    n = 10

    # firstly That you have to input the string. Which is then taken Through the function to be Equated to a math function.
    # Then you input two arrays The first array is the X or time values And the second array is the Y values Then you have to calculate. The. The step. Of your x/time
    # Then step between the x values or time values.
    # When you calculate all this, you call function called predictor. Which is made. Use a firstly send. Function which had been converted to math eqution.
    # Secondly, the acts or tea time array then y array, Then first value which should be taken into account in calculating the interpolating method.
    # Then the step. Then number of intervals, which is constantly four in our case.

    predictor(func, x_values, y_values, n)


elif tv == "2":
    print(2)


    # This is for changing the string input to math function
    def convert_to_function(input_string):
        # Replace sin, cos, ln, exp with math.sin, math.cos, math.log, math.exp respectively
        input_string = input_string.replace('sin', 'np.sin')
        input_string = input_string.replace('cos', 'np.cos')
        input_string = input_string.replace('ln', 'np.log')
        input_string = input_string.replace('exp', 'np.exp')

        def func(x, y, z):
            return eval(input_string)

        return func


    # The Adams–Bashforth methods allow us explicitly to compute the approximate solution at an instant time from the solutions in previous instants
    # Adams methods are based on the idea of approximating the integrand with a polynomial within the interval (tn, tn+1).
    # Using a kth order polynomial results in a k+1th order method. There are two types of Adams methods, the explicit and the implicit types.
    # The explicit type is called the Adams-Bashforth (AB) methods and the implicit type is called the Adams-Moulton (AM) methods.
    # it is conditionally stable

    # constant step size is  used for simplicity, the method can also accommodate adaptive step sizes, adjusting dynamically based on the solution behavior.
    # Adaptive step sizes may be particularly beneficial for handling stiff equations or regions of rapid change in the solution.

    # define the function
    # dont enter division by zero
    def predictor(F, R, Q, Z, n):
        # Define the ODE function
        if len(R) > 3 and len(Q) > 3:
            if len(R) == len(Q):
                z = x_values[-1] - x_values[-2]
                x_end = x_values[-1] + z

                x_start = x_values[-4]
                # Set up initial values and parameters
                A = x_start  # starting time
                B = x_end  # ending time

                N = 4  # number of subintervals which is always 4 because the the adam bashforth formula with 4 used

                # Provide initial arrays for t and y (not necessarily at the same intervals)
                # put x array in t_intial
                t_initial = R
                # put y array in y_intial
                y_initial = Q
                z_value = Z
                # Interpolate the initial values to match the desired time steps

                # we could remove the interpolate and just substiute give function but
                # we interpoleted to check things in between  the values because we found out at first we substuited wrong
                # so we used inter polition and just didnt want to change it
                y_interpolated = interp1d(t_initial, y_initial, kind='linear', fill_value="extrapolate")
                z_interpolated = interp1d(t_initial, z_value, kind='linear', fill_value="extrapolate")

                # Initialize arrays
                # T is the x/time intervel array with the t or x that u want to calculate at

                T = np.linspace(A, B, N + 1)

                # W is the the value of the function  with the y  and x that you want to calculate value of the function
                W = np.zeros(N + 1)

                V = np.zeros(N + 1)
                # Output file setup

                # Initialize using interpolated initial values
                # W is the y/y intervel array with the y that you want to calculate value of the function
                for i in range(N + 1):
                    W[i] = y_interpolated(T[i])
                #    print(f"{i + 1}   {T[i]:.3f} {W[i]:.7f}")
                for i in range(N + 1):
                    V[i] = z_interpolated(T[i])
                #    print(f"{i + 1}   {T[i]:.3f} {W[i]:.7f}")

                # time end-time end/number of intervels
                # Calculate step size
                H = (B - A) / N

                # Predictor-corrector method for the remaining steps

                # Predictor step
                Part1 = 55.0 * F(T[-2], W[-2], V[-2]) - 59.0 * F(T[-3], W[-3], V[-3]) + 37.0 * F(T[-4], W[-4], V[-4])
                Part2 = -9.0 * F(T[-5], W[-5], V[-5])
                Wn = W[-2] + H * (Part1 + Part2) / 24.0
                Vn = V[-2] + H * (Part1 + Part2) / 24.0

                # corrector step
                for i in range(n):
                    Part1 = 9.0 * F(T[-1], Wn, Vn) + 19.0 * F(T[-2], W[-2], V[-2]) - 5.0 * F(T[-3], W[-3], V[-3]) + F(
                        T[-4], W[-4], V[-4])
                    # print(F(T[-1], Wn,Vn))
                    W[-1] = W[-2] + H * (Part1) / 24.0
                    Wn = W[-1]
                    V[-1] = V[-1] + H * Part1 / 24.0
                    Vn = V[-1]

                # print(F(T[-1],W[-1]))
                print("this is the y corrected")
                print(W[-1])
            else:
                print("not equal array sizes")
        else:
            print("minimum array size is 4")

        # print(f"{i + 2}   {T[i + 1]:.3f} {W[i + 1]:.7f}")


    # (y+(x*2+y*2)**0.5)/x
    # 1,1.2,1.4,1.6,1.8,2
    # 0,0.221,0.479,0.784,1.123,1.521
    s = "sin(x)+ln(y)*cos(x*2)+z"
    func = convert_to_function(s)
    x_values = [0, 0.5, 1, 1.5]
    y_values = [2, 2.636, 3.595, 4.968]
    z_values = [0, 0, 0, 0]

    n = 10

    # firstly That you have to input the string. Which is then taken Through the function to be Equated to a math function.
    # Then you input two arrays The first array is the X or time values And the second array is the Y values Then you have to calculate. The. The step. Of your x/time
    # Then step between the x values or time values.
    # When you calculate all this, you call function called predictor. Which is made. Use a firstly send. Function which had been converted to math eqution.
    # Secondly, the acts or tea time array then y array, Then first value which should be taken into account in calculating the interpolating method.
    # Then the step. Then number of intervals, which is constantly four in our case.

    predictor(func, x_values, y_values, z_values, n)



elif tv == "3":
    print(3)


    # This is for changing the string input to math function
    def convert_to_function(input_string):
        # Replace sin, cos, ln, exp with math.sin, math.cos, math.log, math.exp respectively
        input_string = input_string.replace('sin', 'np.sin')
        input_string = input_string.replace('cos', 'np.cos')
        input_string = input_string.replace('ln', 'np.log')
        input_string = input_string.replace('exp', 'np.exp')

        def func(x, y, z):
            return eval(input_string)

        return func


    # The Adams–Bashforth methods allow us explicitly to compute the approximate solution at an instant time from the solutions in previous instants
    # Adams methods are based on the idea of approximating the integrand with a polynomial within the interval (tn, tn+1).
    # Using a kth order polynomial results in a k+1th order method. There are two types of Adams methods, the explicit and the implicit types.
    # The explicit type is called the Adams-Bashforth (AB) methods and the implicit type is called the Adams-Moulton (AM) methods.
    # it is conditionally stable

    # constant step size is  used for simplicity, the method can also accommodate adaptive step sizes, adjusting dynamically based on the solution behavior.
    # Adaptive step sizes may be particularly beneficial for handling stiff equations or regions of rapid change in the solution.
    def process_equation(s):
        s = s.replace(" ", "").strip()
        other_side = "0"

        idx = s.find("r")
        if idx == -1:
            print("r not found")
            return None

        # Find the start
        start = idx - 1
        while start >= 0:
            c = s[start]
            if c == '+' or c == '-':
                break
            start -= 1

        if start != -1:
            other_side += f"-({s[:start]})"

        # Find the end
        end = idx + 1
        while end < len(s):
            c = s[end]
            if c == '+' or c == '-':
                break
            end += 1

        if end != len(s):
            other_side += f"-({s[end + 1:]})"

        r_term = s[start + 1:end]
        first_part = r_term[:idx - start - 1]
        second_part = r_term[idx - start:end - 1]

        intersection = (first_part[-1] if first_part else "") + (second_part[0] if second_part else "")

        op = intersection
        if intersection == "**":
            op = "*"

        fp = first_part[:-1] if first_part else ""
        sp = second_part[1:] if second_part else ""

        term = fp + op + sp
        other_side = f"({other_side})/({1 if not term else ''})"

        return other_side


    # define the function
    # dont enter division by zero
    def predictor(F, R, Q, Z, n):
        # Define the ODE function
        # print(equ)

        if len(R) > 3 and len(Q) > 3:
            if len(R) == len(Q):
                z = x_values[-1] - x_values[-2]
                x_end = x_values[-1] + z

                x_start = x_values[-4]
                # Set up initial values and parameters
                A = x_start  # starting time
                B = x_end  # ending time

                N = 4  # number of subintervals which is always 4 because the the adam bashforth formula with 4 used

                # Provide initial arrays for t and y (not necessarily at the same intervals)
                # put x array in t_intial
                t_initial = R
                # put y array in y_intial
                y_initial = Q
                z_value = Z
                # Interpolate the initial values to match the desired time steps

                # we could remove the interpolate and just substiute give function but
                # we interpoleted to check things in between  the values because we found out at first we substuited wrong
                # so we used inter polition and just didnt want to change it
                y_interpolated = interp1d(t_initial, y_initial, kind='linear', fill_value="extrapolate")
                z_interpolated = interp1d(t_initial, z_value, kind='linear', fill_value="extrapolate")

                # Initialize arrays
                # T is the x/time intervel array with the t or x that u want to calculate at

                T = np.linspace(A, B, N + 1)

                # W is the the value of the function  with the y  and x that you want to calculate value of the function
                W = np.zeros(N + 1)

                V = np.zeros(N + 1)
                # Output file setup

                # Initialize using interpolated initial values
                # W is the y/y intervel array with the y that you want to calculate value of the function
                for i in range(N + 1):
                    W[i] = y_interpolated(T[i])
                #    print(f"{i + 1}   {T[i]:.3f} {W[i]:.7f}")
                for i in range(N + 1):
                    V[i] = z_interpolated(T[i])
                #    print(f"{i + 1}   {T[i]:.3f} {W[i]:.7f}")

                # time end-time end/number of intervels
                # Calculate step size
                H = (B - A) / N

                # Predictor-corrector method for the remaining steps

                # Predictor step
                Part1 = 55.0 * F(T[-2], W[-2], V[-2]) - 59.0 * F(T[-3], W[-3], V[-3]) + 37.0 * F(T[-4], W[-4], V[-4])
                Part2 = -9.0 * F(T[-5], W[-5], V[-5])
                Wn = W[-2] + H * (Part1 + Part2) / 24.0
                Vn = V[-2] + H * (Part1 + Part2) / 24.0

                # corrector step
                # for i in range(n):
                Part1 = 9.0 * F(T[-1], Wn, Vn) + 19.0 * F(T[-2], W[-2], V[-2]) - 5.0 * F(T[-3], W[-3], V[-3]) + F(T[-4],
                                                                                                                  W[-4],
                                                                                                                  V[-4])
                print(F(T[-1], Wn, Vn))
                W[-1] = W[-2] + H * (Part1) / 24.0
                Wn = W[-1]
                V[-1] = V[-1] + H * Part1 / 24.0
                Vn = V[-1]

                # print(F(T[-1],W[-1]))
                print("this is the y corrected")
                print(W[-1])
            else:
                print("not equal array sizes")
        else:
            print("minimum array size is 4")

        # print(f"{i + 2}   {T[i + 1]:.3f} {W[i + 1]:.7f}")


    # (y+(x*2+y*2)**0.5)/x
    # 1,1.2,1.4,1.6,1.8,2
    # 0,0.221,0.479,0.784,1.123,1.521
    s = "sin(x)+ln(y)*cos(x*2)+z+r"
    s = process_equation(s)

    print(s)
    func = convert_to_function(s)
    print(func)

    x_values = [0, 0.5, 1, 1.5]
    y_values = [2, 2.636, 3.595, 4.968]
    z_values = [1, 3, 5, 6]

    n = 10

    predictor(func, x_values, y_values, z_values, n)
    # firstly That you have to input the string. Which is then taken Through the function to be Equated to a math function.
    # Then you input two arrays The first array is the X or time values And the second array is the Y values Then you have to calculate. The. The step. Of your x/time
    # Then step between the x values or time values.
    # When you calculate all this, you call function called predictor. Which is made. Use a firstly send. Function which had been converted to math eqution.
    # Secondly, the acts or tea time array then y array, Then first value which should be taken into account in calculating the interpolating method.
    # Then the step. Then number of intervals, which is constantly four in our case.



else:
    # Code to execute if tv is not equal to any of the specified values
    print("Invalid option")