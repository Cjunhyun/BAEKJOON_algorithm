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