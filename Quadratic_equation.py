import math

# Taking input from user
a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))

# Calculate discriminant
d = b**2 - 4*a*c

# Check roots
if d > 0:
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    print("Two real roots:", root1, "and", root2)

elif d == 0:
    root = -b / (2*a)
    print("One real root:", root)

else:
    real = -b / (2*a)
    imag = math.sqrt(-d) / (2*a)
    print("Complex roots:", real, "+", imag, "i and", real, "-", imag, "i")