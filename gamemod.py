def step():
    print ("1. 주먹으로 때린다")
    print ("2. 발로 찬다")
    print ("3. 머리로 박는다")
    print ("4. 도구를 쓴다")
    b = input("선택: ")
    if b == "1":
        print("몬스터가 데미지를 입었다")
    elif b== "4":
        print ("1. 어떤 도구")
        print ("2. ??")
        print ("3. ???")
        c = input ("선택: ")
        if c == "1":
            print ("터진다")
        elif c == "2":
            print ("소용없다")
        else :
            print ("효과 있다")
    else:
        print ("피했다")

def step2():
    print ("도망간다")