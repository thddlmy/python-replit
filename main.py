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
x = list()
y = []