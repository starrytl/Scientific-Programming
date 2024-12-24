import numpy as np

#v2
#파이를 해결 = 사인을 좌표를 통해 계산
def buffon_needle(num_trial, needle_length, line_distance):
    # Random Generate needle
    y_center = np.random.uniform(0, line_distance, num_trial)
    
    sin_x = np.random.uniform(-1, 1, num_trial)
    sin_y = np.random.uniform(-1, 1, num_trial)
    
    sin_xy = sin_y / np.sqrt(sin_x**2 + sin_y**2)

    #sin의 범위 0~파이가 아닌 전체범위임 따라서 v1의 0~파이 범위의 0.5배(/2)
    y_up = y_center + (needle_length / 2) * sin_xy
    y_down = y_center - (needle_length / 2) * sin_xy

    # count cross num
    count = np.sum((y_down < 0) | (y_up > line_distance))

    # estimate π
    pi_estimate = (2 * needle_length * num_trial) / (count * line_distance) / 2

    return pi_estimate
    
# parameter setting
# * needle_length < line_distance
num_trial = 10000000
needle_length = 1.0
line_distance = 2.0

# run program
pi_estimated = buffon_needle(num_trial, needle_length, line_distance)

print(f"estimated value: {pi_estimated}")
print(f"built-in constant: {np.pi}")


