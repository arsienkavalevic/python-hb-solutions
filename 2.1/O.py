hours = int(input())
minutes = int(input())
time = int(input())

print(f"{((hours + ((time + minutes) // 60)) % 24):0>2}:{((time + minutes) % 60):0>2}")