#백준 단계별로 풀어보기 2.조건문

# 1330번
A,B = map(int,input().split())
if(A>B):print(">")
elif(A<B):print("<")
else : print("==")

# 9498번
a = int(input())
if(a>=90) : print("A")
elif(90>a>=80):print("B")
elif(80>a>=70):print("C")
elif(70>a>=60):print("D")
else:print("F")

#2753번
a = int(input())
if(a%4 ==0 and a%100 != 0):print("1")
elif(a%400 ==0):print("1")
else:print("0")

#1461번
a=int(input())
b=int(input())
if(a>0 and b>0):print("1")
elif(a>0 and b<0):print("4")
elif(a<0 and b<0):print("3")
else:print("2")

#2884번
a,b = map(int,input().split())
if(b>=45): print(a,b-45)
elif(b<45):
    b = 60+(b-45)
    if(a==0):print(23,b)
    else:print(a-1,b)

#2525번
a,b = map(int,input().split())
c = int(input())
if(c+b <60):
    print(a,c+b)
else:
    n = (c+b)//60
    m = (c+b)%60
    if(a+n>23):
        print((a+n)%24,m)
    else:
        print((a+n),m)

#2480번
a,b,c = map(int,input().split())
if(a==b==c):
    print(10000 + a*1000)
elif(a==b or a==c):
    print(1000 + a*100)
elif(b==c):
    print(1000+b*100)
else:
    i = max(a,b,c)
    print(i*100)