a = float(input("Lãi suất 1 năm (%) ="))
b = float(input("Số tiền gửi = "))
c = float(input("Số tháng gửi = "))
laix = (b * c) * (a / 12)# tính lãi
so_tien_nhan = b + laix # tiền nhận đc
print("tiền lãi : ",laix)
print("tiền nhận được là :",so_tien_nhan )