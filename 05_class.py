# #클래스의 정의
# class Person:
#     def hello(self):
#         print('Hello')

# person = Person()
# person.hello()
# person1 = Person()
# person1.hello()
# print('')

# #속성 정의
# class Person:
#     def __init__(self): #생성자 __init__ == js의 constructor
#         self.hi = 'Hello'
#         self.hh = 'HH'
#     def hello(self):
#         print(self.hi)
# person = Person()
# person.hello()
# print(person.hi)
# print(person.hh)
# print('')

# # #속성 정의와 초기화
# class Person:
#     def __init__(self, n, a):
#         self.name = n
#         self.__age = a

#     def hello(self):
#         print('Hello {}'.format(self.name))
#         print('당신은 {}살 입니다.'.format(self.__age))

# person = Person('홍길동', 20)
# person.hello()
# #print(person.age)  #오류
# #print(person.__age)#오류
# person.__age=30     #오류 없지만 값은 변하지 않는다.
# person.hello()

# #클래스 정의 실습 (학생클래스  '몇학년 몇반 누구입니다.'->introduce)
# class Student:
#     def __init__(self, grade, classno, name):
#         self.grade = grade
#         self.classno = classno
#         self.name = name

#     def introduce(self):
#         print('{}학년 {}반 {} 입니다.'.format(self.grade, self.classno, self.name))
# student = Student(3, 2, '홍길동')
# student.introduce()        

# #비공개 속성 정의
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         if 0 <= age <= 20: 
#             self.__age = age
#         else:
#             self.__age = 0
    
#     def inc_age(self):
#         self.__age += 1
#     def info(self):
#         print(self.__age)

# person = Person('홍길동', 33)
# person.inc_age()
# person.info()        

# #클래스 속성 사용
# class Person:
#     count = 0

#     def __init__(self, name):
#         self.name = name
#         Person.count += 1

# person1 = Person('홍길동')
# print(person1.count)        #1
# person1 = Person('허균')
# print(person1.count)        #2


# #정적 메서드 사용
# class Math:
#     @staticmethod
#     def add(a, b):
#         return a+b
#     @staticmethod
#     def sub(a, b):
#         return a-b
# print(Math.add(4,5))
# print(Math.sub(9,5))

# #사각형을 관리하는 클래스
# class Rectangle:
#     def __init__(self, w, h):
#         self.width = w
#         self.height = h
#     def area(self):
#         return self.width * self.height
#     def getDouble(self):
#         self.width *= 2
#         self.height *= 2
# rect = Rectangle(4,5)
# print(rect.area())
# rect.getDouble()
# print(rect.width, rect.height)
# print(rect.area())

#클래스의 상속
class Vehicle:
    def __init__(self, speed):
        self.speed = speed
    def speed_up(self):
        self.speed += 10
    def speed_down(self):
        self.speed -= 10

class Car(Vehicle):
    def __init__(self, speed, wheels, seats):
        Vehicle.__init__(self, speed)
        self.wheels = wheels
        self.seats = seats

    def info(self):
        print("Car:", self.speed, self.wheels, self.seats)

# car = Car(100, 4, 5)
# car.speed_up()
# car.info()
# car.speed_up()
# car.info()
# car.speed_down()
# car.info()

#클래스 상속 실습
class Truck(Car):
    def __init__(self, speed, wheels, seats, loadage):
        Car.__init__(self, speed, wheels, seats)
        self.loadage = loadage

    def load(self):
        print("load")

    def unload(self):
        print("unload")
    
    def info(self):
        print("Truck:", self.speed, self.wheels, self.seats, self.loadage)

truck = Truck(100, 8, 2, 50)
truck.load()
truck.unload()
truck.speed_up()
truck.info()
truck.speed_down()
truck.info()        

car = Car(150, 4, 2)
car.speed_up()
car.speed_up()
car.speed_up()
car.speed_up()
car.speed_up()
car.info()