#!/usr/bin/env python3
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression



def buffon_needle(num_trial, needle_length, line_distance):
    y_center = np.random.uniform(0, line_distance, num_trial)

    sin_x = np.random.uniform(-1, 1, num_trial)
    sin_y = np.random.uniform(-1, 1, num_trial)

    sin_xy = sin_y / np.sqrt(sin_x**2 + sin_y**2)

    y_up = y_center + (needle_length / 2) * sin_xy
    y_down = y_center - (needle_length / 2) * sin_xy

    count = np.sum((y_down < 0) | (y_up > line_distance))

    pi_estimate = (2 * needle_length * num_trial) / (count * line_distance) / 2

    return pi_estimate

# num_trial 값에 대한 파이 추정값 계산
num_trials = np.linspace(1000, 10000000, 100).astype(int)
pi_estimates = np.array([buffon_needle(trials, 1.0, 2.0) for trials in num_trials])

X = num_trials.reshape(-1, 1)
y = pi_estimates

reg = LinearRegression()
reg.fit(X, y)

# 결과 출력
print(f"회귀계수: {reg.coef_[0]}")
print(f"절편: {reg.intercept_}")
print(f"Estimated value: {pi_estimates[-1]}")
print(f"built-in constant: {np.pi}")


# 예측 결과 시각화
plt.scatter(num_trials, pi_estimates, label='Estimated π values', color='blue')
plt.plot(num_trials, reg.predict(X), label='Linear Regression', color='red')
plt.axhline(np.pi, color='green', linestyle='--', label='built-in constant π (np.pi)')
plt.xlabel('Number of Trials')
plt.ylabel('Estimated π')
plt.legend()
plt.show()

from sklearn.preprocessing import PolynomialFeatures

# 로그 변환
X_log = np.log(num_trials).reshape(-1, 1)

# 다항 회귀 적용(2차)
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X_log)

reg = LinearRegression()
reg.fit(X_poly, y)

# 예측 및 시각화
plt.scatter(num_trials, pi_estimates, label='Estimated π values', color='blue')
plt.plot(num_trials, reg.predict(X_poly), label='Polynomial Regression', color='red')
plt.axhline(np.pi, color='green', linestyle='--', label='built-in constant π (np.pi)')
plt.xlabel('Number of Trials (log scale)')
plt.ylabel('Estimated π')
plt.xscale('log')
plt.legend()
plt.show()

