#!/usr/bin/env python3

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import os

# Parameters
epsilon = 0.01
max_steps = 1000
num_directions = 100

# Function to define the boundary: cardioid
def boundary_function(point):
    x, y = point
    r = np.sqrt(x ** 2 + y ** 2)
    theta = np.arctan2(y, x)
    cardioid_radius = 0.5 * (1 + np.cos(theta))
    return cardioid_radius - r

# Function to determine the largest possible circle radius within the boundary
def largest_possible_radius(point):
    theta_values = np.linspace(0, 2 * np.pi, num_directions, endpoint=False)
    max_radius = float('inf')
    for theta in theta_values:
        direction = np.array([np.cos(theta), np.sin(theta)])
        radius = 0
        step_size = 0.01
        steps = 0
        while boundary_function(point + radius * direction) > 0:
            radius += step_size
            steps += 1
            if steps > 10000:  # Prevent infinite loop
                break
        max_radius = min(max_radius, radius)
    return max(max_radius - epsilon, 0)

# Function to perform a single Walk on Spheres
def walk_on_spheres(starting_point):
    path = [starting_point]
    current_point = starting_point
    radii = []
    steps = 0

    while boundary_function(current_point) > epsilon and steps < max_steps:
        # Determine the radius of the largest possible circle within the boundary
        max_radius = largest_possible_radius(current_point)
        radius = np.random.uniform(0, max_radius)
        radii.append(radius)

        # Choose a random angle to move to a new point on the circle
        theta = np.random.uniform(0, 2 * np.pi)
        new_point = current_point + radius * np.array([np.cos(theta), np.sin(theta)])

        # Append the new point to the path
        path.append(new_point)
        current_point = new_point
        steps += 1

    return path, radii

# Visualization function for all steps at once
def visualize_entire_walk(path, radii):
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)

    # Plot the boundary (cardioid)
    theta = np.linspace(0, 2 * np.pi, 1000)
    x_boundary = 0.5 * (1 + np.cos(theta)) * np.cos(theta)
    y_boundary = 0.5 * (1 + np.cos(theta)) * np.sin(theta)
    ax.plot(x_boundary, y_boundary, color='b', linestyle='--', label='Boundary')

    # Extract x and y coordinates from the path
    x_coords, y_coords = zip(*path)

    # Plot the entire walk
    ax.plot(x_coords, y_coords, marker='o', color='r', linestyle='-', linewidth=1, markersize=3)

    # Highlight starting and ending points
    ax.plot(x_coords[0], y_coords[0], marker='o', color='g', markersize=6, label='Start')
    ax.plot(x_coords[-1], y_coords[-1], marker='x', color='k', markersize=6, label='End')

    # Plot all circles at each step
    for i, (x, y) in enumerate(path):
        if i < len(radii):
            current_circle = plt.Circle((x, y), radii[i], color='orange', fill=False, linestyle=':')
            ax.add_artist(current_circle)

    plt.legend()
    plt.title('Walk on Spheres - Entire Path with Circles')

    # Save the plot to the same directory as the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, "wos.png")
    print(f"Saving visualization as '{output_path}'...")
    plt.savefig(output_path)
    print("Saved successfully.")

# Main function to perform and visualize the walk
if __name__ == "__main__":
    # Initial starting point (random point inside the boundary)
    for _ in range(1000):  # Maximum 1000 attempts
        starting_point = np.random.uniform(-1.0, 1.0, 2)
        if boundary_function(starting_point) > 0:
            break
    else:
        raise ValueError("Failed to find a valid starting point within the boundary.")

    # Perform the walk
    path, radii = walk_on_spheres(starting_point)

    # Visualize the entire walk with all steps
    visualize_entire_walk(path, radii)
