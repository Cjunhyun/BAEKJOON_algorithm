#백준 단계별로 풀어보기 3.반복문

# 2739번
a = int(input())
for i in range(1,10):
    print("%d * %d = %d" %(a,i,a*i))

# 10950번
n = int(input())
nums = []
for i in range(0,n):
     count = list(map(int, input().split()))
     nums.append(count)
for i in range(0,n):
     print(nums[i][0]+nums[i][1])

# 8393번
n = int(input())
k = 0
for i in range(1,n+1):
    k += i
print(k)

# 25304번
sum = int(input())
n = int(input())
nums = []
for i in range(n):
    c = list(map(int, input().split()))
    nums.append(c)
test = 0
for i in range(n):
    test += nums[i][0] * nums[i][1]

if(sum == test):
    print("Yes")
else:
    print("No")

# 25314번
n = int(input())
count = 0
for i in range(0,n,4):
    count += 1
print("long "*count +"int")

# 15552번
import sys
n = int(input()) 
for i in range(n):
        a,b = map(int, sys.stdin.readline().split())
        print(a+b)
    
# 11021번
n = int(input())
nums = []
for i in range(0,n):
     count = list(map(int, input().split()))
     nums.append(count)
for i in range(n):
        print("Case #%d: %d" %(i+1,nums[i][0]+nums[i][1]))

# 11022번
n = int(input())
nums = []
for i in range(0,n):
     count = list(map(int, input().split()))
     nums.append(count)
for i in range(n):
        print("Case #%d: %d + %d = %d" %(i+1,nums[i][0],nums[i][1],nums[i][0]+nums[i][1]))
    
# 2438번
n = int(input())
for i in range(1,n+1):
    print("*"*i)

#2439번
n = int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"*"*i)

#10952번
k = 1
while k==1 :
    n = list(map(int, input().split()))
    if(n[0] == 0 and n[1]==0):
        k = 0
        break
    else:
        print(n[0]+n[1])

# 10951번
while True:
    try:
        A, B= map(int,input().split())
        print(A+B)
    except:
        break