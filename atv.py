import math
from decimal import Decimal, getcontext

getcontext().prec = 50

def format_zero(n, epsilon=1e-9):
    n = Decimal(n)
    if abs(n) < epsilon:
        return '-0' if n < 0 else '0'
    return str(n)

def round_decimal(n, decimals=0):
    n = Decimal(n)
    return n.quantize(Decimal('1e-{0}'.format(decimals)))

def format_signed_zero(n):
    if n == 0:
        return '-0' if str(n).startswith('-') else '0'
    return str(n)

f1, f2 = map(float, input().split())
d1, d2 = map(float, input().split())

f1, f2, d1, d2 = Decimal(f1), Decimal(f2), Decimal(d1), Decimal(d2)

print(f"F1 = {f1}, F2 = {f2}")
print(f"D1 = {d1}, D2 = {d2}")
print()

print(f"F1 = {f1:.2f}, F2 = {f2:.2f}")
print(f"D1 = {d1:.2f}, D2 = {d2:.2f}")
print()

print(f"F1 = {f1:.5f}, F2 = {f2:.5f}")
print(f"D1 = {d1:.5f}, D2 = {d2:.5f}")
print()

print(f"F1 = {f1:.10f}, F2 = {f2:.10f}")
print(f"D1 = {d1:.10f}, D2 = {d2:.10f}")
print()

print(f"F1 = {f1:.28f}, F2 = {f2:.28f}")
print(f"D1 = {d1:.28f}, D2 = {d2:.28f}")
print()

print(f"F1 = {f1:.3E}, F2 = {f2:.3E}")
print(f"D1 = {d1:.3E}, D2 = {d2:.3E}")
print()

f1_rounded = round_decimal(f1, 0)
f2_rounded = round_decimal(f2, 0)
d1_rounded = round_decimal(d1, 0)
d2_rounded = round_decimal(d2, 0)

print(f"F1 = {format_signed_zero(f1_rounded)}, F2 = {format_signed_zero(f2_rounded)}")
print(f"D1 = {format_signed_zero(d1_rounded)}, D2 = {format_signed_zero(d2_rounded)}")
