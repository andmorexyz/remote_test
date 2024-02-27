age=input("年齢を打ち込んでください:")
int_age=int(age)
if int_age < 21:
    print("「あなたは若いですね!」")
elif int_age > 21:
    print("「老けてますね笑」")
else:
    print("半角数字で入力してください！")
