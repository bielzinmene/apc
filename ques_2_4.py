x1, x2, x3 = map(int, input().split())
c = input()

if c == 'P':
    print("Ponderada")
    y1, y2, y3 = map(int, input().split())
    media = ((x1*y1) + (x2*y2) + (x3*y3))/(y1+y2+y3)
    print(f'{media:.2f}')
elif c == 'A':
    print("Aritmetica")
    media = (x1+x2+x3)/3
    print(f'{media:.2f}')
elif c == 'H':
    print("Harmonica")
    media = 3/((1/x1) + (1/x2) + (1/x3))
    print(f'{media:.2f}')
else:
    print("Operação inexistente")

