# Contando quantas vezes o número 6 aparece de 1 a 1536
count_6 = sum('6' in str(i) for i in range(1, 1537))
print(count_6)
