# Tính tổng các chữ số của một số nguyên N
N = int(input("Nhập số nguyên N: "))
tong = 0
while N != 0:
    digit = N % 10
    tong += digit
    N //= 10
print(f"Tổng các chữ số của {N} là {tong}")
