# Các số chia hết cho m từ 1 đến n
m = int(input("Nhập số tự nhiên m: "))
n = int(input("Nhập số tự nhiên n (m < n): "))
i = 1
while i <= n:
    if i % m == 0:
        print(i)
    i += 1
