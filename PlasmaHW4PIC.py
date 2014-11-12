import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Constants for problem
q = input ('Enter particle charge: ')
m = input ('Enter particle mass: ')
dt = input ('Enter time step size: ')
N = 100
Np = input ('Enter number of particles: ')
t = np.linspace(0,dt*N,N)

# Establishes position and velocity arrays depending on
# desired time steps and final time
r = np.zeros((N,3,Np))
v = np.zeros((N,3,Np))

# Establishes initial conditions in first index
# Having (np.random.random()-np.random.random())
# removes positive bias in initial velocities
for n in range(Np):
    r[0,:,n] = [0.0, 0.0, 0.0]
    v[0,:,n] = [10**3*(np.random.random()-np.random.random()
), 10**3*(np.random.random()-np.random.random()
), 10**3*(np.random.random()-np.random.random()
)]

# Constant B and E Fields
B = np.array([0.0, 0.0, 0.1])
E = np.array([1000.0,0.0,0.0])

# Calculates the acceleration from Newton's Law
# Uses step approximation to calculate future position
for i in range(N-1):
    for n in range(Np):
        a   = q/m*E + q/m* np.cross(v[i,:,n],B)
        v[i+1,:,n] = v[i,:,n] + a*dt
        r[i+1,:,n] = r[i,:,n] + v[i+1,:,n]*dt

# Plots
plt.figure(figsize=(8,6))
plt.plot(t, r[:,0,0], label="x-direction")
plt.plot(t, r[:,1,0], label="y-direction")
plt.plot(t, r[:,2,0], label="z-direction")
plt.xlabel("Time",fontsize=26)
plt.ylabel("Position",fontsize=26)
plt.legend()

plt.figure(figsize=(8,6))
plt.plot(t, v[:,0,0], label=r"$v_x$")
plt.plot(t, v[:,1,0], label=r"$v_y$")
plt.plot(t, v[:,2,0], label=r"$v_z$")
plt.xlabel("Time",fontsize=26)
plt.ylabel("Velocities",fontsize=26)
plt.legend()

# Creates 3-D position plot
for n in range(Np):
    fig = plt.figure(3)
    ax = fig.gca(projection='3d')
    ax.plot(r[:,0,n], r[:,1,n], r[:,2,n])

plt.show()