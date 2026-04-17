# def add(x, y):
#     return x + y

# f = lambda x, y: x + y

# print(add(1,2))
# print(f(1,2))

# f = lambda x: x if x % 3 == 0 else 0    #나머지가0이면 x반환 아니면 0반환 
# print(f(3))
# print(f(6))
# print(f(4))

# print('')
# nums = [1,2,3,4,5]
# def pow(x):
#     return x ** 2
# f = lambda x: x ** 2
# print(nums)
# print(map(pow, nums))
# print(list(map(pow, nums)))
# print(list(map(f, nums)))
# print(list(map(lambda x: x ** 2, nums)))

# print('')
# nums1 = [1,2,3,4,5]
# nums2 = [6,7,8,9,10]
# print(list(map(lambda x, y: x * y, nums1, nums2)))

# # 5배 구하기 실습
# num = list(range(1, 10))
# print(list(map(lambda x: x*5, num)))

# ages = [18, 19, 39, 12, 43, 13, 21, 25]
# def adult_func(age):
#     if age>= 19:
#         return True
#     else:
#         return False

# for age in filter(adult_func, ages):
#     print(age)
# print()

# for age in filter(lambda age: age >= 19, ages):
#     print(age)

# print()
# adult_ages = list(filter(lambda age: age >= 19, ages))
# print(adult_ages)

# #실습 filter, map 사용하기 
# nums = list(range(1, 11))
# numeven = list(filter(lambda x: x % 2 == 0, nums))
# print(numeven)
# numdouble = list(map(lambda x: x ** 2, numeven))
# print(numdouble)
# numlambda = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, nums)))
# print(numlambda)
#############################################
# from functools import reduce 

# nums = list(range(1, 5))
# sum = reduce(lambda x, y: x+y, nums)
# print(sum)

# mul = reduce(lambda x, y: x*y, nums)
# print(mul)

#############################################
# #실습 lamba, filter, reduce 사용 
# from functools import reduce 

# nums = list(range(1, 11))
# numeven = filter(lambda x: x % 2 == 0, nums)
# print(numeven)
# mul = reduce(lambda x, y: x*y, numeven)
# print(mul)
# nummul = reduce(lambda x, y: x*y, filter(lambda x: x%2 == 0, nums))
# print(nummul)

# #list 축약표현 [표현식 for 변수 in 리스트]
# list1 = list(range(1, 10))

# list2 = list(map(lambda x: x**2, list1))
# print(list2)

# list3 = [x ** 2 for x in list1]
# print(list3)

# list4 = [x ** 2 for x in range(1,10)]
# print(list4)

# list5 = [x ** 2 for x in list1 if x > 5]
# print(list5)

# list6 = [x ** 2 for x in range(1, 10) if x%2 == 0]
# print(list6)

# lambda 실습
# 1~10까지 숫자의 제곱 
list1 = [x ** 2 for x in range(1, 11)]
print(list1)
# 1~20까지 짝수 
list2 = [x for x in range(1, 21) if x%2 == 0]
print(list2)
# 1~20까지 3의 배수 
list3 = [x for x in range(1, 21) if x%3 == 0]
print(list3)
# 1~20까지 숫자중 5의 배수의 제곱 
list4 = [x ** 2 for x in range(1, 21) if x%5 == 0]
print(list4)
