import numpy as np
import matplotlib.pyplot as plt

# Define boundary
def boundary_function(theta, a):
    x = a * (np.cos(theta))**3
    y = a * (np.sin(theta))**3
    return x, y

# Check in the closed curve
def is_inside_boundary(x, y, a):
    return (np.abs(x) / a)**(2/3) + (np.abs(y) / a)**(2/3) <= 1

# Calculate distance to the boundary
def distance_to_boundary(x, y, a):
    theta = np.arctan2(y, x)
    bx, by = boundary_function(theta, a)
    return np.sqrt((x - bx)**2 + (y - by)**2)

# Initial settings
epsilon = 0.7
a = 5.0
distance_threshold = 0.1

# Set starting point
while True:
    x, y = np.random.uniform(-a, a), np.random.uniform(-a, a)
    if is_inside_boundary(x, y, a) and distance_to_boundary(x, y, a) > epsilon:
        break

# Create a list to store the path
trajectory = [(x, y)]

# Implement
# np.random.seed(0)
max_iterations = 1000
iteration = 0

plt.figure(figsize=(8, 8))

while True:
    iteration += 1
    
    # Move in a random direction
    theta = np.random.uniform(0, 2 * np.pi)
    x_new = x + epsilon * np.cos(theta)
    y_new = y + epsilon * np.sin(theta)

    # Print current coordinates
    print(f"Iteration {iteration}: x = {x_new:.4f}, y = {y_new:.4f}")

    # Visualize circle for random movement
    circle_x = x + epsilon * np.cos(np.linspace(0, 2 * np.pi, 100))
    circle_y = y + epsilon * np.sin(np.linspace(0, 2 * np.pi, 100))
    plt.plot(circle_x, circle_y, 'c--', alpha=0.3)

    # Stop if close enough to the boundary
    if distance_to_boundary(x_new, y_new, a) < distance_threshold:
        x, y = x_new, y_new
        trajectory.append((x, y))
        break

    # Move if inside the boundary
    if is_inside_boundary(x_new, y_new, a):
        x, y = x_new, y_new
        trajectory.append((x, y))
    else:
        epsilon = max(epsilon / 1.5, 0.05)  # Reduce step size

# Visualize asteroid boundary
theta = np.linspace(0, 2 * np.pi, 500)
boundary_x, boundary_y = boundary_function(theta, a)

# Visualize boundary and fill the interior area
plt.plot(boundary_x, boundary_y, 'b', label='Asteroid Boundary')
plt.fill(boundary_x, boundary_y, color='lightblue', alpha=0.3)

# Visualize the path
trajectory = np.array(trajectory)
plt.plot(trajectory[:, 0], trajectory[:, 1], 'r-', label='Path')
plt.scatter(trajectory[0, 0], trajectory[0, 1], color='g', label='Start', s=100)
plt.scatter(trajectory[-1, 0], trajectory[-1, 1], color='k', label='End', s=100)

plt.axis('equal')
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Walk on Spheres - boundary : Asteroid')
plt.show()

