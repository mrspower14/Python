# print(type(10))         #<class 'int'>
# print(type('hello'))    #<class 'str'>

# print('')
# print(4+10)             #14
# print(20*20)            #400
# print(1/2)              #0.5 (실수나눗셈)
# print(11//2)            #5 (정수나눗셈(몫))
# print(4**2)             #16 (누승)
# print(20%3)             #2 (나머지)

# print('')
# num=4 
# print(num)              #4
# num+=4 
# print(num)              #8
# num-=3 
# print(num)              #5
# num**=2 
# print(num)              #25
# num/=3
# print(num)              #8.333333333333334
# num//=3
# print(num)              #2.0
# num%=3
# print(num)              #2.0

# print('')
# print(5 < 6)            #True
# print(13 == 13)         #True
# print( 11 != 5)         #True
# print( 13 == 4)         #False
# print('Hello' > 'World!') #False

# print('')
# hello = 'Hello '
# hello += 'World!'
# print(hello)    #Hello World!
# hello *= 3
# print(hello)    #Hello World!Hello World!Hello World!

# print('')
# print(True and True)    #True
# print(True and False)   #false
# print(not False)        #true
# print(5<6 and True)     #true

# age = 10
# if age == 10:
#     print('10살')
#     print('입니다.')
# print('여긴 다른 블럭입니다.')

# print('')
# print('Hello world!')
# print(age)
# name = '홍길동'
# print('나의 이름은 ' + name)    #나의 이름은 홍길동
# print('나의 이름은', name)      #나의 이름은 홍길동


# print('')
# age = 20
# name='손흥민'
# print(name, age)
# print('이름은', name, '나이는', age)            #이름은 손흥민 나이는 20
# print('이름은 '+ name, '나이는 ' + str(age))    #이름은 손흥민 나이는 20

# print('')
# str1 = "{}".format(10)              #10
# print(str1)
# str2 = "{} 과 {}".format(10, 20)    #10 과 20
# print(str2)

# num1 = 10
# num2 = 20
# str3 = "{}*{}={}".format(num1, num2, num1*num2) #10*20=200
# print(str3)

# print('')
# str4 = '이름은 {} 나이는 {}'.format(name, age)     #이름은 손흥민 나이는 20
# print(str4)
# str5 = '이름은 {0} 나이는 {1}'.format(name, age)   #이름은 손흥민 나이는 20
# print(str5)
# str6 = '이름은 {1} 나이는 {0}'.format(age, name)   #이름은 손흥민 나이는 20
# print(str6)
# print('이름은 {1} 나이는 {0}'.format(age, name))   #이름은 손흥민 나이는 20

# print('')
# str7 = '이름은 {:s} 나이는 {:d}'.format(name, age)     #이름은 손흥민 나이는 20
# print(str7);
# print('pi = {:f}'.format(3.141592))         #3.141592
# print('pi = {:10f}'.format(3.141592))       #  3.141592
# print('pi = {:5.2f}'.format(3.141592))      # 3.14
# print('pi = {:.2f}'.format(3.141592))       #3.14

# print('')
# print('이름은 %s 나이는 %d'%(name, age))        #이름은 손흥민 나이는 20
# print('이름은 %s 나이는 %5d'%(name, age))       #이름은 손흥민 나이는    20    
# print('이름은 %s 나이는 %05d'%(name, age))      #이름은 손흥민 나이는 00020
# print('pi = %f'%3.141592)                   #pi = 3.141592
# print('pi = %5.2f'%3.141592)                #pi =  3.14
# print('pi = %.2f'%3.141592)                 #pi = 3.14

# print('')
# scores = [30, 50, 90, 89, 56, 87]
# score0 = scores[0]
# print(score0);      #30
# print(scores[5])    #87
# print(scores[0])    #30
# print(scores[-1])   #87
# print(scores[-3])   #89

# scores[-1] = 300
# print(scores)       #[30, 50, 90, 89, 56, 300]

# print('')
# scores.append(99)
# scores.append('Hello')
# print(scores)               #[30, 50, 90, 89, 56, 300, 99, 'Hello']

# scores.insert(1, 33)        #[30, 33, 50, 90, 89, 56, 300, 99, 'Hello']
# print(scores)
# scores.insert(2, 'World')   #[30, 33, 'World', 50, 90, 89, 56, 300, 99, 'Hello']
# print(scores)

# print('')
# list1 = [1,2,3,4,5]
# list2 = [5,6,7,8,9,10]
# print(list1 + list2)        #[1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10]
# print(list2 + list1)        #[5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]
# print(list1 * 3)            #[1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
# print(list2 * 3)            #[5, 6, 7, 8, 9, 10, 5, 6, 7, 8, 9, 10, 5, 6, 7, 8, 9, 10]

# scores = [30, 50, 90, 89, 56, 87, 45]
# length = len(scores)
# print('scores의 길이는 {}입니다.'.format(length))   #scores의 길이는 7입니다.

# bts = ['진', '슈가', '제이홉', 'RM', '지민', '뷔', '정국']
# print('bts의 멤버는 {}명 입니다.'.format(len(bts)))  #bts의 멤버는 7명 입니다.

# numbers = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# numbers1 = numbers[0:4]
# print(numbers1)         #[0, 10, 20, 30]
# print(numbers[:4])      #[0, 10, 20, 30]
# print(numbers[7:11])    #[70, 80, 90, 100]
# print(numbers[7:])      #[70, 80, 90, 100]
# print(numbers[:])       #[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# print(numbers[2:4])     #[20, 30]

# print('')
# r1 = range(1, 10 , 1)
# print(r1)               #range(1, 10)
# r2 = range(10, 20, 2)
# print(r2)               #range(10, 20, 2)
# r3 = range(10, 1)
# print(r3)               #range(10, 1)
# r4 = range(10, 0 -1)
# print(r4)               #range(10, -1)
# r5 = range(10, 0, -2)
# print(r5)               #range(10, 0, -2)

# print('')
# list1 = list(range(10))
# print(list1)                    #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# list2 = list(range(1, 10))
# print(list2)                    #[1, 2, 3, 4, 5, 6, 7, 8, 9]
# list3 = list(range(1, 10, 2))
# print(list3)                    #[1, 3, 5, 7, 9]
# list4 = list(range(10, 0, -1))
# print(list4)                    #[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# print('')
# student = ('전정국', '인공지능학과', 3, 175.3, 3.5, True);
# print(student)
# print(type(student))    #<class 'tuple'>
# print(student[0])
# #student[0] = '정국'     #error immutable 
# #print(student)

# car = ('Tesla', 'model3', 'red', 500)
# print(car)

# print('')
# range1 = range(10)
# tuple1 = tuple(range1)
# print(tuple1)           #(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# range2 = range(-5, 15, 2)
# print(tuple(range2))    #(-5, -3, -1, 1, 3, 5, 7, 9, 11, 13)

print('')
age = input('나이를 입력하시오')
print(age)
num = 3
diff = input('변화량을 입력하시오')
#print(num + diff)   #error TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(num + int(diff))  #30, 20 입력시: 23
print(age + diff)       #20, 20 입력시: 3020