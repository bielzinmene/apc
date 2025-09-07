saque=int(input())

notas_100=0
notas_50=0
notas_20=0
notas_10=0
notas_2=0
notas_1=0

while True:
    if saque>=100:
        saque=saque-100
        notas_100+=1
    elif saque>=50:
        saque-=50
        notas_50 += 1
    elif saque>=20:
        saque-=20
        notas_20 += 1
    elif saque>=10:
        saque-=10
        notas_10 += 1
    elif saque>=2:
        saque-=2
        notas_2 += 1

    if saque==0:
        break

if notas_100>0:
    print(f'Entregue {notas_100} nota de R$ 100,00')
if notas_50>0:
    print(f'Entregue {notas_50} nota de R$ 50,00')
if notas_20>0:
    print(f'Entregue {notas_20} nota de R$ 20,00')
if notas_10>0:
    print(f'Entregue {notas_10} nota de R$ 10,00')
if notas_2>0:
    print(f'Entregue {notas_2} nota de R$ 2,00')
if notas_1>0:
    print(f'Entregue {notas_1} nota de R$ 1,00')