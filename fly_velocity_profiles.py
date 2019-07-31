#!/usr/bin/env python3

## Fly Casting Physics
## Copyright (C) 2019, Torsten Ht.
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
import numpy as np
import matplotlib.pyplot as plt

# Computes the fly velocity profiles for semicircular loops

## Following equations are taken from:
## C. Gatti-Bono and N. C. Perkins
## Comparison of numerical and analytical solutions for fly casting dynamics
## Sports Engineering - September 2003

# Loop diameters
Ds = [2.0, 1.5, 1.0955, 0.75, 0.05] # [m]

# Set this parameter true, if you want to use the values from Gatti-Bonos's paper
isReferenceParameters = True

if isReferenceParameters:
    # Diameter of the fly line
    d_l = 1.009e-3 # [m]

    # Initial fly line length
    l_0 = 4.8 # [m]

    # Density of the fly line
    rho_l = 1.158e3 # [kg]

    # Density of the air
    rho_a = 1.29 # [kg/m³]

    # Normal drag coefficient
    C_n = 1.0

    # Tangential drag coefficient
    C_t = 0.015

    # Mass of the fly
    m_f = 0.000075 # [kg]

    # Drag coefficient of the fly
    C_f = 1.0

    # Radius of the fly
    r_f = 0.0075 # [m]

    # Initial velocity
    v_0 = 15.0 # [m/s]
else:
    # Loop diameter
    D = 0.75 # [m]

    # Loop radius
    R = D / 2.0 # [m]

    # Diameter of the fly line
    d_l = 1.1e-3 # [m]

    # Initial fly line length
    l_0 = 4.46 # [m]

    # Density of the fly line
    rho_l = 0.850e3 # [kg]

    # Density of the air
    rho_a = 1.2 # [kg/m³]

    # Normal drag coefficient
    C_n = 1.0

    # Tangential drag coefficient
    C_t = 0.005

    # Mass of the fly
    m_f = 0.000075 # [kg]

    # Drag coefficient of the fly
    C_f = 1.0

    # Radius of the fly
    r_f = 0.005 # [m]

    # Initial velocity
    v_0 = 17.7 # [m/s]

# Now compute the velocity histories
displacement_histories = []
velocity_histories = []
for D in Ds:
    # Loop radius
    R = D / 2.0 # [m]
    # Constants from above paper 
    alpha = rho_l * math.pi * (d_l ** 2.0) / 4.0
    beta = math.pi * R / 2.0 + 4.0 * m_f / (rho_l * math.pi * (d_l ** 2.0))
    lambd = (4.0 * rho_a * C_t) / ( rho_l * d_l )
    # NOTE: mu seems to have a typo in above paper: C_t is missing in the 5.0 * (math.pi**2) / 32.0 term
    mu = 2.0 * (d_l * R * (5.0 * (math.pi**2) / 32.0 * C_t +  (1.0/12.0) * C_n) + (1.0/2.0) * C_f * math.pi * (r_f ** 2)) / ( C_t * d_l * math.pi)

    print("Loop (diameter, radius) = ( %2.2f m, %2.2f m )" % (D, R) )
    print("--")
    print("alpha = ", alpha)
    print("beta = ", beta)
    print("lambd = ", lambd)
    print("mu = ", mu)
    print("--")
    displacement_history = []
    velocity_history = []
    for l in np.arange(l_0, 0.0, -0.05):
        # Computing the velocity as a function of the length of the traveling line l(t)
        # NOTE: the (l_0 + beta) / (l - beta) term is wrong in the above paper
        x = 2.0 * (l_0 - l) # According eq.12
        v = v_0 * math.exp(lambd * (l - l_0)) * (((l_0 + beta) / (l + beta)) ** ((1.0/2.0) + lambd * (beta - mu)))

        if abs(x - round(x)) < 0.01:
            print("Fly velocity at fly displacement %2.2f m = %2.2f m/s" % (x, v)) 

        # Add to data series
        displacement_history.append(x)
        velocity_history.append(v)
    
    displacement_histories.append(displacement_history)
    velocity_histories.append(velocity_history)
    print("--")
    print()

i = 0
plt.figure(1, figsize=(10,10))
ylims = [(12.0, 15.0), (13.5, 15.0), (14.0, 15.5), (14.0, 17.0), (10, 30)]
for sp in [321, 322, 323, 324, 325]:
    plt.subplot(sp)
    plt.plot(displacement_histories[i], velocity_histories[i])
    plt.xlim((0, 8))
    plt.ylim(ylims[i])
    plt.grid(True)
    plt.xlabel("Fly Displacement [m]")
    plt.ylabel("Fly Velocity [m/s]")
    i += 1
plt.savefig("velocity_histories.png", dpi=300)
