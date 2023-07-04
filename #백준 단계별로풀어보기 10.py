#백준 단계별로풀어보기 10
#27323번
a = int(input())
b = int(input())
print(a*b)

#1085번
x,y,w,h = map(int,input().split())
dis_list = []
dis_list.append(x)
dis_list.append(y)
dis_list.append(w-x)
dis_list.append(h-y)
print(min(dis_list))

#3009번
from collections import Counter

x_list = []
y_list = []

for i in range(3):
    x,y = map(int,input().split())
    x_list.append(x)
    y_list.append(y)

counter1 = Counter(x_list)
most_common1 = counter1.most_common()
counter2 = Counter(y_list)
most_common2 = counter2.most_common()

print(most_common1[-1][0],most_common2[-1][0])

#15894번
n = int(input())
print(n*4)

#9063번
n = int(input())
x_list = []
y_list = []
for i in range(n):
    x,y = map(int,input().split())
    x_list.append(x)
    y_list.append(y)
x_len = max(x_list) - min(x_list)
y_len = max(y_list) - min(y_list)
if(n < 2):
    print("0")
else: 
    print(x_len * y_len)

#10101번
n_list = []
for i in range(3):
    n = int(input())
    n_list.append(n)

n_list.sort()
a = n_list[0]
b = n_list[1]
c = n_list[2]

if a+b+c == 180:
    if a == b == c == 60:
        print("Equilateral")
    elif a == b or b == c or c == a:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")

#5073번
check = 1
while(check):
    a,b,c = map(int,input().split())

    if( a == b == c == 0):
        check = 2
        break 

    if(a + b <= c or a + c <= b or b + c <= a):
        print("Invalid")
    elif(a ==  b == c):
        print("Equilateral")
    elif(a == b != c or b == c != a or c==a!=b):
        print("Isosceles")
    else:
        print("Scalene")

#14215번
n_list = list(map(int, input().split()))
n_list.sort()
a = n_list[0]
b = n_list[1]
c = n_list[2]

if(a + b > c):
    print(a+b+c)
else:
    c = a + b - 1
    print(a+b+c)