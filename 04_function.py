# # 함수 정의
# def hello():
#     print('Hello World!')

# hello()

# # 가변 매개변수 사용
# def hello4(greeting, *names):
#     for name in names:
#         print(greeting, name)

# hello4('안녕', '진', '슈가', '제이홉', 'RM', '지민', '뷔')        

# # 함수 호출시 매개변수명 사용
# def function(first, second, third):
#     return first - second + third

# print(function(3, 5, 7))
# print(function(first=3, second=5, third=7))
# print(function(second=5, third=7, first=3))

# # 함수 매개변수명의 기본값 설정
# def function1(first=1, second=3, third=5):
#     return first+second+third
# print(function1())              #9
# print(function1(first=3))       #11
# print(function1(10, 10))        #25
# print(function1(first=10, third=10))#23

# print('')
# def function2(first, second, third=5):
#     return first+second+third
# print(function2(1,2,3))                 #6
# print(function2(first=1, second=2))     #8
# print(function2(1, second=5))           #11
# print(function2(second=5, first=2))     #12


##반환형이 콜렉션일때 unpacking
# def function3():
#     return 1, "Hello", True
# a, b, c = function3()
# print(a,b,c)        #1 Hello True
# a=function3()
# print(a)            #(1, 'Hello', True)
# print(type(a))      #<class 'tuple'>

# #반환형이 리스트일때 unpacking
# def ret_list():
#     return [1,2]
# l = ret_list()
# print(l)                #[1, 2]
# print(l[0])             #1
# n1, n2 = ret_list()
# print(n1, n2)           #1 2
# n1, _ = ret_list()
# print(n1)               #1

# #젯수와 피젯수 튜플로 반환하는 함수 만들기 
# def divide(num1, num2):
#     q = num1 // num2
#     r = num1 % num2
#     return (q, r)
# rtn = divide(15, 4)
# print(rtn)
# print(divide(25,6))

# print('')
# def divide(*num):
#     q = num[0] // num[1]
#     r = num[0] % num[1]
#     return (q, r)
# rtn = divide(15, 4)
# print(rtn)
# print(divide(25,6))