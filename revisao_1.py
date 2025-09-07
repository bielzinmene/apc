inicio=1000
fim=9999

for i in range(inicio,fim,1):
    a=i//100
    b=i%100
    soma=a+b
    quadrado=soma**2
    if quadrado == 1:
        print(i)
    