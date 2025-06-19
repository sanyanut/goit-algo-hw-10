import numpy as np
import scipy.integrate as spi


def f(x):
    return x**2


a = 0
b = 2

result, error = spi.quad(f, a, b)

print("Інтеграл: ", result, error)

y_max = f(b)
area_rect = (b - a) * y_max
exact_value = 8 / 3

n_variations = [100, 1000, 10000, 100000, 1000000, 10000000]

print(f"Точне значення інтеграла: {exact_value:.6f}\n")
print("-" * 67)
print(
    f"{'К-сть точок (N)':<19} | {'Результат Монте-Карло':<23} | {'Абсолютна похибка'}"
)
print("-" * 67)

for n in n_variations:

    x_rand = np.random.uniform(a, b, n)
    y_rand = np.random.uniform(0, y_max, n)

    points_under_curve = np.sum(y_rand <= f(x_rand))

    integral_monte_carlo = area_rect * (points_under_curve / n)

    error = abs(integral_monte_carlo - exact_value)

    print(
        f"N = {n:<15} | Інтеграл ≈ {integral_monte_carlo:<12.6f} | Похибка = {error:.6f}"
    )

print("-" * 67)
