print("How old are you?",end='')
age = input()
print("How tall are you?",end='')
height = input()
print("How much do you weight?",end='')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")


#课后作业，用x = int(input())改后的。

age = int(input("How old are you?"))
height = int(input("How tall are you?"))
weight = float(input("How much do you weigh?"))  # 这里改成 float() 就能输入小数了！

print(f"So, you're {age} old, {height} tall and {weight} heavy.")
