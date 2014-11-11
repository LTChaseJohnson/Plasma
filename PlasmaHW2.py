from math import *
import numpy as np
import matplotlib.pyplot as plt

e = 1.602E-19
epsilon0 = 8.854E-12
Ei = 2.323E-18
me = 9.109E-31
N = 1500
h = 6.626e-34

sigma0 = ((pi*e**2)/(4*pi*epsilon0*Ei))**2

Te = np.linspace(1,100,N)
Tj = Te/6.24e18
k = sigma0*np.sqrt((8*Tj)/(pi*me))*(1+(2*Tj)/Ei)*np.exp(-Ei/Tj)
sigma = pi*(e**2/(4*pi*epsilon0))**2*(1/Tj)*((1/Ei)-(1/Tj))
plt.figure(1)
plt.plot(Te,k)
'''plt.title('Ionization Coefficient for Nitrogen')'''
plt.ylabel('$\\frac{m^3}{s}$')
plt.xlabel('$T_e$ $eV$')
plt.xlim(0,100)
'''plt.ylim(0,1.4e-13)'''
plt.figure(2)
plt.plot(Te,sigma)
'''plt.title('Ionization Cross Section for Nitrogen')'''
plt.xlabel('$T_e$ $eV$')
plt.ylabel('$\\sigma_i$ $m^2$')
plt.ylim(0.0,8e-21)

Te2=np.linspace(1,165,N)
gamma1 = (2*pi*me*Te2)**(3/2)
gamma2 = np.exp(-24.6/Te2)
gamma = gamma1*gamma2
print gamma
neplus = (-2.*gamma+np.sqrt(4*gamma**2+4.*0.1*gamma/Te2))/2.
neminus = (-2.*gamma-np.sqrt(4*gamma**2+4.*gamma*.1/Te2))/2.
plt.figure(3)
plt.xlabel('$T_e$ $eV$')
plt.ylabel('n_e')
plt.plot(Te2,neplus)

AHe = 2.8
AAir = 14.6
AAr = 13.6
BHe = 34.
BAir = 365.
BAr = 235.
gammase = 0.12

pd = np.logspace(-1,3,10000)

V_bHe = (BHe*pd)/(np.log(AHe*pd)-np.log(np.log(1+gammase**(-1))))
V_bAir = (BAir*pd)/(np.log(AAir*pd)-np.log(np.log(1+gammase**(-1))))
V_bAr = (BAr*pd)/(np.log(AAr*pd)-np.log(np.log(1+gammase**(-1))))

plt.figure(4)
plt.loglog(pd,V_bHe,label='Helium')
plt.loglog(pd,V_bAir,label='Air')
plt.loglog(pd,V_bAr,label='Argon')
plt.xlabel('$pd$ (mm-Torr)')
plt.ylabel('$V_BD$ (V)')
plt.legend(loc='best')
plt.show()