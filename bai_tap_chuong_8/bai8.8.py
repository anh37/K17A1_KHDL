a = int(input("Nhập loại phòng cần dùng : "))
b = int(input("Nhập số đêm cần thuê : "))

if a == 1:
    if b == 1:
        tien_phong = b * 1260000
    if b == 2 or b == 3:
        tien_phong = b * 1260000 * 3/4
    if b >= 4:
        tien_phong = b * 1260000 * 0.7
    print("Loại phòng bạn đang dùng là  Standard ")    

elif a == 2:
    if b == 1:
        tien_phong = b * 1550000
    if b == 2 or b == 3:
        tien_phong = b * 1550000 * 3/4
    if b >= 4:
        tien_phong = b * 1550000 * 0.7
    print("Loại phòng bạn đang dùng là Supperior Garden View ") 

elif a == 3 :
    if b == 1:
        tien_phong = b * 1830000
    if b == 2 or b == 3:
        tien_phong = b * 1830000 * 3/4
    if b >= 4:
        tien_phong = b * 1830000 * 0.7
    print("Loại phòng bạn đang dùng là Supperior Ocean View ") 


elif a == 4:
    if b == 1:
        tien_phong = b * 1830000
    if b == 2 or b == 3:
        tien_phong = b * 1830000 * 3/4
    if b >= 4:
        tien_phong = b * 1830000 * 0.7
    print("Loại phòng bạn đang dùng là Garden View Bungalow") 

elif a == 5:
    if b == 1:
        tien_phong = b * 2120000
    if b == 2 or b == 3:
        tien_phong = b * 2120000 * 3/4
    if b >= 4:
        tien_phong = b * 2120000 * 0.7
    print("Loại phòng bạn đang dùng là Pool View Bunglaow ") 

elif a == 6:
    if b == 1:
        tien_phong = b * 2120000
    if b == 2 or b == 3:
        tien_phong = b * 2120000 * 3/4
    if b >= 4:
        tien_phong = b * 2120000 * 0.7
    print("Loại phòng bạn đang dùng là Family Room ") 

elif a == 7:
    if b == 1:
        tien_phong = b * 2540000
    if b == 2 or b == 3:
        tien_phong = b * 2540000 * 3/4
    if b >= 4:
        tien_phong = b * 2540000 * 0.7
    print("Loại phòng bạn đang dùng là Beach Front Bungalow ")         

elif a == 8:
    if b == 1:
        tien_phong = b * 4800000
    if b == 2 or b == 3:
        tien_phong = b * 4800000 * 3/4
    if b >= 4:
        tien_phong = b * 4800000 * 0.7
    print("Loại phòng bạn đang dùng là VIP sea View ") 

elif a > 8:
    print(" HIỆN CHÚNG TÔI CHƯA CÓ LOẠI PHÒNG BẠN ĐANG YÊU CÂU")

print("Số tiền phải trả là :", tien_phong , "VND")
