def stockmarket(stock):
    resultado = {}
    
    for data, preco, quantidade, simbolo in stock:
        valor_total = preco * quantidade
        valor_total = float(valor_total)
        if data in resultado:
            resultado[data] += valor_total
        else:
            resultado[data] = valor_total
    
    return resultado
