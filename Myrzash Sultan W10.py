# 1
palindrom = "qazaq"

if palindrom == palindrom[::-1]:
    print("Palindrom")
else:
    print("Palindrom emes")

# 2
san = 92498
sec = san%60
min = san//60%60
hour = san//3600%24
day = san//86400

print(day, hour, min, sec, sep = ":")

# 3
sandar = "12, 345, 64, 9, 567, 89"
list_sandar = sandar.split(", ")
tuple_sandar = tuple(list_sandar)
print(list_sandar)
print(tuple_sandar)

# 4
print(list_sandar[0], list_sandar[-1])

# 5
programs = {"Chrome":"birdenge", "Word":"wordE", "Excel":"excelE", "PowerPoint":"powerpointX"}
suranys = input()
try :
    print(programs[suranys])
except KeyError:
    print("Qate")

# 6
n = input()
nn = int(n+n)
nnn = int(n+n+n)
print(int(n)+nn+nnn)

# 7
sandar = [12, 345, 64, 9, 567, 20, 89, 237, 11, 2]

for san in sandar:
    if san == 237:
        break
    if san % 2 == 0:
        print(san, end=" ")