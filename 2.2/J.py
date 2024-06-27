num = int(input())
first_digit = num // 100 + num // 10 % 10
second_digit = num % 10 + num // 10 % 10
if first_digit < second_digit:
    print(str(second_digit) + str(first_digit))
else:
    print(str(first_digit) + str(second_digit))