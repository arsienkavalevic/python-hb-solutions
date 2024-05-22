n = int(input())
f = ((n // 100) % 10) * 1000
s = (n // 1000) * 100
t = (n % 10) * 10
c = (n // 10) % 10
result = f + s + t + c
print(result)