all_mb_weight = int(input())
all_mb_cost = int(input())
first_mb_cost = int(input())
second_mb_cost = int(input())

proportion = (first_mb_cost - all_mb_cost) / ((all_mb_cost - second_mb_cost) + (first_mb_cost - all_mb_cost))

print(int(all_mb_weight - (proportion * all_mb_weight)), int(proportion * all_mb_weight), sep=" ")