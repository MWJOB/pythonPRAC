from random import*


print("값을 입력해주십시오")
a = int(input())
c = 0

print(str(a) + "%의 확률의 강화 시뮬레이션입니다.")

while True:
    b = (int(randint(1, 101)))
    if a >= b:
        print("성공")
        print(str(c) + "만큼 시도하여 성공하셨습니다!")
        print(b)
        break
    else:
        print("실패")
        c = c+1
