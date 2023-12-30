"""
    About:
        Given f(x, y) = 0, g(x, y) = 0
        Separate x from f(x, y) and y from g(x, y)
        -> Xi+1 = F(Xi, Yi)
        -> Yi+1 = G(Xi+1, Yi)
        Convergence conditions:
        -> | Fx | + | Fy | < 1 @ initial values
        and
        -> | Gx | + | Gy | < 1 @ initial values
        If the check fails we re-perform separation but with switching the functions f and g

    Stopping Criteria:
        -> Number of iterations
        -> | Xi+1 - Xi | <= Es and | Yi+1 - Yi | <= Es
"""
from sympy import symbols, sympify, Eq, solve, diff
from sympy.functions.elementary import *
from sympy.plotting import plot3d, plot

def fixed_point_2var(user_equation1, user_equation2, start_x = 0, start_y = 0, iterations = 100,stopping_error = 0, use_iter = True):
    """
    Interprets given user input and uses the fixed point method to find the solution for x and y.
    Either a certain number of iterations is defined or a stopping error is given. Even when a 
    stopping error is specified it is limited to 100 iterations as the solution may never converge.
    This function uses 4 significant digits.

    Parameters:
    - user_equation1: The first equation in the form: f(x, y) = 0.
    - user_equation2: The second equation in the form: g(x, y) = 0.
    - start_x: Starting value for x (defaults to zero).
    - start_y: Starting value for y (defaults to zero).
    - iterations: Number of iterations for the method (defaults to 100).
    - stopping_error: Stopping error value (defaults to zero).
    - use_iter: Choose whether to use iterations (True) or stopping error (False) 
                (defaults to 1 [iterations]).

    Returns:
    - Solution for x, y, Relative approximate error for x, Relative approximate error for y.
        , Convergence check for 1st eqn, , Convergence check for 2nd eqn

    """
    try:
        # Define symbolic variables
        x, y, z, l = symbols('x y z l')

        # Modify the equations to emulate the isolation of variables
        # Replace one occurence of the variable with another name (ex: z) and then after
        # substituting the values of x and y, solve for the new variable to get
        # an expression that has achived isolation of variables.

        if 'x' in user_equation1 and 'y' in user_equation2:
            modified_input_1 = user_equation1.replace('x', 'z', 1)
            modified_input_2 = user_equation2.replace('y', 'l', 1)
        else:
            modified_input_1 = user_equation2.replace('x', 'z', 1)
            modified_input_2 = user_equation1.replace('y', 'l', 1)

        # Convert user input to symbolic expressions
        eqn1_sym = sympify(modified_input_1)
        eqn2_sym = sympify(modified_input_2)

        # Isolate the variables
        eqn1_iso = solve(eqn1_sym, z)[0]
        eqn2_iso = solve(eqn2_sym, l)[0]

        # Check for convergence
        conv_Fx_sym = sympify("0")
        conv_Fy_sym = sympify("0")
        conv_Gx_sym = sympify("0")
        conv_Gy_sym = sympify("0")

        # Get the symbolic expressions of the derivatives
        if x in list(eqn1_iso.free_symbols):
            conv_Fx_sym = diff(eqn1_iso, x)
        if y in list(eqn1_iso.free_symbols):
            conv_Fy_sym = diff(eqn1_iso, y)
        if x in list(eqn2_iso.free_symbols):
            conv_Gx_sym = diff(eqn2_iso, x)
        if y in list(eqn2_iso.free_symbols):
            conv_Gy_sym = diff(eqn2_iso, y)

        # Calculate derivative values at the initial point
        conv_Fx = abs(conv_Fx_sym.evalf(subs={x: start_x, y: start_y}))
        conv_Fy = abs(conv_Fy_sym.evalf(subs={x: start_x, y: start_y}))
        conv_Gx = abs(conv_Gx_sym.evalf(subs={x: start_x, y: start_y}))
        conv_Gy = abs(conv_Gy_sym.evalf(subs={x: start_x, y: start_y}))
        conv_F = round((conv_Fx + conv_Fy), 4)
        conv_G = round((conv_Gx + conv_Gy), 4)

        # Initialize variables
        x_val, y_val = start_x, start_y # Hold Zi_1, Li_1 respectively
        old_x, old_y = start_x, start_y # Hold Zi, Li respectively
        err_rel_x, err_rel_y = 0, 0     # Relative errors for x, y respectively
        # Perform iterations based on the chosen method
        if use_iter == True:
            for i in range(iterations):
                # Store the current values as old for fixed point
                # and error calculations
                old_x, old_y = x_val, y_val
                # Update x and y values using the fixed-point method
                x_val = eqn1_iso.evalf(subs={x: old_x, y: old_y})
                y_val = eqn2_iso.evalf(subs={x: x_val, y: old_y})
                x_val = round(float(x_val), 4)
                y_val = round(float(y_val), 4)
                # For Debugging: print(f"Iteration {i + 1} x, y: {x_val}, {y_val}")
        else:
            # In case the soln never converges, define max iterations
            iterations = 100
            # Initialize stopping errors as infinity for the first iteration
            stop_x, stop_y = float('inf'), float('inf')
            while max(stop_x, stop_y) > float(stopping_error) and iterations != 0:
                # Store the current values as old for fixed point
                # and error calculations
                old_x, old_y = x_val, y_val
                # Update x and y values using the fixed-point method
                x_val = eqn1_iso.evalf(subs={x: old_x, y: old_y})
                y_val = eqn2_iso.evalf(subs={x: x_val, y: old_y})
                x_val = round(float(x_val), 4)
                y_val = round(float(y_val), 4)
                # Update stopping error
                stop_x, stop_y = abs(x_val - old_x), abs(y_val - old_y)
                iterations -= 1
                # For Debugging: print(f"Iteration (tolerance) {100 - iterations} x, y: {x_val}, {y_val}")

        # Calculate relative errors, handle division by zero case
        if x_val != 0:
            err_rel_x = round(abs((x_val - old_x) * 100 / (x_val)), 4)
        if y_val != 0:
            err_rel_y = round(abs((y_val - old_y) * 100 / (y_val)), 4)

    except Exception as e:
        print(f"Error: {e}")

    return x_val, y_val, err_rel_x, err_rel_y, conv_F, conv_G

