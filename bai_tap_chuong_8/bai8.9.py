n = int(input("Nhập một số nguyên: "))

if n < 0:
    print("Vui lòng nhập một số nguyên dương.")
else:
    while n >= 0:
        print(n)
        n -= 1
