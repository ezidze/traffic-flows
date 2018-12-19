import numpy as np
import matplotlib.pyplot as plt
import math

#values

b1 = 50.0
b2 = 75.0
a = 60.0
eta = 1.0
gamma = 2.0
T0 = 70.0

pmin = 1.0 #minimum  money per minute
pmax = 10.0 #maximum money per minute

def T(x):

    global T0

    return T0 + gamma * x ** 4

def P(x,c): #function of money per minute

    return ( a + c - b1 ) / ( b2 - ( T0 + gamma * x ** 4 ) )

def X(p): #funtion of share of people

    global eta

    return p ** ( -eta )

def balance_search(c): #function of search balance

    global X,P

    y = [0.0, ]

    z = [ P( y[-1], c ), ]

    while np.abs( X( z[-1] ) - y[-1] ) >= 10 ** -3:

        y.append( X( z[-1] ) )

        z.append( P( y[-1], c ) )

    return y

def budget( x ): #functional

    global a, b1, b2, pmax, pmin ,T

    return ( 1 - x ) * ( b1 + b2 * ( pmax ** 2 - pmin ** 2 ) / 2.0 )\
           + x * ( a + T( x ) * ( pmax ** 2 - pmin ** 2 ) / 2 )

def budget_without_parking_fee( x, c ): #functional without parking fee

    global budget

    return budget( x ) - c * x






