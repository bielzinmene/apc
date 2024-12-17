mais = '+'
tracinho = '-'
barra = '|'
valor = 'preço'
cifrao = 'R$'
linha1 = mais + tracinho*20 + mais + tracinho*20 + mais
linha2 = barra + " "*8 + 'peixe' + " "*7 + barra + " "*6 + 'preço   R$' + " "*4 + barra
linha3 = '+' + '-' * 41 + '+'
count = 0 
menor_preco = float('inf')
peixe_menor = ""


def peixes(peixe, preco):
    n = len(peixe)
    espaco = 20 - n
    if count == 1:
        print(linha1)
        print(linha2)
        print(linha1)
        print(f"| {peixe:<19}{barra}{preco:>19.2f} |")
        print(linha1)
    
    if count > 1:
        print(f"| {peixe:<19}{barra}{preco:>19.2f} |")
        print(linha1)

def sem_peixe():
        print(linha1)
        print(linha2)
        print(linha1)
        print(f"| {'Hoje não tem peixe':^38}  |")
        print(linha3)

def cambada(menor_preco, peixe_menor):
    if preco < menor_preco:
        menor_preco = preco
        peixe_menor = peixe

def menor():

    print(linha3)
    print(f"| {'Cambada de menor preço':^38}  |")
    print(linha1)
    print(f"| {peixe_menor:<19}{barra}{menor_preco:>19.2f} |")
    print(linha1)



while True:

     
    peixe, preco = input().split()
    preco = float(preco)
    count +=1

    cambada(menor_preco, peixe_menor)

    if peixe == 'fim' and preco < 0:
        if count == 1:
            sem_peixe()
            break
    if peixe == 'fim' and preco < 0:
         if count > 1:
              menor()
              break
    else:
        peixes(peixe, preco)


        
