# xe 4 chỗ 
a  = int(input("Nhập loại xe = "))
b = int(input("Nhập số km = "))
c = int(input("Nhập thời gian chờ = "))

if a ==  4:
    if b <= 0.8 and b >0:
        tien_cuoc = b * 11000
    elif b >= 0 and b <= 20:
        tien_cuoc = 0.8 * 11000 + (b-0.8) * 12100
    elif b >=21:
        tien_cuoc = (b - 20) * 10000 + 19.2 * 12100 + 0.8 * 11000
if a == 7:
    if b <= 0.8 and b >0:
        tien_cuoc = b * 13000
    elif b >= 0 and b <= 30:
        tien_cuoc = 0.8 * 13000 + (b-0.8) * 13100
    elif b >=21:
        tien_cuoc = (b - 20) * 13000 + 29.2 * 14100 + 0.8 * 13000

if c <= 5:
    tien_cho = 0
else:
    tien_cho = (c - 5) * 800        



print("tiền cước chờ là : ",tien_cho ,"VND" )
print("tiền cước di chuyển la : ", tien_cuoc ,"VND")
print("tổng cước là : ", tien_cho + tien_cuoc ,"VND")
        
