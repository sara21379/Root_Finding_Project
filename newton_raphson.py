def Newton_Raphson(f, f_prime, x0, epsilon=0.0001, max_iter=100):
    iteration = 0
    x = x0

    while iteration < max_iter:
        fx = f(x)
        fpx = f_prime(x)

        if fpx == 0:
            print("Derivative equals 0. Cannot continue.")
            return None

        x_new = x - fx / fpx
        iteration += 1

        if abs(x_new - x) < epsilon:
            print(f"Estimated root: {x_new}")
            print(f"Number of iterations: {iteration}")
            return x_new

        x = x_new

    print("The method did not converge after 100 iterations.")
    return None
if __name__ == "__main__":
    def f(x):
        return x**3 - x - 2

    def f_prime(x):
        return 3 * x**2 - 1

    Newton_Raphson(f, f_prime, x0=1.5)
