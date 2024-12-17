def ocultar_tweet(frase, palavra_censurada):

    if palavra_censurada in frase:
        frase = frase.replace(palavra_censurada, "*")
        print(frase)

    else:
        print("tudo certo :)")
            
    
frase = input()
palavra_censurada = input()
ocultar_tweet(frase, palavra_censurada)