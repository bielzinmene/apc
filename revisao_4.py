n=int(input())
gasto_deivis=0

for i in range(n):
    renda_cidadao_i=int(input())
    if renda_cidadao_i<1000:
        gasto_deivis+=1000-renda_cidadao_i

print(gasto_deivis)