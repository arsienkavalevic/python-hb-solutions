name_one = input()
name_two = input()
name_three = input()

if name_three > name_one < name_two:
    print(name_one)
elif name_one > name_two < name_three:
    print(name_two)
else:
    print(name_three)