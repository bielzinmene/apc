n_bits = int(input())

decimal = 0

for i_bit in range (n_bits-1, -1, -1):
    bit = int(input())
    decimal += bit * (2 ** i_bit)
print(decimal)