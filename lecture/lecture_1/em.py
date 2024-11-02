# EM Problem 1-16
# Package
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

x_component = np.linspace(0, 1, 100)
y_component = np.linspace(0, 1, 100)
z_component = np.linspace(0, 1, 100)

def position_vector(x, y, z):
    position = np.array([x, y, z])
    position_magnitude = np.linalg.norm(position)
    return position / np.square(position_magnitude)

# Create a figure and a 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Generate the grid of points
X, Y, Z = np.meshgrid(x_component, y_component, z_component)

# Plot the surface
ax.plot_surface(X, Y, Z)

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Graph')

# Show the plot
plt.show()

