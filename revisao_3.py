def classisficador(a,b,c):
    if(a+b>c) and (b+c>a) and (a+c>b):
        print('triangulo')
        if (a!=b)and(a!=c):
            print('escaleno')
        elif(a==b)or(a==c)or(b==c):
            print('isoceles')
            if(a==b)and(a==c):
                print('equilatero')
        maior=max(a,b,c)
        if a==maior:
            lado1=b
            lado2=c
        elif b==maior:
            lado1=a
            lado2=c
        else:
            lado1=a
            lado2=b
        if(maior*2)==(lado1*2+lado2*2):
            print('retangulo')
    else:
        print('gondim sendo gondim')