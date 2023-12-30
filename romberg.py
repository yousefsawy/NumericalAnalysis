import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

##############################################################################

#Output functions


def plot_array(input_array, title_str):
  plt.plot(input_array)
  plt.scatter(range(len(input_array)), input_array, color='red')
  plt.title(title_str)
  plt.show()


def plot_math_function(func, start, end, step):

  x_vals = np.arange(start, end, step)
  y_vals = func(x_vals)
  plt.plot(x_vals, y_vals)
  plt.title('Plot')
  plt.show()


def True_Error(exact, result):
  Error = (exact - result) * 100 / exact
  return "True error = " + str(round(Error,5)) + " %"


#def plot_math_function_str(func_str, start, end, step):
#
#  x = sp.symbols('x')
#  func = sp.sympify(func_str)
#  func = sp.lambdify(x, func, "numpy")
#
#  x_vals = np.arange(start, end, step)
#  y_vals = func(x_vals)
#
#  plt.plot(x_vals, y_vals)
#  plt.title(f'Plot of {func_str}')
#  plt.show()


def About_Section():
  str = '        4\u207FI\u2090 - I\u2097\u2091\u209B\u209B \n' + 'I\u1D63\u2092\u2098 = ______________ \n' + '            4\u207F\u207B\u00b9 \n\n' + '                \u1D62\u208C\u2099\u208B\u2081 \n' + 'I\u209C\u1D63\u2090\u209A = \u00BD h(f(a)+2\u2140f(x\u1D62)+f(b))\n' + '                \u2071\u207C\u00B9  '

  return str


###############################################################################

###############################################################################


#trapaziodal interpolation recieving function as input
def trap_function(a, b, h, function):
  I = function(a) + function(b)
  x = h + a
  while x <= (b - a - h+1):
    I += 2 * function(x)
    x += h
  I = I * (h / 2)
  return I


#Romberg exterpolation recieving function as input


def Romberg_function(a ,b, Order_of_Error, function):
  i = 0
  n = 1
  loop = int(Order_of_Error / 2)
  hprev = b - a
  I = [0.0] * (loop)

  for i in range(loop):
    I[i] = trap_function(a, b, hprev, function)
    hprev = hprev / 2

  i = 0

  for n in range(loop - 1):
    for i in range(loop - (n + 1)):
      I[i] = (pow(4, n + 1) * I[i + 1] - I[i]) / (pow(4, n + 1) - 1)

  return I[0]


###############################################################################

###############################################################################


#trapaziodal interpolation recieving table as input
def trap_table(a, b, h, table):
  I = table[a] + table[b]
  x = h + a
  while x <= (b - a - h+1):
    I += 2 * table[x]
    x += h
  I = I * (h / 2)
  return I


#Uses Same trapaziodal interpolation as Romberg table


#Romberg exterpolation recieving function and table as input
def Romberg_func_table(table: dict, function, Order_of_Error: int = -1):
  i = 0
  n = 1
  a = list(table.keys())[0]
  b = list(table.keys())[-1]
  hprev = b - a

  func = dict()

  for x, y in table.items():
    func[x] = function(x, y)

  if (Order_of_Error != -1):
    if (int(len(table) / 2) >= int(Order_of_Error / 2)):
      loop = int(Order_of_Error / 2)
    else:
      loop = int(len(table) / 2)
  else:
    loop = int(len(table) / 2)

  I = [0.0] * (loop)

  for i in range(loop):
    I[i] = trap_table(a, b, hprev, func)
    hprev = hprev / 2

  i = 0

  for n in range(loop - 1):
    for i in range(loop - (n + 1)):
      I[i] = (pow(4, n + 1) * I[i + 1] - I[i]) / (pow(4, n + 1) - 1)

  return I[0]


###############################################################################

###############################################################################

#Input prameters function
a = 1
b = 9
Order_of_Error = 10
#Input function
x = sp.symbols('x')
fn = sp.sympify("sin(x)")
exact = sp.integrate(fn, (x,a,b))
exact_1 = float(exact)
print("Exact = "+ str(exact_1))
fn = sp.lambdify(x, fn, "numpy")
#Output

result = Romberg_function(a, b, Order_of_Error, fn)
print("Result = " + str(result))
print(True_Error(exact_1, result))
print("\n\n")

#plot_math_function(fn, a, b, 0.1)

###############################################################################

###############################################################################
#Input prameters table
test = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}

#Input function
x = sp.symbols('x y')
func = sp.sympify("sin(x)")
func = sp.lambdify(x, func, "numpy")


print("Exact = "+ str(exact_1))
#Output
result = Romberg_func_table(test, func)
print("Result = " + str(result))
print(True_Error(float(exact_1), result))

print("\n\n")


###############################################################################



about = About_Section()
print(about)
