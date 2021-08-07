## 백준 알고리즘 1139번 
## 한줄로 서기


k = int(input())

k_list = list(map(int,input().split()))
##
s_list =[0]*k
y = k

while ( y != 0 ) :
    
    for i in range(len(k_list),0,-1):
        check = 0
        x = k_list[i-1]

        for n in range(len(s_list)):

            if ( check == x ) :

                s_list.insert(n,y)
                y = y-1
                break
                
            if ( y < s_list[n]):
                check += 1

while 0 in s_list :
    s_list.remove(0)


            
for b in s_list:
    print(b, end = ' ')
