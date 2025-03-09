import numpy as np

# Euler Method implementation
def euler_method(f, a, b, N, y0):
    h = (b - a) / N
    t = a
    w = y0
    for _ in range(N):
        w += h * f(t, w)
        t += h
    return w

# Runge-Kutta (4th Order) Method
def runge_kutta_method(f, a, b, N, y0):
    h = (b - a) / N
    t = a
    w = y0
    for _ in range(N):
        k1 = f(t, w)
        k2 = f(t + h / 2, w + h / 2 * k1)
        k3 = f(t + h / 2, w + h / 2 * k2)
        k4 = f(t + h, w + h * k3)
        w += h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        t += h
    return w

# Function specified in the assignment
def function(t, y):
    return t - y ** 2

# Main execution
if __name__ == "__main__":
    a, b = 0, 2
    N = 10
    y0 = 1

    euler_result = euler_method(function, a, b, N, y0)
    runge_kutta_result = runge_kutta_method(function, a, b, N, y0)

    print("Euler's Method Approximation:", euler_result)
    print("Runge-Kutta Method Approximation:", runge_kutta_result)
