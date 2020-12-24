#####LEC 5#####

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def say_hello(self, to_name):
    print("안뇽~ "+to_name+" 난 "+self.name)

  def introduce(self):
    print("내 이름은" + self.name + "그리고 나는 "+ str(self.age)+"살이야")
  
songyi = Person("송이",20)
songyi.say_hello("주상")
songyi.introduce()

class Police(Person):
  def arrest(self, to_arrest):
    print("넌 체포됐다 " + to_arrest)
  
class Programmer(Person):
  def program(self, to_program):
    print("다음엔 뭘 만들지? 아! 이거 "+to_program)

joosang = Person("주상", 24)
lily = Police("릴리", 24)
alex = Programmer("알렉스", 20)

joosang.introduce()
lily.introduce()
alex.introduce()

lily.arrest("주상")
alex.program("릴리")

start+=1

#####LEC 6#####
#라이브러리 = 파이썬의 패키지
#모듈 == 코드가 들어있는 파일

from animal import dog # animal 패키지안에 dog을 가져와죠
from animal import cat

d = dog.Dog()
c= cat.Cat()

d.hi()
c.hi()

from animal import *

dd = Dog()
cc = Cat()

dd.hi()
cc.hi()