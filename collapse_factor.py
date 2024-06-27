import math

To = 540 #pressurant inlet temp, R - 300K
r = 0.61843832 #maximum radius of tank, ft - 0.19m
Vi = 0.317832 #initial ullage volume, ft^3 - 0.009m^3
cpw = 0.214961307 #al wall specific heat Btu/lbR - 900J/kgK
rho_w = 168.5555 #al wall density, lb/ft^3 - 2700kg/m^3
d_w = 0.00675 #al wall thickness, ft - 0.081in
p = 106560 #ullage pressure, lb/ft^2 - 740psi
time = 60 #seconds
h_a = 0.00582 #ambient heat transfer coefficient, BTU/sft^2R - forced_convec_htc_cylin(101325, 200, 300, 50, 0.381, 'AIR') - 119j/sm^2K
T_a = 540 #ambient temperature, R - 300K
A_d = 0.001736 #pressurant gas distributor area, ft^2 - 0.25in^2
V_l = 0.11770378418 #LOX volumetric flowrate, mdot/density, ft^3/s - 4/1200 m^3/s
V = 8.793352 #propellant tank volume, ft^3 - 0.249m^3
Mw = 4 #mollecular weight of pressurant
alpha = 1 #gass compressibility. At 740psi helium doesnt have factor
R = 1545.4 #gas constant english units
exponential_1_term = 0.0000681 * ((To - 164) ** (-0.165)) * \
                    (r ** (-0.895)) * \
                    (h_a ** 0.765) * \
                    (T_a - 164)
exponential_2_term = (-5.04) * ((To - 164) ** (-0.443)) * \
                    (r ** (-2.604)) * \
                    (V_l / A_d)
Tm = 164 + ((To - 164) * (
    3.1 *
    ((To - 164) ** (-0.304)) *
    (r ** 0.1395) *
    (Vi ** 0.01416) *
    ((cpw * rho_w * d_w) ** (-0.078)) *
    (p ** 0.0762) *
    (time ** (-0.1146)) *
    (math.e ** exponential_1_term) *
    (math.e ** exponential_2_term)
))
Wt = (p * V * Mw) / (alpha * R * Tm)
print(Wt/60)