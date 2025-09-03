def to_twos_complement(value, bits=8):
    if value < 0:
        value = (1 << bits) + value
    return format(value, f'0{bits}b')
def from_twos_complement(binary_str):
    bits = len(binary_str)
    value = int(binary_str, 2)
    if binary_str[0] == '1':  
        value -= (1 << bits)
    return value
binary_repr = to_twos_complement(-42, 8)
print("2's complement of -42 (8 bits):", binary_repr)
original = from_twos_complement(binary_repr)
print("Back to decimal:", original)
