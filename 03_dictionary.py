# #1.dictionary
# dic1 = {}
# print(dic1)
# dic2 = dict()
# print(dic2)
# dic3 = {'name':'item', 1:3.5, False:[1,2,3]}
# print(dic3)
# print(dic3['name'])
# print(dic3[1])
# dic4 = dict(name = '홍길동', height = 180, age = 20)
# print(dic4)
# print(dic4['name'])

# print()
# student = {'name':'홍길동', 'major':'정통과', 'score':3.5}
# print(student['name'])
# print(student['score'])
# scores = {1:3.5, 2:4.0, 3:4.3, 4:4.2}
# print(scores[1])
# print(scores[2])
# student['major'] = '정보통신과'
# print(student)
# student['grade'] = 4
# print(student)
# scores[2] = '4.5'
# scores[5] = 5.0
# print(scores)

# del student['name']
# print(student)
# del scores[1]
# print(scores)

# #dictionary Key, Value 가져오기 
# print()
# student = {'name':'홍길동', 'major':'정통과', 'score':3.5}
# print(student.items())          #dict_items([('name', '홍길동'), ('major', '정통과'), ('score', 3.5)])
# print(student.keys())           #dict_keys(['name', 'major', 'score'])
# print(student.values())         #dict_values(['홍길동', '정통과', 3.5])
# print()
# print(list(student.items()))    #[('name', '홍길동'), ('major', '정통과'), ('score', 3.5)]
# print(list(student.keys()))     #['name', 'major', 'score']
# print(list(student.values()))   #['홍길동', '정통과', 3.5]

# #Set (중복없음, 순서없음)
# set1 = set([0,1,2,3,4,5,6])
# set2 = set([4,5,6,7,8,9,10])
# print(set1 & set2)              #교집합 {4, 5, 6}
# print(set1.intersection(set2))  #교집합 {4, 5, 6}
# print(set1 | set2)              #합집합 {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# print(set1.union(set2))         #합집합 {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# print(set1 - set2)              #차집합 {0, 1, 2, 3}
# print(set1.difference(set2))    #차집합 {0, 1, 2, 3}


# #packing, unpacking
# nums = 1,2,3
# print(nums)             #packing
# print(type(nums))
# num1, num2, num3 = nums #unpacking
# print(num1, num2, num3) 

# print('')
# nums = [1,2,3,4,5]      #list
# print(type(nums))
# num1, num2, num3, num4, num5 = nums
# print(num1, num2, num3, num4, num5)
# num1, num2, *num3 = nums
# print(num1, num2, num3)
# *num1, num2, num3 = nums
# num3 = ''
# print(num1, num2, num3)
# num1, num2, _, _, _ = nums
# print(num1, num2, num3)

# print('')
# student = {'name':'홍길동', 'major':'정통과', 'grade':3}
# a, b, c = student
# print(a, b, c)          #name major grade (키값이 나온다)
# set1 = {1,2,3,4}
# a, *b, c = set1
# print(a, b, c)          #1 [2, 3] 4

