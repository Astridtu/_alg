# 方法 a
def power2n_a(n):
    return 2**n

# 方法 b：用遞迴 （慢）
def power2n_b(n):
    if n == 0: return 1
    return power2n_b(n-1) + power2n_b(n-1)

# 方法 c：用遞迴 (快)
def power2n_c(n):
    if n == 0: return 1
    return 2 * power2n_c(n-1)

# 方法 d：用遞迴+查表 (Lookup table method)
lookup_table = {}

def power2n_d(n):
    if n in lookup_table:   # Check if value is already in the lookup table
        return lookup_table[n]
    
    if n == 0:              # Base case
        result = 1
    else:
        result = 2 * power2n_d(n-1)  # Recursive calculation
        
    lookup_table[n] = result  # Store the result in the lookup table
    return result

# Test the functions
print('power2n_a(10) =', power2n_a(10))
print('power2n_b(10) =', power2n_b(10))
print('power2n_c(40) =', power2n_c(40))
print('power2n_d(40) =', power2n_d(40))  # Using the lookup table method
