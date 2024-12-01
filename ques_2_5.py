indiceReclamacao = int(input())
percentReclamResolPrim = int(input())
percentCliCancel = int(input())
indiceIndisponibilidade = int(input())
canceladoPorProblema = int(input())

# Cálculo do índice de reclamações
if percentReclamResolPrim >= 60:
    indice = indiceReclamacao - 5
else:
    indice = indiceReclamacao + 15
print(f'{indice}')

# Cálculo dos cancelamentos
if percentCliCancel <= 10:
    if canceladoPorProblema == 1:
        indice = indice + 80
    else:
        indice = indice - 30
else:
    if canceladoPorProblema == 1:
        indice = indice + 50
    else:
        indice = indice - 10
print(f'{indice}')

# Cálculo do índice de indisponibilidade
if indiceIndisponibilidade >= 10:
    indice = indice + 70
else:
    indice = indice - 20
print(f'{indice}')
