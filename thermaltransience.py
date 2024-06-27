from CoolProp.CoolProp import PropsSI
import matplotlib.pyplot as plt
import math

#transience with an aluminum block and an unlimited heat source being applied
thickness = 0.1 #m
area = 1 #m^2
al_thermal_conductivity = 200
input_temperature = 140
al_init_temp = 300
al_density = 2700
al_specific_heat = 900 #J/kg/K
temp_array = []
time = 0
time_array = []
heater = 90000 #W

#while time < 1000:

    #q = kA * (dT/dx)
    #heat_transfer_rate = (((area * al_thermal_conductivity)  * (input_temperature - al_init_temp)) / thickness) + heater

    #q = m*c*deltaT
    #mass = thickness * area * al_density #density * volume
    #delta_T = heat_transfer_rate / (mass * al_specific_heat) #per second

    #temp_array.append(al_init_temp)
    #time_array.append(time)
    #al_init_temp = al_init_temp + delta_T
    #time+=1

#plt.plot(time_array, temp_array)
#plt.title("Temperature vs Time heater vacuum")
#plt.xlabel("Time")
#plt.ylabel("Temperature")
#plt.show()

thickness = 0.1 #m
area = 1 #m^2
al_thermal_conductivity = 200
input_temperature = 140
al_init_temp = 300
al_density = 2700
al_specific_heat = 900 #J/kg/K
temp_array = []
time = 0
time_array = []
heater = 90000 #W
time = 600

T = input_temperature + ((al_init_temp - input_temperature)*
                         (math.e ** (-time * ((al_thermal_conductivity*area)/(al_density*thickness*area*thickness*al_specific_heat)))))
print(T)