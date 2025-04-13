import random
import math

def estimate_pi(num_samples):
    points_inside_circle = 0

    for _ in range(num_samples):
        # Generate a random point (x, y) in the square [-1, 1] x [-1, 1]
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        # Check if the point falls inside the circle (x^2 + y^2 <= 1)
        if x**2 + y**2 <= 1:
            points_inside_circle += 1

    # The ratio of points inside the circle to the total number of points approximates (pi/4)
    pi_estimate = 4 * points_inside_circle / num_samples
    return pi_estimate

# Run the simulation with a large number of samples
num_samples = 1000000
pi_estimated = estimate_pi(num_samples)
print(f"Estimated π after {num_samples} samples: {pi_estimated}")
