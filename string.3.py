def conta_dig(frase):
    count = 0
    for i in frase:
        if i.isdigit():
            count +=1
    return count

frase = input()
print(conta_dig(frase))

