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