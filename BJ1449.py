## 백준 1449번 수리공 항승

# 입력
n,L = map(int,input().split())
n_list = list(map(int,input().split()))
n_list = sorted(n_list)

#
L_count = 0
start = 0

for i in range(len(n_list)):

    if (start < n_list[i]):

        L_count += 1
        start = n_list[i] + L - 1

print(L_count)
