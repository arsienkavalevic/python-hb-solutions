number_one = int(input())
number_two = int(input())
first = ((number_one % 10) + (number_two % 10)) % 10
second = ((((number_one // 10) % 10) + ((number_two // 10) % 10)) % 10) * 10
third = (((number_one // 100) + (number_two // 100)) % 10) * 100

result = first + second + third
print(result)