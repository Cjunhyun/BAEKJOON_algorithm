## 백준 1744번 수 묶기

k = int(input())

k_list = []

for i in range(k):
    
    k_int = int(input())
    k_list.append(k_int)

k_list = sorted(k_list , reverse = True)


##

x_list = []
y_list = []
k_sum = 0

for i in range(k):

    if (k_list[i] > 1) :
        x_list.append(k_list[i])
        
    elif (k_list[i] == 1) :
        k_sum += k_list[i]
        
    elif(k_list[i] < 1) :
        y_list.append(k_list[i])
        
y_list = sorted(y_list)



##
n = 2
x_list = [x_list[i * n:(i + 1) * n] for i in range((len(x_list) + n - 1) // n )] 


for i in range(len(x_list)):
    xx = 1
    for x in range(len(x_list[i])):
        xx *= x_list[i][x]
    k_sum += xx
    
  
##

n = 2
y_list = [y_list[i * n:(i + 1) * n] for i in range((len(y_list) + n - 1) // n )] 


for i in range(len(y_list)):
    yy=1
    for y in range(len(y_list[i])):
        yy *= y_list[i][y]
    k_sum += yy

print(k_sum)








        
        




        
        



        

    
