import mod1

num1 = 10
num2 = 5

result = mod1.add(num1, num2)

print(result)

a = int(input("첫번째 숫자: "))
b = int(input("두번째 숫자: "))
print ("1. 더하기 2. 빼기")
c = int(input("선택"))
if c == 1:
    print (mod1.add(a, b))
if c == 2:
    print (mod1.sub(a, b))
