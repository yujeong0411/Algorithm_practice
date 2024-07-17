total_price = int(input())
buy = int(input())

sum_ = 0          # 물건 값 합계
for i in range(buy):
    a_price, b_buy = map(int, input().split())
    sum_ += a_price*b_buy

if sum_ == total_price:
    print("Yes")
else:
    print("No")