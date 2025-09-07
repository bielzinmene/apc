def fatorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def serie_taylor(func, derivada, x, a, n):
    soma = 0
    for k in range(n):
        termo = derivada(a, k) * (x - a)**k / fatorial(k)
        soma += termo
    return soma

def f(x):
    return x

def derivada(a, k):
    if k == 0:
        return a 
    elif k == 1:
        return 1  
    else:
        return 0  

resultado = serie_taylor(f, derivada, 1, 0, 5)
print(resultado)
