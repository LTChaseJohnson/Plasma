from pylab import *
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Constants for problem
q = input ('Enter particle charge: ')
m = input ('Enter particle mass: ')
dt = input ('Enter time step size: ')
N = 100
t = np.linspace(0,dt*N,N)

# Establishes position and velocity arrays depending on
# desired time steps and final time
r = zeros((N,3))
v = zeros((N,3))

# Establishes initial conditions in first index
r[0] = [0.0, 0.0, 0.0]
v[0] = [10**5, 10**5, 10**5]

# Constant B and E Fields
B = array([0.0, 0.0, 0.1])
E = array([1000.0,0.0,0.0])

# Calculates the acceleration from Newton's Law
# Uses step approximation to calculate future position
for i in range(N-1):
    a   = q/m*E + q/m* cross(v[i],B) 
    v[i+1] = v[i] + a*dt
    r[i+1] = r[i] + v[i+1]*dt

# Plots
figure(figsize=(8,6))
plot(t, r[:,0], label="x-direction")
plot(t, r[:,1], label="y-direction")
plot(t, r[:,2], label="z-direction")
xlabel("Time",fontsize=26)
ylabel("Position",fontsize=26)
legend()

figure(figsize=(8,6))
plot(t, v[:,0], label=r"$v_x$")
plot(t, v[:,1], label=r"$v_y$")
plot(t, v[:,2], label=r"$v_z$")
xlabel("Time",fontsize=26)
ylabel("Velocities",fontsize=26)
legend()

# Creates 3-D position plot
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(r[:,0], r[:,1], r[:,2])

plt.show()