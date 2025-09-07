def fatorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def exp_taylor(x, n):
    soma = 0
    for k in range(n):
        soma += x**k / fatorial(k)
    return soma

print(exp_taylor(1, 10))
