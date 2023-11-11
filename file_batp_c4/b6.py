
# Giải hệ phương trình bậc nhất ax + b = 0
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))

if a == 0:
    if b == 0:
        print("Phương trình vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
else:
    x = -b / a
    print(f"Nghiệm của phương trình là x = {x}")
