import numpy as np
from scipy.stats import norm

lambda_param = 1
true_median = np.log(2) / lambda_param
alpha = 0.05

def calculate_coverage_exp(n, num_simulations=1000):
    coverage_count = 0
    z = norm.ppf(1 - alpha / 2)

    for _ in range(num_simulations):
        sample = np.random.exponential(1 / lambda_param, n)
        sample_median = np.median(sample)
        sample_std = 1 / np.sqrt(n)
        lower_bound = sample_median - z * sample_std
        upper_bound = sample_median + z * sample_std

        if lower_bound <= true_median <= upper_bound:
            coverage_count += 1

    coverage_probability = coverage_count / num_simulations
    return coverage_probability


coverage_small = calculate_coverage_exp(25)
print(f"Вероятность попадания при маленькой выборке: {coverage_small}")
coverage_large = calculate_coverage_exp(10000)
print(f"Вероятность попадания при большой выборке:  {coverage_large}")
