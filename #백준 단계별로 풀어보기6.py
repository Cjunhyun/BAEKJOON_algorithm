#백준 단계별로 풀어보기6
# 3003번
n_list = list(map(int,input().split()))
c = [1,1,2,2,2,8]
result = []

for i in range(len(n_list)):
    tem = c[i] - n_list[i]
    result.append(tem)

res = ' '.join(str(s) for s in result)
print(res)

# 2444번
n = int(input())

# 다이아몬드를 저장할 리스트 초기화
diamond = [" " * (2 * n - 1) for _ in range(2 * n - 1)]

# 다이아몬드 만들기
for i in range(n):
    diamond[i] = " " * (n - 1 - i) + "*" * (2 * i + 1)
    diamond[2 * n - 2 - i] = diamond[i]

# 다이아몬드 출력
for row in diamond:
    print(row)

# 10812번
n , m = map(int,input().split())
n_list = [] 
for i in range(1,n+1):
    n_list.append(i)

for i in range(m):
    i , j , k = map(int,input().split())
    i -= 1
    j -=1
    k -=1
    tem1 = n_list[i:k]
    tem2 = n_list[k:j+1]

    if(len(tem2) != 0 and len(tem1) != 0):

        n_list[i:i+len(tem2)] = tem2
        n_list[i+len(tem2):i+len(tem2)+len(tem1)] = tem1
    else:
        continue

res = ' '.join(str(s) for s in n_list)
print(res)

#10988번
s = input()
s_list = list(s)

check = 1
for i in range(len(s_list)):
    if(s_list[len(s_list)-1-i] != s_list[i]):
        check = 0
        
print(check)

# 1157번 공부해보기
s = input().upper()
s_list = list(set(s))
res_list =[]

for i in s_list:
    res_list.append(s.count(i))


if(res_list.count(max(res_list)) > 1):
    print("?")
else:
    m_index = res_list.index(max(res_list))
    print(s_list[m_index])

# 4344번
n = int(input())

for i in range(n):
    nums = list(map(int,input().split()))
    n_cnt = nums[0]
    n_sum = 0
    n_avr = 0
    for j in range(1,len(nums)):
        n_sum += nums[j]

    n_avr = n_sum/(n_cnt)
    av_cnt = 0
    for j in range(1,len(nums)):
        if(nums[j] > n_avr):
            av_cnt += 1
    res = float((av_cnt/n_cnt)*100)
    result = str(format(res,".3f"))
    print(result+"%")

# 2941번
s = list(input())
c_list = ['c=','c-','dz=','d-','lj','nj','s=','z=']
check = 0
idx = 0
while(len(s) > idx):
    if(idx == len(s)-1):
        tem = s[idx]
    else:
        tem = s[idx] + s[idx +1]

    if(tem in c_list):
        check += 1
        idx += 2
    elif(tem != 'dz'):
        check +=1
        idx +=1
    else:
        if((len(s) - idx) >= 3 and s[idx +2] == '='):
            check += 1
            idx += 3
        else:
            check +=1
            idx += 1
print(check)