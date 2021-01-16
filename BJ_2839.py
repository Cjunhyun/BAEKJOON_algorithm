##백준 2839번

k = int(input())

cnt = 0

while(k > 0):
    
    if (k %5==0):
        k -= 5
        cnt += 1

    elif (k %3==0):
        k -= 3
        cnt += 1
    elif (k >5):
        k -= 5
        cnt += 1
    else :
        cnt = -1
        break

    
print(cnt)
    

    

