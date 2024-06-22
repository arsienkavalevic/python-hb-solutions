num = int(input())
if num // 1000 == num % 10 and num % 1000 // 100 == num % 100 // 10:
    print("YES")
else:
    print("NO")