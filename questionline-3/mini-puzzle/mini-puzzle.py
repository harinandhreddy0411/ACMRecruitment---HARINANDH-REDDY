def rotate_and_convert(binary_str: str, k: int) -> int:
    n = len(binary_str)
    k = k % n  
    rotated = binary_str[-k:] + binary_str[:-k]
    decimal_value = int(rotated, 2)
    
    return decimal_value
print(rotate_and_convert("1011", 1))  
print(rotate_and_convert("1011", 2))  


