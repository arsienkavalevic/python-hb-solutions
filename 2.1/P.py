stock_km = int(input())
mall_km = int(input())
speed = int(input())
distance = mall_km - stock_km
print(f"{(distance / speed):.2f}")