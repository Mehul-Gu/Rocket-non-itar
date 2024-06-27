from units import in2m
from CoolProp.CoolProp import PropsSI
from scipy.optimize import fsolve
import math

mdot = 0.1 #kg/s
D = in2m(0.216) #m
A = math.pi * ((D/2)**2) #m^2
gamma = 1.66 
c = PropsSI('A','T',288,'P',6.895e+6,'Helium') #m/s
Cd = 0.6
density = PropsSI('D','T',288,'P',6.895e+6,'Helium')

fun = lambda velocity: mdot - ((velocity * A) * Cd * density * ((1 + (((gamma - 1) / 2) * (velocity / c))) ** ((-1)/(gamma - 1))))
velocity_solution = fsolve(fun, 0)[0]
print("Barely choked velocity of Helium is " + str(velocity_solution))

mdot = 0.1 #kg/s
D = in2m(0.136) #m
A = math.pi * ((D/2)**2) #m^2
gamma = 1.4
c = 354.4 #m/s
Cd = 0.6
density = PropsSI('D','T',288,'P',6.895e+6,'Nitrogen')
c = PropsSI('A','T',288,'P',6.895e+6,'Nitrogen') #m/s
fun = lambda velocity: mdot - ((velocity * A) * Cd * density * ((1 + (((gamma - 1) / 2) * (velocity / c))) ** ((-1)/(gamma - 1))))
velocity_solution = fsolve(fun, 0)[0]
print("Barely choked velocity of Nitrogen is " + str(velocity_solution))
