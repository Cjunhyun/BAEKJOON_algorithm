# 백준 4796번 캠핑

##이중리스트를 만들어서 입력값 받기

c_list = []
c_index = 0

while True :

    a, b, c = map(int,input().split())

    if(a==0 and b==0 and c==0):
        break

    c_list.append([])
    c_list[c_index].append(a)
    c_list[c_index].append(b)
    c_list[c_index].append(c)

    c_index += 1


##이중리스트 인덱스 순서대로 case비교

case_list = []

for i in range(len(c_list)):
    case_time = 0

    case_l = c_list[i][0]
    case_p = c_list[i][1]
    case_v = c_list[i][2]

    count = case_v // case_p
    case_time += count*case_l

    left_time = case_v % case_p

    if (left_time < case_l):
        case_time += left_time
    elif ( left_time >=case_l):
        case_time += case_l

    case_list.append(case_time)


##비교한 case리스트 요소들을 출력

for i in range(len(case_list)):
    print('Case {}: {}'.format(i+1,case_list[i]))
