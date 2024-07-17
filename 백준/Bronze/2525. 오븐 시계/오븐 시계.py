hour, min_ = map(int, input().split())
cook_min = int(input())

hour += cook_min//60
min_ += cook_min%60

if min_ >= 60:
    hour += 1
    min_ -= 60

if hour > 23:
    hour -= 24

print(hour, min_)