import sympy as sp
from sympy import sympify
from sympy.plotting import plot_implicit

#*************************************************************#
#****************FUNC****************#
def NonLinearNewton (func1, func2, start_x, start_y, num_of_iterations = 20, stop_error = 0):
    func1 = func1.replace('power', 'pow')
    func2 = func2.replace('power', 'pow')
    func1 = func1.replace('exponential', 'exp')
    func2 = func2.replace('exponential', 'exp')
    func1 = func1.replace('log(x)', 'log(x)/log(10)')
    func1 = func1.replace('log(y)', 'log(y)/log(10)')
    func2 = func2.replace('log(x)', 'log(x)/log(10)')
    func2 = func2.replace('log(y)', 'log(y)/log(10)')
    x = sp.symbols('x')
    y = sp.symbols('y')
    h = sp.symbols('h')
    k = sp.symbols('k')
    x_iterations = start_x
    y_iterations = start_y
    error_x = 0
    error_y = 0
    stopping_error = stop_error
#Turning strings into mathematical expressions
    expression1 = sympify(func1)
    expression2 = sympify(func2)
#Evaluating fx and fy
    f1x = sp.diff(expression1,x)
    f_1_y = sp.diff(expression1,y)
    f_2_x = sp.diff(expression2,x)
    f_2_y = sp.diff(expression2,y)
    #print (f1x.subs({x:start_x, y:start_y}))
    for i in range(0, num_of_iterations):
      A0 = sp.N(f1x.subs({x:x_iterations, y:y_iterations})) 
      A1 = sp.N(f_1_y.subs({x:x_iterations, y:y_iterations})) 
      A2 = sp.N(f_2_x.subs({x:x_iterations, y:y_iterations})) 
      A3 = sp.N(f_2_y.subs({x:x_iterations, y:y_iterations})) 
      
      f1_neg = -sp.N(expression1.subs({x:x_iterations, y:y_iterations})) 
      f2_neg = -sp.N(expression2.subs({x:x_iterations, y:y_iterations}))
      
      eq1 = sp.Eq(A0*h + A1*k ,f1_neg)
      eq2 = sp.Eq(A2*h + A3*k ,f2_neg)
      solution =sp.solve((eq1,eq2), (h,k))
      h_it = solution[h]
      k_it = solution[k]
      #Update the value of x, y and check error
      prev_x = x_iterations
      prev_y = y_iterations
      x_iterations = prev_x + h_it
      y_iterations = prev_y + k_it
      error_x = (x_iterations - prev_x)
      error_y = (y_iterations - prev_y)

      if abs(error_x) <= stopping_error or abs(error_y) <= stopping_error:
          break
          
    error_x = abs ((error_x/x_iterations)*100)
    error_y = abs ((error_y/y_iterations)*100)       
    # print (f"The solution is x = {x_iterations}, y = {y_iterations}") 
    # print (f"The error in calculating x = {error_x} %  ,The error in calculating y = {error_y} %") 
    p1 = plot_implicit(expression1, show=False, line_color='blue', legend=True, x_value = x, y_value = y)
    p2 = plot_implicit(expression2, show=False, line_color='red', legend=True, x_value = x, y_value = y)
    p1.extend(p2)
    p1.show() 

    return x_iterations, y_iterations, error_x, error_y

#Example from assignment 5 
# NonLinearNewton ("x+3*log(x)-power(y,2)", "2*power(x,2)-x*y-5*x+1", 3.4, 2.2, num_of_iterations = 2)


    