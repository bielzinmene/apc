entrada = input()
dados = entrada.split(", ")

nome_da_cor = dados[0]
ind_r = int(dados[1])
ind_g = int(dados[2])
ind_b = int(dados[3])

hexa = f"#{ind_r:02X}{ind_g:02X}{ind_b:02X}"

print(f"{nome_da_cor} {hexa}")
