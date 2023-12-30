# tính chỉ sô bmi
def tinh_bmi(chieu_cao, can_nang):
    bmi = can_nang/(chieu_cao * chieu_cao)
    print("Chỉ số bmi của bạn là: ",bmi)
    return bmi
# gọi hàm
chieu_cao = float(input("Nhập chiều cao (m) : "))
can_nang = float(input("Nhập cân nặng (kg) : "))

bmi = tinh_bmi(chieu_cao, can_nang)

# đánh giá
if bmi < 18.5:
    print("Gầy")
elif 18.5 <= bmi < 24.9:
    print("Bình thường")
else:
    print("Béo phì")