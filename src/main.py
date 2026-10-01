from datetime import date

from utils import add, subtract, multiply, divide

print("Md. Maksude Ala")
print(date.today())

print("5 + 3 =", add(5, 3))
print("5 - 3 =", subtract(5, 3))
print("5 * 3 =", multiply(5, 3))
print("5 / 3 =", divide(5, 3))

try:
    print("5 / 0 =", divide(5, 0))
except ValueError as e:
    print("Error:", e)
