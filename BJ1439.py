## 백준 1439번 뒤집기
import sys

#입력
s = sys.stdin.readline()
s=s.rstrip() #개행문자 제거

#0,1 기준으로 쪼개기
s0_list = list(s.split('0'))
s1_list = list(s.split('1'))

#공백제거
s0_list = list(filter(None,s0_list))
s1_list = list(filter(None,s1_list))

#출력
if(len(s0_list) > len(s1_list)):
    print(len(s1_list))
else:
    print(len(s0_list))
