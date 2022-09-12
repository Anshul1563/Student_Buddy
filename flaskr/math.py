#DIFFENCIATION WITHOUT VALUES
from importlib.machinery import DEBUG_BYTECODE_SUFFIXES
from sympy import *
from scipy.integrate import odeint 
import sympy as smp
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
def model(y1,t):
    global y
    y = y1
    global dydt
    dydt1=eval(dydt)
    return dydt1

def Differentiation(expr):

    x, y = symbols('x y') 
    expr = eval(expr)
    expr_diff = Derivative(expr, x) 
    val = "{}".format(expr_diff.doit())
    return val

def Integration(expr):
    x, y = symbols('x y') 
    x2=eval(expr)
    x3=smp.integrate(x2,x)
    return x3

def deq(dydt):
  y = 0
  def model(y1,t):
      nonlocal y
      y = y1
      nonlocal dydt
      dydt1 = eval(dydt)
      return dydt1
  t=np.linspace(0,5)
  y0=0
  y=odeint(model,y0,t)

  plt.plot(t,y)
  plt.xlabel('time')
  plt.ylabel('y(t)')
  plt.show()


    
