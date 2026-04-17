# max_value = max(1, 30, 50)
# print(max_value)

# min_value = min(1, 30, 50)
# print(min_value)

# max_str = max('AAC', "ABC", "ACC")
# print(max_str)

# min_str = min('AAC', "ABC", "ACC")
# print(min_str)

# length = len('안녕하세요.')
# print(length)

# result = eval('10+20+30+40')
# print(result)

# result = eval("not 40>50")
# print(result)

# list = [2, 5, 5, 3, 9, 1]
# result = sorted(list)
# print(result)

# print('')
# str1 = '안녕하세요'
# str_id = id(str1)
# print(str_id)

# list_id = id([1,2,3,4,5])
# print(hex(list_id))     #16진수
# print(oct(list_id))     #8진수

# print(type(3.14))
# print(type([1,2,3,4,5]))

# print(abs(-5))

###############################################
# import datetime

# today = datetime.date.today()
# print(today)
# now = datetime.datetime.now()
# print(now)

# print(now.year)
# print(now.month)
# print(now.day)

# print(dir(datetime))

# print('')

###############################################
# import datetime as dt

# today = dt.date.today()
# print(today)
# now = dt.datetime.now()
# print(now)

# know = now + dt.timedelta(hours=9)
# print(know)

# time_diff = know - now
# print(time_diff)

# print('')

# from datetime import datetime, date
# xmas1 = datetime(2023, 12, 25, 0, 0)
# print(xmas1)
# xmas2 = date(2025, 12, 15)
# print(xmas2)
# print(datetime.today())

###############################################
# import time

# print(time.time())

# local_time = time.localtime(time.time())
# str_time = time.strftime('%Y-%m-%d %H:%M:%s', local_time)
# print(str_time)

###############################################
# import math

# print(dir(math))
# print(math.ceil(3.1))       #4
# print(math.floor(3.9))      #3
# print(math.fabs(-3.1))      #3.1
# print(abs(-3.1))            #3.1
# print(math.pi)              #3.141592..
# print(math.sin(math.pi/2))  #1.0


###############################################
# import random

# print(random.random())
# print(random.randrange(1, 7))   #1~6
# print(random.randint(1, 7))     #1~7

# list1 = [1,2,3,4,5,6,7,8,9,10]
# random.shuffle(list1)   #순서 바꿈
# print(list1)
# print(random.choice(list1)) #하나 임의 선택
# print(random.sample(list1, 5))  #5개 아이템 임의 선택

###############################################
# # 로또 번호 만들기 실습
# import random
# list1 = list(range(1, 46))

# # shuffle 함수 이용
# list_rtn = []
# random.shuffle(list1)
# list_rtn = list1[0:6]
# list_rtn.sort()
# print(list_rtn) 

# # sample 함수 이용 
# list_rtn = random.sample(list1, 6)
# list_rtn.sort()
# print(list_rtn) 

# #내장모듈 활용
# import os
# #print(dir(os))

# print(os.sep) #경로구분자
# cur_dir = os.getcwd() #현재 작업경로
# print(cur_dir)
# test_dir = os.path.join(cur_dir, 'SHK_test')

# print(test_dir)

# print(os.path.exists(test_dir))
# if not os.path.exists(test_dir):
#     os.mkdir(test_dir)
# print(os.path.exists(test_dir))

# 파일 읽기 
# f=open('test.txt', 'r')
# text = f.read()
# print(text)
# f.close()

# with open('test.txt', 'r+') as f:
#     text = f.read()
#     print(text)

# with open('test.txt', 'r+') as f:
#     lines = f.readlines()

#     for line in lines:
#         print(line, end = "")

# with open('test.txt', 'r') as f:
#     print(f.readline(), end="")
#     print(f.readline(), end="")
#     print(f.readline(), end="")
#     print(f.readline(), end="")

# #파일 쓰기
# text = '안녕하세요.\n 파이썬입니다.\n 반갑습니다.\n'
# # with open('test.txt', 'w') as f:
# #     f.write(text)

# with open('test.txt', 'a') as f:
#     f.writelines(text)

# #exception
# str1 = input('피젯수를 입력하시오.')
# str2 = input('젯수를 입력하시요')

# try:
#     num1 = int(str1)
#     num2 = int(str2)
#     result = num1 / num2
#     print('{} / {} = {}'.format(num1, num2, result))
# # except:
# #     print('입력값을 확인하시요.')
# # except Exception as e:
# #     print("exception: ", e)
# # except ValueError:
# #     print('숫자를 입력하시오.')
# # except ZeroDivisionError:
# #     print('0으로 나눌 수 없습니다.')
# except Exception as e:
#     print("Exception: ", e)
# else:
#     print('Except Else: {} / {} = {}'.format(num1, num2, result))
# finally:
#     print('처리가 완료되었습니다')


#읽기 오류 표시 실습
try:
    f = open('test11.txt', 'r')
    text = f.read()
    print(text)
    f.close()
except Exception as e:
    print('파일을 여는중 예외가 발생했습니다: ', e)

