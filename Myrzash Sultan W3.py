"""
### 1
#1
print("4 8 15 16 23 42 ")
#2
print(4, 8, 15, 16, 23, 42, sep="\n")
#3
san = int(input())
print(san, san+1, san+2, sep="\n")
#4
a = int(input())
b = int(input())
c = int(input())
print(a+b+c)
#5
v = int(input())
print("V=", v**3,"\nTSA=", 6*v**2)
"""

### 2
#1
n = int(input())
k = int(input())
print(k // n)
print(k % n)
#2
digits = int(input())
print(digits//1000, (digits//100)%10, (digits//10)%10, digits%10, sep="\n")
#3
shrek = int(input())
print(shrek-shrek//2)