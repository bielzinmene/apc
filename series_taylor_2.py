import math

def fact(n):
    if n == 0:
        return 1
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

def cos(x, N=10):
    somatorio=0
    for n in range(N):
        elem=(-1)**n/fact(2*n)
        elem*=(x**(2*n))
        somatorio+=elem
    return somatorio

def sin(x,N=10):
    somatorio=0
    for n in range(N):
        elem=(-1)**n/fact(2*n+1)
        elem*=(x**(2*n+1))
        somatorio+=elem
    return somatorio

def angle2grads(angle_in_degrees):
    return math.radians(angle_in_degrees)

a = float(input())
grad_a=angle2grads(a)

print(f"cos({a}) = {cos(grad_a):.4f}, math.cos({a}) = {math.cos(grad_a):.4f}")
print(f"sin({a}) = {sin(grad_a):.4f}, math.sin({a}) = {math.sin(grad_a):.4f}")