from pylab import *
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

q = 1.602E-19
m = 9.109E-27
dt = 1E-7
N = 100
t = np.linspace(0,dt*N,N)

r = zeros((N,3))
v = zeros((N,3))

r[0] = [0.0, 0.0, 0.0]
v[0] = [10**5, 10**5, 10**5]

B = array([0.0, 0.0, 0.1])
E = array([1000.0,0.0,0.0])

for i in range(N-1):
    a   = q/m*E + q/m* cross(v[i],B) 
    v[i+1] = v[i] + a*dt
    r[i+1] = r[i] + v[i+1]*dt

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

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(r[:,0], r[:,1], r[:,2])
plt.show()