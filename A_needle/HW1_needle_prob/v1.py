import numpy as np

#v1 Pseudo-Random - using library
def buffon_needle(num_trial, needle_length, line_distance):
    # Random Generate needle
    y_center = np.random.uniform(0, line_distance, num_trial)
    theta = np.random.uniform(0, np.pi, num_trial)
#문제점: π 추정을 위해 라이브러리 π를 사용
    y_up = y_center + (needle_length/2) * np.sin(theta)
    y_down = y_center - (needle_length/2) * np.sin(theta)

    # count cross num
    count = np.sum((y_down < 0) | (y_up > line_distance))

    # estimate π
    pi_estimate = (2 * needle_length * num_trial) / (count*line_distance)

    return pi_estimate

# parameter setting
# * needle_length < line_distance
num_trial = 1000000
needle_length = 1.0
line_distance = 2.0

# run program
pi_estimated = buffon_needle(num_trial, needle_length, line_distance)

print(f"estimated value: {pi_estimated}")
print(f"built-in constant: {np.pi}")


