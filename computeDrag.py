## Fly Casting Physics
## 
## Comparing the skin friction / form (pressure) drag during the acceleration phase 
## of the fly line.
##
## Copyright (C) 2022, Torsten Ht.
##
## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <http://www.gnu.org/licenses/>.

import math

# The fly line is simplifified as a cylinder. We assume that the line is straight while accelerating.
# Otherwise, a non straight line can be modelled with the line inclination parameter.

v = 40 # m/s, the line velocity
theta_deg = 3.0 # °, line inclination
theta_rad = theta_deg * math.pi / 180.0 # radians, line inclination

rho_line = 860 # kg/m³, fly line density 
m_line = 0.020 # kg, fly line mass

v_t = v * math.cos(theta_rad) # is the flow velocity tangential to the line
v_n = v * math.sin(theta_rad) # is the flow velocity normal to the line

rho_air = 1.204 # kg/m3, is the mass density of the fluid (air)
# see https://www.engineersedge.com/physics/viscosity_of_air_dynamic_and_kinematic_14483.htm
mu_air =  1.825e-6 # Pa.s, Dynamic Viscosity of Air @ 20°C
Cdn = 1.0 # Form drag coefficient
Cdt = 0.005 # Skin friction coefficient

def computeReferenceAreas():
    vol_line = m_line / rho_line
    A_line_cross = vol_line / l_line # Surface area of the line cross section
    d_line = math.sqrt(A_line_cross * 4.0 / math.pi)  # Line diameter
    A_skin = math.pi * d_line * l_line # Reference area for skin friction
    A_form = d_line * l_line # Reference area for form drag
    print("Line length = {l:.1f} m".format(l = l_line))
    print("Line diameter = {d_mm:.2f} mm".format(d_mm = d_line * 1000))
    print("Reference area (skin friction) = {A:.3f} m²".format(A=A_skin))
    print("Reference area (form drag) = {A:.3f} m²".format(A=A_form))
    
    # compute Reynolds Number
    # from https://en.wikipedia.org/wiki/Reynolds_number
    Re_n = rho_air * v * d_line / mu_air
    Re_t = rho_air * v * l_line / mu_air
    print("Reynolds Number Re (form drag) = {:.2e}".format(Re_n))
    print("Reynolds Number Re (skin friction) = {:.2e}".format(Re_t))

    return (A_skin, A_form)

def computeDrag():
    (A_skin, A_form) = computeReferenceAreas()
    Fdt = 0.5 * rho_air * (v_t ** 2) * Cdt * A_skin
    Fdn = 0.5 * rho_air * (v_n ** 2) * Cdn * A_form
    return (Fdt, Fdn)

def printConstants():
    print("Air density = {rho:.3f} kg/m³".format(rho=rho_air))
    print("Tangential velocity = {v:.2f} m/s".format(v=v_t))
    print("Normal velocity = {v:.2f} m/s".format(v=v_n))
    print("Skin friction coefficent = ", Cdt)
    print("Form drag coefficent = ", Cdn)
    print("Line inclination = {:.1f}°".format(theta_deg))
    print("--")

def printResults(Fdt, Fdn):
    print("Skin friction force Fdt = {F:.4f} N".format(F=Fdt))
    print("Form drag force Fdn = {F:.4f} N".format(F=Fdn))
    print("--")

printConstants()

# Case A
l_line = 10.0 # m, fly line length
(FdtA, FdnA) = computeDrag()
printResults(FdtA, FdnA)

# Case B
l_line = 20.0 # m, fly line length
(FdtB, FdnB) = computeDrag()
printResults(FdtB, FdnB)

# Print the difference
Fdiff = abs((FdtA + FdnA) - (FdtB + FdnB))

print("Force difference = {F:.4f} N".format(F=Fdiff))

