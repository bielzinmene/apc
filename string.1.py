def tem_virgula(frase):
    count = 0
    for virguala in frase:
        if "," in frase:
            count =+1
    if count > 0:
        print("Passed")
    else:
        print("Failed")

frase = input()
tem_virgula(frase)