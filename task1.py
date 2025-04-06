import numpy as np
from scipy.stats import norm

mu1 = 2
mu2 = 1
sigma1_sq = 1
sigma2_sq = 0.5
true_diff = mu1 - mu2
alpha = 0.05


def calculate_coverage(n1, n2, num_simulations=1000):
    coverage_count = 0
    sigma = np.sqrt(sigma1_sq / n1 + sigma2_sq / n2)
    z = norm.ppf(1 - alpha / 2)

    for _ in range(num_simulations):
        X1 = np.random.normal(mu1, np.sqrt(sigma1_sq), n1)
        X2 = np.random.normal(mu2, np.sqrt(sigma2_sq), n2)
        X1_mean = np.mean(X1)
        X2_mean = np.mean(X2)
        diff_mean = X1_mean - X2_mean
        lower_bound = diff_mean - z * sigma
        upper_bound = diff_mean + z * sigma

        if lower_bound <= true_diff <= upper_bound:
            coverage_count += 1

    coverage_probability = coverage_count / num_simulations
    return coverage_probability


coverage_small = calculate_coverage(25, 25)
print(f"Вероятность попадания при маленькой выборке: {coverage_small}")
coverage_large = calculate_coverage(10000, 10000)
print(f"Вероятность попадания при большой выборке: {coverage_large}")
