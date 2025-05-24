def Bisection_Method(f, a, b, epsilon=0.0001, max_iter=100):
    if f(a) * f(b) >= 0:
        print("⚠️ Error: The function must change sign in the given range.")
        return None

    iteration = 0
    while (b - a) / 2.0 > epsilon and iteration < max_iter:
        midpoint = (a + b) / 2.0
        f_mid = f(midpoint)
        iteration += 1

        if abs(f_mid) < epsilon:
            break

        if f(a) * f_mid < 0:
            b = midpoint
        else:
            a = midpoint

    root = (a + b) / 2.0
    print(f"✅ Bisection Method: Approximate root = {root}")
    print(f"🔄 Iterations = {iteration}")
    return root
