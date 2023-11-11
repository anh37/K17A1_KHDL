a = int(input("Nhập số cần kiểm tra: "))

if a > 1:
    for i in range(2, int(a ** 0.5) + 1):
        if (a % i) == 0:
            print(f"{a} không phải là số nguyên tố.")
            break
    else:
        print(f"{a} là số nguyên tố.")
else:
    print(f"{a} không phải là số nguyên tố.")
