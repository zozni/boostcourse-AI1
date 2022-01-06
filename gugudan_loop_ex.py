# number = 999999

# while(number != 0):
#     print("구구단 몇 단을 계산할까요(1~9)?")
#     number = int(input())

#     if number == 0 :
#         break
    
#     print(f"구구단 {number}단을 계산합니다.")

#     for i in range(1, 10):
#         result = number * i
#         print(f"{number} X {i} = {result}")

# print("구구단 게임을 종료합니다.")     ----------- 내가 한 버전


while True :
    print("구구단 몇 단을 계산할까요(1~9)?")
    dan = int(input())
    if 1 <= dan and dan <= 9 :
        print(f"구구단 {dan}단을 계산합니다.")
        for i in range(1, 10):
            result = dan * i
            print(f"{dan} X {i} = {result}")
    elif dan == 0:
        print("구구단 게임을 종료합니다.")
        break
    else:
        print("잘못 입력하셨습니다.")   # 이거는 근데 그렇게 좋은 코드가 아님.
                                       #왜냐하면 자칫 잘못하면 무한루프에 빠지게됨. 
                                       # 그래서 일반적으로 이렇게 안씀.