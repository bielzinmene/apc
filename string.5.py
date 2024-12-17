def transformar_numeros(frase):
    numeros_extenso = {
        "zero": "0", "um": "1", "dois": "2", "tres": "3", "quatro": "4", 
        "cinco": "5", "seis": "6", "sete": "7", "oito": "8", "nove": "9"
    }
    
    
    
    for extenso, algarismo in numeros_extenso.items():
        frase = frase.replace(extenso, algarismo)
            
    
    print(frase)

frase = input()

transformar_numeros(frase)