def fixed_point_1var(user_equation, start_x = 0, iterations = 100, stopping_error = 0, use_iter = True):
    """
    Interprets given user input and uses the fixed point method to find the solution for x.
    Either a certain number of iterations is defined or a stopping error is given. Even when a 
    stopping error is specified it is limited to 100 iterations as the solution may never converge.
    This function uses 4 significant digits.

    Parameters:
    - user_equation1: The first equation in the form: f(x) = 0.
    - start_x: Starting value for x (defaults to zero).
    - iterations: Number of iterations for the method (defaults to 100).
    - stopping_error: Stopping error value (defaults to zero).
    - use_iter: Choose whether to use iterations (True) or stopping error (False) 
                (defaults to 1 [iterations]).

    Returns:
    - Solution for x, Relative approximate error for x, Convergence check for 1st eqn

    """
    try:
        # Define symbolic variables
        x, z = symbols('x z')

        # Modify the equations to emulate the isolation of variables
        # Replace one occurence of the variable with another name (ex: z) and then after
        # substituting the values of x and y, solve for the new variable to get
        # an expression that has achived isolation of variables.

        modified_input = user_equation.replace('x', 'z', 1)

        # Convert user input to symbolic expressions
        eqn_sym = sympify(modified_input)

        # Isolate the variables
        eqn_iso = solve(eqn_sym, z)[0]

        # Check for convergence
        conv_Fx_sym = sympify("0")

        # Get the symbolic expressions of the derivatives
        if x in list(eqn_iso.free_symbols):
            conv_Fx_sym = diff(eqn_iso, x)

        # Calculate derivative values at the initial point
        conv_Fx = abs(conv_Fx_sym.evalf(subs={x: start_x}))
        conv_F = round((conv_Fx), 4)

        # Initialize variables
        x_val, old_x = start_x, start_x     # Hold Zi_1, Zi respectively
        err_rel_x = 0                       # Relative error for x

        # Perform iterations based on the chosen method
        if use_iter == True:
            for i in range(iterations):
                # Store the current values as old for fixed point
                # and error calculations
                old_x = x_val
                # Update x values using the fixed-point method
                x_val = eqn_iso.evalf(subs={x: old_x})
                x_val = round(float(x_val), 4)
                # For Debugging: print(f"Iteration {i + 1} x: {x_val}")
        else:
            # In case the soln never converges, define max iterations
            iterations = 100
            # Initialize stopping errors as infinity for the first iteration
            stop_x= float('inf')
            while stop_x > float(stopping_error) and iterations != 0:
                # Store the current values as old for fixed point
                # and error calculations
                old_x = x_val
                # Update x values using the fixed-point method
                x_val = eqn_iso.evalf(subs={x: old_x})
                x_val = round(float(x_val), 4)
                # Update stopping error
                stop_x = abs(x_val - old_x)
                iterations -= 1
                # For Debugging: print(f"Iteration (tolerance) {100 - iterations} x: {x_val}")

        # Calculate relative errors, handle division by zero case
        err_rel_x = 0
        if x_val != 0:
            err_rel_x = round(abs((x_val - old_x) * 100 / (x_val)), 4)

    except Exception as e:
        print(f"Error: {e}")

    return x_val, err_rel_x, conv_F

