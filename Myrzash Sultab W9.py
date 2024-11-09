# 1
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for san in a:
    if san < 5:
        print(san)

# 2
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for san in a:
    if san in b:
        c.append(san)
print(c)

# 3
import operator
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

sorted_d1 = sorted(d.items(), key=operator.itemgetter(1))
print(sorted_d1)

sorted_d2 = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
print(sorted_d2)

# 4
dict_a = {1:10, 2:20}
dict_b = {3:30, 4:40}
dict_c = {5:50, 6:60}

dict_d = {**dict_a, **dict_b, **dict_c}
print(dict_d)

# 5
my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}

for i in range(3):
    for key, value in my_dict.items():
        if value == max(my_dict.values()):
            print(key, value)
            my_dict.pop(key)
            break

# 6
birsan = input()
ne = int(input())

san = int(birsan, ne)
print(san)

# 7
n = int(input())

for i in range(1, n+1):
    for j in range(n-i+1):
        print(end=" ")

    C = 1
    for j in range(1, i+1):
        print(' ', C, sep='', end='')

        C = C * (i - j) // j
    print()