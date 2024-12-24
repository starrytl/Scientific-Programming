import numpy as np
import math

# v1-1 taylor sine
# taylor_sin, 라이브러리에 저장된 sine 대신 taylor 급수를 통해 구한 sine 사용
def taylor_sin(x,num_trial_taylor=20):
  sin_taylor=0.0
  for n in range(num_trial_taylor):
    sign=(-1)**n
    term=(x**(2*n+1))/math.factorial(2*n+1)
    sin_taylor +=sign*term
  return sin_taylor
vectorized_taylor_sin = np.vectorize(taylor_sin)
# 참고: 파이썬 numpy 라이브러리에 저장된 sin은 테일러급수를 통해 추정한 sin값을 벡터화 해 저장되어있으므로 굳이 할 필요는 없다.


def buffon_needle(num_trial, needle_length, line_distance):
    # Random Generate needle
    y_center = np.random.uniform(0, line_distance, num_trial)
    theta = np.random.uniform(0, np.pi, num_trial)

    y_up = y_center + (needle_length/2) *vectorized_taylor_sin(theta)
    y_down = y_center - (needle_length/2) *vectorized_taylor_sin(theta)
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
