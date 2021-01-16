## 백준 11399번


#입력
n= int(input())
k_list = map(int,input().split())
k_list = sorted(k_list)

work_min =0
sum_min =0

for i in range(n):

    work_min += k_list[i]
    sum_min = sum_min + work_min

print(sum_min)
