soma = 0.00
salario_maior = float(-1000000.00)
maior_salario_nome = ""
salario_menor = float(1000000.00)
menor_salario_nome = ""
cont = int(input())
cont_stop = 0
media_salaria = float(0.00)

if cont == 0:
    print("Não tem média")
    print("Não tem")
    print("Não tem")
else:
 while True:
    
    nome,salario = input().split(",")
    salario = float(salario)
    soma += salario
    
    if salario > salario_maior:
        salario_maior = salario
        maior_salario_nome = nome 
    if salario < salario_menor:
        salario_menor = salario
        menor_salario_nome = nome 

    cont_stop+=1

    if cont == cont_stop:
        break
    
if cont > 0:
    media_salaria = soma / cont

    print(f'{media_salaria:.2f}')
    print(f'{maior_salario_nome} {salario_maior:.2f}')
    print(f'{menor_salario_nome} {salario_menor:.2f}')



