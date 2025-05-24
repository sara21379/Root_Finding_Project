def Secant_Method(f, x0, x1, epsilon=0.0001, max_iter=100):
    iteration = 0

    while iteration < max_iter:
        f_x0 = f(x0)
        f_x1 = f(x1)

        denominator = f_x1 - f_x0
        if denominator == 0:
            print("⚠️ Secant method error: division by zero.")
            return None

        x2 = x1 - f_x1 * (x1 - x0) / denominator
        iteration += 1

        if abs(x2 - x1) < epsilon:
            print(f"✅ Secant Method: Approximate root = {x2}")
            print(f"🔄 Iterations = {iteration}")
            return x2

        x0, x1 = x1, x2

    print("❌ Secant Method did not converge after maximum iterations.")
    return None
