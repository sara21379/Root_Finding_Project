from bisection_method import Bisection_Method
from newton_raphson import Newton_Raphson
from secant_method import Secant_Method

def f(x):
    return x**3 - x - 2

def f_prime(x):
    return 3 * x**2 - 1

def main():
    print("Choose a method for finding roots:")
    print("1. Bisection")
    print("2. Newton-Raphson")
    print("3. Secant")

    choice = input("Enter method number (1-3): ").strip()
    if choice not in ['1', '2', '3']:
        print(" Invalid method number. Please choose 1, 2, or 3.")
        return

    try:
        start = float(input("Enter lower end of the range: "))
        end = float(input("Enter upper end of the range: "))
    except ValueError:
        print(" Invalid input. Range bounds must be numeric.")
        return

    if start == end:
        print(" Range cannot have identical start and end values.")
        return
    elif start > end:
        start, end = end, start  # Swap if reversed

    #  Limit range span
    if end - start > 1_000_000:
        print(" The range is too large. Please choose a smaller interval.")
        return

    try:
        step = float(input("Enter step size (e.g. 0.1): "))
    except ValueError:
        print(" Invalid input. Step size must be numeric.")
        return

    if step <= 0:
        print(" Step size must be greater than 0.")
        return
    elif step > (end - start):
        print(" Step size is too large for the given range.")
        return

    #  Limit expected iterations
    max_steps = int((end - start) / step)
    if max_steps > 100_000:
        print(" Too many iterations expected. Please increase step size or reduce range.")
        return

    try:
        epsilon = float(input("Enter epsilon precision level (e.g. 0.0001): "))
    except ValueError:
        print(" Invalid input. Epsilon must be numeric.")
        return

    if epsilon <= 0:
        print(" Epsilon must be greater than 0.")
        return
    elif epsilon > 1:
        print(" Epsilon is too large. Please choose a smaller value like 0.0001.")
        return

    x = start
    found_any = False

    while x < end:
        x1 = x
        x2 = x + step

        try:
            fx1 = f(x1)
            fx2 = f(x2)
            fpx1 = f_prime(x1)
            fpx2 = f_prime(x2)
        except Exception as e:
            print(f" Error evaluating function: {e}")
            return

        # Case 1: function changes sign
        if fx1 * fx2 < 0:
            found_any = True
            print(f"\n>>> Found a range with sign change: ({x1}, {x2})")
            if choice == '1':
                Bisection_Method(f, x1, x2, epsilon)
            elif choice == '2':
                x0 = (x1 + x2) / 2
                Newton_Raphson(f, f_prime, x0, epsilon)
            elif choice == '3':
                Secant_Method(f, x1, x2, epsilon)

        # Case 2: root at endpoints
        elif abs(fx1) < epsilon:
            found_any = True
            print(f"\n>>> f({x1}) is very close to zero. Approximate root: {x1}")
        elif abs(fx2) < epsilon:
            found_any = True
            print(f"\n>>> f({x2}) is very close to zero. Approximate root: {x2}")

        # Case 3: possible multiple root
        elif abs(fx1) < epsilon and abs(fpx1) < epsilon:
            found_any = True
            print(f"\n>>> f({x1}) ≈ 0 and f'({x1}) ≈ 0. Possible multiple root at: {x1}")
        elif abs(fx2) < epsilon and abs(fpx2) < epsilon:
            found_any = True
            print(f"\n>>> f({x2}) ≈ 0 and f'({x2}) ≈ 0. Possible multiple root at: {x2}")

        x += step

    if not found_any:
        print("\n No roots were found within the given range.")

if __name__ == "__main__":
    main()
