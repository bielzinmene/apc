def decodificar_string(codificada):
    resultado = []
    i = 0
    while i < len(codificada):
        letra = codificada[i]
        i += 1
        quantidade = 0
        while i < len(codificada) and codificada[i].isdigit():
            quantidade = quantidade * 10 + int(codificada[i]) 
            i += 1
        resultado.append(letra * quantidade)  
    return ''.join(resultado)

N = int(input())  
for _ in range(N):
    codificada = input().strip()
    print(decodificar_string(codificada))
