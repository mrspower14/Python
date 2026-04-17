# adult = 18
# age = 19
# if age < adult :
#     print('당신은 미성년자입니다.')
#     print('당신은 입장할 수 없습니다.')
# else:
#     print('당신은 성인입니다.')
    
# print('')
# gender = 'male'
# if gender == 'male':
#     print('당신은 남자입니다.')
# else:
#     print('당신은 남자가 아닙니다.')

# print('')
# score = 90
# if score >= 90:
#     result = 'A'
# elif score > 80:
#     result = 'B'
# elif score >= 70:
#     result = 'C'
# elif score >= 60:
#     result = 'D'
# else:
#     result = 'F'
# print(result)

# print('')
# for i in range(10):
#     print('Hello World!', i)
# print('')
# for i in range(1, 10):
#     print('Hello World!', i)  
# print('')  
# for i in range(10, 0, -1):
#     print('Hello World!', i) 

# print('')  
# list1 = [1,2,3,4,5,6,7,8,9,10]
# for num in list1:
#     print(num)
# print('')  
# fruits = ('apple', 'orange', 'grape')
# for fruit in fruits:
#     print(fruit)
# print('')  
# tuple1 = (1,2,3,4,5,6,7,8,9,10)
# for num in tuple1:
#     print(num)

# print('')
# str_count = input('반복할 횟수를 입력하세요.')
# count = int(str_count)

# for i in range(count):
#     print('Hello, world!', i)

# print('')
# fruits1 = ('apple', 'orange', 'grape')
# for i in range(count):
#     for fruit in fruits1:
#         print(i, fruit)

## 구구단 출력 (단 입력받아서) 
# print('')
# str_dan = input('출력할 단을 입력하세요.')
# dan = int(str_dan)        

# print('## {} 단 ##'.format(dan))
# for i in range(1, 10):
#     print('{} * {} = {}'.format(dan, i, '%2d'%(dan * i)))

# ## 구구단 2~9단
# for dan in range(2, 10):
#     print('## {} 단 ##'.format(dan))
#     for i in range(1, 10):
#         print('{} * {} = {}'.format(dan, i, '%2d'%(dan * i)))
#     print('')

#홀수 출력 (for, continue, % 사용)
for i in range(0, 10):
    if i%2 == 0:
        continue
    else:
        print(i);