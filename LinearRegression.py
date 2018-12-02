from numpy import *


def step_gradient(b_current, m_current, X, Y, learningRate):
    b_gradient = 0
    m_gradient = 0
    N = float(len(X))
    for i in range(0, len(X)):
        x = X[i]
        y = Y[i]
        b_gradient += -(2/N) * (y - ((m_current * x) + b_current))
        m_gradient += -(2/N) * x * (y - ((m_current * x) + b_current))
    new_b = b_current - (learningRate * b_gradient)
    new_m = m_current - (learningRate * m_gradient)
    return [new_b, new_m]


def gradient_descent_runner(X, Y, starting_b, starting_m, learning_rate, num_iterations):
    b = starting_b
    m = starting_m
    for i in range(num_iterations):
        b, m = step_gradient(b, m, X, Y, learning_rate)
    return [b, m]


def run(X, Y):
    learning_rate = 0.0001
    initial_b = 0
    initial_m = 0
    num_iterations = 1000
    [b, m] = gradient_descent_runner(
        X, Y, initial_b, initial_m, learning_rate, num_iterations)
    return [b, m]


if __name__ == '__main__':
    run()
