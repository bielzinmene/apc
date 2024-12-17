def concat(frase):
    primeiros = frase[0:2]
    ultimos = frase[-2:]
    redef = primeiros + ultimos
    print(redef)
frase = input()
concat(frase)