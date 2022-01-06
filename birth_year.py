print("당신이 태어난 년도를 입력하세요")
year = int(input())
age = 2021 - year + 1

if age <= 26 and 20 <= age:
    print("대학생")
elif age <= 20 and 17 <= age:
    print("고등학생")
elif age <= 17 and 14 <= age:
    print("중학생")
elif age <= 14 and 8 <= age:
    print("초등학생")
else:
    print("학생이 아닙니다.")
