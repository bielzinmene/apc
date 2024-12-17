entrada = input()
dados = entrada.split(", ")

nome_da_cor = dados[0]
ind_r = int(dados[1])
ind_g = int(dados[2])
ind_b = int(dados[3])

hexa = f"#{ind_r:X.2f}{ind_g:X.2f}{ind_b:X.2f}"

print(f"{nome_da_cor} {hexa}")