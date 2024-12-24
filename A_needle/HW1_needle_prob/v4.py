import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def buffon_needle_full_sequence(n_max, needle_length, line_distance):
    # n_max개의 난수를 한 번에 생성
    y_center = np.random.uniform(0, line_distance, n_max)
    sin_x = np.random.uniform(-1, 1, n_max)
    sin_y = np.random.uniform(-1, 1, n_max)

    # 방향 벡터의 y 성분 정규화 (sin_xy)
    sin_xy = sin_y / np.sqrt(sin_x**2 + sin_y**2)
    
    # 바늘이 교차했는지(True / False) 나타내는 배열
    y_up = y_center + (needle_length / 2) * sin_xy
    y_down = y_center - (needle_length / 2) * sin_xy
    cross_flags = ((y_down < 0) | (y_up > line_distance)).astype(int)

    # 바늘 교차 횟수
    cross_count = np.cumsum(cross_flags)

    # 각 i번째 시도에서의 π 추정값을 담을 배열
    pi_estimates = np.zeros(n_max)

    # Buffon Needle
    i_vals = np.arange(1, n_max + 1)
    nonzero_cross = cross_count > 0  # 교차 횟수가 0이 아닌 경우만 계산
    pi_estimates[nonzero_cross] = (2 * needle_length * i_vals[nonzero_cross]) / (cross_count[nonzero_cross] * line_distance)

    return pi_estimates

def run_experiment_and_visualize(n_max=10**6):

    # 모든 n에 대해 누적 계산
    pi_estimates = buffon_needle_full_sequence(
        n_max=n_max,
        needle_length=1.0,
        line_distance=2.0
    )

    # X: 시도 횟수(1부터 n_max까지), y: 추정된 π
    X = np.arange(1, n_max + 1).reshape(-1, 1).astype(np.float64)
    y = pi_estimates

    # 선형회귀
    model = LinearRegression()
    nonzero_mask = y > 0  # π 추정값이 0이 아닌 부분만 사용
    model.fit(X[nonzero_mask], y[nonzero_mask])
    y_pred = model.predict(X)

    # ======== 그래프 시각화 ========
    plt.figure(figsize=(10, 6))
    
    plt.scatter(X, y, s=1, alpha=0.3, label='Buffon Needle Estimates')  

    # 회귀선
    plt.plot(X, y_pred, color='red', linewidth=2, label='Linear Regression')

    # 실제(시스템 저장) π 선
    plt.axhline(np.pi, color='green', linestyle='--', linewidth=2, label='built-in π value')
    
    plt.xlabel('Number of Trials')
    plt.ylabel('Estimated π')
    plt.title(f'Buffon Needle (1 to {n_max}) - Full Linear Regression')
    plt.legend()
    plt.grid(True)

    # 그래프 저장
    plt.savefig('v4_buffon_regression.png', dpi=300)
    plt.show()

if __name__ == "__main__":
    run_experiment_and_visualize(n_max=10**6)
