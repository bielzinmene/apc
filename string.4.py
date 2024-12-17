def format_string(format_frase):
    finalstring = format_frase.replace(" ", "")
    print(finalstring)

def isimpar(frase):
    format_frase = frase[1::2]
    format_string(format_frase)

frase = input()
isimpar(frase)