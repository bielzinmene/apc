pas, trans = input().split()
pas = int(pas)

if trans == 'C':
    val = pas * 60
    print(f"Para transportar {pas} passageiros de canoa sairá R$ {val:.2f}")
elif trans == 'B':
    val = pas * 105
    print(f"Para transportar {pas} passageiros de barco sairá R$ {val:.2f}")
elif trans == 'V':
    val = pas * 120
    print(f"Para transportar {pas} passageiros de voadeira sairá R$ {val:.2f}")