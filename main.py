start=1

#####LEC 1#####
print("[LEC %d]" %(start));
print("Hello World")

start+=1

#####LEC 2#####
print("[LEC %d]" %(start));
# 캐스팅
print("너 혹시 몇살이야?"+str(24))

# boolean
x= True
y = False

# 조건문
if 2 > 1 and 3 > 1:
  print("hello!")

if not 2 < 1:
  print("hello~")

x = 3;
if x > 2:
  print("hello~!")
else :
  print("hi~!")

# function

def chat(name1, name2, age):

  print("%s: 안녕? 몇살이니" %name1)
  print("%s: 나? %d!" %(name2, age))

# 반복은 너무 귀찮다.. 더럽다..!

chat("알렉스", "윤하", 20)
chat("철수","영희", 30)

# 다른 이름으로 쓰고 싶으면..? -> 함수인자 / return는 결과값

# 인사 함수
# 이름과 나이를 받고
# 나이 : 10미만->안녕 10<나이<20 -> 안녕하세요 그 외 -> 안녕하십니까

def sayHello(name, age):
  if age<10:
    print("안녕"+name)
  elif age > 10 and age < 20:
    print("안녕하세요 "+name)
  else:
    print("안녕하십니까 "+name)

sayHello("송이", 24)
sayHello("주상", 12)

start+=1

#####LEC 3#####
print("[LEC %d]" %(start))
# for문 & while
for i in range(10):
  print("주상아메이플재밌어?")

i=0
while True:
  print("주상아메이플재밌어?")
  print(i)
  i+=1

  if(i==5):
    break
  # 기타등등 break, continue

start+=1

#####LEC 4#####
print("[LEC %d]" %(start))

#리스트 (아래 x와 y는 의미가 같은 문장)
x = [1, 5, 3, 4]
y = ["hello", "World"]
z = ["hello", 1, 2, 3]
#마구마구 타입들이 섞여도된다

print(len(x))
print(sorted(x))

for n in x:
  print(n)

for n in y:
  print(n)

print(x.index(3))
print("hello" in y)

#튜플 (둘은 같은 표현)
tuple1 = tuple()
tuple2 = ()

x = (1,2,3)
y = ('a','b','c')

#x[0] = 10 튜플은 값 못바꾼다

# 딕셔너리 (key와 value로 이루어져있다)
dic1 = dict()
dic2 = {}

x = {
  "name": "송이",
  1: 24
}

print(x["name"])
print(x[1])
print(x.keys())
print(x.values())

for key in x:
  print(key)
  print(x[key])


# mini project

fruit = ["사과", "사과", "바나나", "바나나", "딸기", "키위", "복숭아", "복숭아", "복숭아"]

d = {}

for f in fruit:
  if f in d:
    d[f]+=1
  else:
    d[f]=1

print(d)

start+=1
  
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