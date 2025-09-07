n = int(input())
pess_nt = {}
count = 0

for _ in range(n):
    nome, nota = input().split(',')  
    nota = float(nota)  
    pess_nt[nome] = nota  # adiciona ao dicionário

nota_esp = float(input())

# Coleta os nomes das pessoas que possuem a nota específica
nomes_com_nota_esp = [nome for nome, nota in pess_nt.items() if nota == nota_esp]
nomes_com_nota_esp.sort()
if len(nomes_com_nota_esp) == 0:
    print(f'Você foi o único aluno com essa nota.')
# Imprimir os nomes separados por '/'
print('/'.join(nomes_com_nota_esp))

    
