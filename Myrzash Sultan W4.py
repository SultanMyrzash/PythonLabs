#1
n = int(input())
print(n << 1)

#2
a = int(input())
b = int(input())
c = input("+,-,*,/:")

if (c == "+"):
    print(a+b)
elif (c == "-"):
    print(a-b)
elif (c == "*"):
    print(a*b)
elif (c == "/"):
    print(a/b)
else: print("Qate")

#3
san = int(input())
san1 = san//1000
san2 = (san//100)%10
san3 = (san//10)%10
san4 = san%10

if (san1 + san4 == san2 - san3):
    print("yes")
else:
    print("no")
    
#4
age = int(input())
if (age >= 18):
    print("Access allowe")
else:
    print("Access denied")

#5
qn = int(input("Qansha san tergingiz keledi (keminde 3 san):"))
arf = [int(input(f"San {i+1}:")) for i in range(qn)]
arp = arf[1]-arf[0]
for shrek in range(qn-1):
    if arf[shrek]+arp == arf[shrek+1]:
        continue
    else:
        print("no")
        break
else:
    print("YES")
    
#6
rook1 = int(input())
rook2 = int(input())
rook3 = int(input())
rook4 = int(input())

if(rook1<9 and rook2<9 and rook3<9 and rook4<9 and rook1>0 and rook2>0 and rook3>0 and rook4>0):
    if ((rook1==rook3) ^ (rook2==rook4)):
        print("Yes")
    else:
        print("no")
else:
    print("no")

#7
king1 = int(input())
king2 = int(input())
king3 = int(input())
king4 = int(input())

if(king1<9 and king2<9 and king3<9 and king4<9 and king1>0 and king2>0 and king3>0 and king4>0):
    check = 0
    if(king1 == king3 + 1):check += 1
    if(king2 == king4 + 1):check+= 1
    if(king1 == king3 - 1):check+= 1
    if(king2 == king4 - 1):check+= 1
    if(king1 == king3):check+= 1
    elif(king2 == king4):check+= 1
else: print("Taqtada ondai sandar zhoq")
if check == 2:
    print("yes")
else:
    print("no")

#8
x1 = int(input())
x2 = int(input())
x3 = int(input())

if(x1 > x2):
    if(x2>x3):
        print(x2)
    elif(x3<x1):
        print(x3)
    else:print(x1)
elif(x2 > x1):
    if(x1>x3):
        print(x1)
    elif(x3<x2):
        print(x3)
    else:
        print(x2)
else:
    if(x1>x3):
        print(x1)
    elif(x3<x2):
        print(x3)
    else:
        print(x2)


