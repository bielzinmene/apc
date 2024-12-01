data = input().strip()
d, m, a = map(str, data.split('/'))
print(f'{d}-{m}-{a}')
print(f'{m}-{d}-{a}')
print(f'{a}/{m}/{d}')

