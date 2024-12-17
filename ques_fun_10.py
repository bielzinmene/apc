def troco(x):
    m50 = x // 50
    x = x % 50
    print(f'{m50} moedas de 50 centavos')
    
    m25 = x // 25
    x = x % 25
    print(f'{m25} moedas de 25 centavos')
    
    m10 = x // 10
    x = x % 10
    print(f'{m10} moedas de 10 centavos')

    m05 = x // 5
    x = x % 5
    print(f'{m05} moedas de 5 centavos')

    m01 = x // 1
    x = x % 1
    print(f'{m01} moedas de 1 centavo')
