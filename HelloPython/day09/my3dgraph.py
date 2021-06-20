from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
 
 # Open the drawing window 1, draw in 3D space
fig = plt.figure(1)
ax = fig.gca(projection='3d')
 
 # Give points (0, 0, 0) and (100, 200, 300)
y = range(3)

x = np.zeros(3)
z = [0, 20, 10]

zs = []
zs.append([0, 50, 0])
zs.append([0, 50, 0])
x1 = np.zeros(3)
z1 = [0, 20, 10]

 # Connect the first two points in the array
figure = ax.plot(x, y, zs[0], c='b')
figure1 = ax.plot(x+1, y, zs[1], c='r')

#plt.show() 

for i in range(3):
    y1 = range(3)
    x1 = np.zeros(3)
    z1 = [0, 20, 0]
    figure = ax.plot(x1+1, y1, z1, c='b')
plt.show()