def fixed_point_main(user_equation1, user_equation2, start_x = 0, start_y = 0, iterations = 100,stopping_error = 0, use_iter = True, use_one_var = False):
    """
    Wrapper To call either the one-variable or two-variable fixed point functions

    Parameters:
    - All parameters of the two-variable fixed point function
    - use_one_var: True when one-variable method is needed, false otherwise (and false by default).

    Returns:
        The return value of the chosen fixed point function
    """
    output_func = []
    if use_one_var is True:
        output_func = fixed_point_1var(user_equation1, start_x, iterations, stopping_error, use_iter)
    else:
        output_func = fixed_point_2var(user_equation1,user_equation2, start_x, start_y,iterations, stopping_error, use_iter)
    return output_func

def plot_eqn(user_equation1, user_equation2, use_one_var = False):
    """
    Plots the Given Equations

    Parameters:
    - user_equation1 & user_equation2: Equations to be plotted
    - use_one_var: True when one-variable method is needed, false otherwise (and false by default).
    """

    x, y = symbols('x y')

    if use_one_var is True:
        # Convert both eqn into sympy expression
        f = sympify(user_equation1)
        plot(f, (x, -5, 5), title='Graph of f(x)', xlabel='x', ylabel='f(x)')
    else:
        # Convert both eqns into sympy expressions
        f1 = sympify(user_equation1)
        f2 = sympify(user_equation2)
        # Plot the first and second functions
        plot1 = plot3d(f1, (x, -0.5, 0.5), (y, -0.5, 0.5), title='Graph of f1(x,y) & f2(x,y)',
                        xlabel='x', ylabel='y', show = False)
        plot2 = plot3d(f2, (x, -0.5, 0.5), (y, -0.5, 0.5), title='Graph of f2(x,y)',
                        xlabel='x', ylabel='y', show = False)
        # Add the plot of the 2nd function to the first
        plot1.extend(plot2)
        plot1.show()


# #Input Examples:
#   #Example 1 (Two var):
# INPUT_1 = "5 * (x**2) - (y**2)"
# INPUT_2 = "y - 0.25 * sin(x) - 0.25 * cos(y)"
# START_X = 0.25
# START_Y = 0.25
# ITERATIONS = 5
# STOPPING_ERROR = 0
# USE_ITERATIONS = False
# USE_ONE_VARIABLE = False

#   Example 2 (Two var):
# INPUT_1 = "x * y  - cos(y) + 1"
# INPUT_2 = "(E ** y) + y ** 2 - 2"
# START_X = 1.9
# START_Y = 0.1
# ITERATIONS = 50
# STOPPING_ERROR = 0
# USE_ITERATIONS = True
# USE_ONE_VARIABLE = False

#   Example 3 (One var):
# INPUT_1 = "sin(x) + 2*x - 1"
# INPUT_2=0
# START_X = 0.3
# START_Y=0
# ITERATIONS = 10
# STOPPING_ERROR = 0
# USE_ITERATIONS = True
# USE_ONE_VARIABLE = True

# Note that the trigonometric functions take input in radians

# INPUT_1 = "5 * (x**2) - (y**2)"
# INPUT_2 = "y - 0.25 * sin(x) - 0.25 * cos(y)"
# START_X = 0.25
# START_Y = 0.25
# ITERATIONS = 5
# STOPPING_ERROR = 0
# USE_ITERATIONS = False
# USE_ONE_VARIABLE = False

# output = fixed_point_main(INPUT_1, INPUT_2, START_X, START_Y,ITERATIONS, STOPPING_ERROR, USE_ITERATIONS, USE_ONE_VARIABLE)
# print(f"Output 1: x = {output[0]}, y = {output[0]}, Eax = {output[1]}%, Eay = {output[1]}%")
# print(f"| Fx | + | Fy | = {output[2]}, | Gx | + | Gy | = {output[2]}")
#plot_eqn(INPUT_1, INPUT_2, USE_ONE_VARIABLE)

# INPUT_1 = "2*x + sin(x) - 1"
# INPUT_2=0
# START_X = 0.3
# START_Y=0
# ITERATIONS = 11
# STOPPING_ERROR = 0
# USE_ITERATIONS = True
# USE_ONE_VARIABLE = True

# output = fixed_point_main(INPUT_1, INPUT_2, START_X, START_Y, ITERATIONS, STOPPING_ERROR, USE_ITERATIONS, USE_ONE_VARIABLE)
# print(f"Output 2: x = {output[0]}, Eax = {output[1]}%, | Fx | = {output[2]}")
# plot_eqn(INPUT_1, INPUT_2, USE_ONE_VARIABLE)
