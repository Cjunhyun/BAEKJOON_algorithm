##백주 5585번 거스름돈

m = int(input())
change_m = 1000-m
count = 0

while(1):

    if(change_m >= 500):
        change_m -= 500
        count += 1
    elif(change_m >= 100):
        change_m -= 100
        count +=1
    elif(change_m >= 50):
        change_m -= 50
        count += 1
    elif(change_m >= 10):
        change_m -= 10
        count += 1
    elif(change_m >= 5):
        change_m -= 5
        count += 1
    elif(change_m >= 1):
        change_m -= 1
        count += 1
    elif(change_m == 0):
        break
    

print(count)


