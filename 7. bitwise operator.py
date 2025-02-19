# write a program to perform bitwise operators
a=0b1010
b=0b1100
print(f'using Right shift operator',bin(a>>2))
print(f'using Left shift operator',bin(a<<2))
print(f'using Bitwise AND operator',a&b)
print(f'using Bitwise OR operator',a|b)
print(f'using Bitwise XOR operator',a^b)
print(f'using Bitwise NOT operator',~a)
