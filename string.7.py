def verificar_palindromo(s):
    n = len(s)
    count = 0
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            count += 1
    
    if count == 1 or (count == 0 and n % 2 == 1):
        return "ON"
    else:
        return "OFF"

s = input().strip()
print(verificar_palindromo(s))
