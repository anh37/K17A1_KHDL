kwh = float(input("Nhập số điện mà you đã dùng = "))

if kwh <= 50:
    tien = kwh * 1.678
elif kwh <= 100:
    tien = 50 * 1.678 + (kwh - 50) * 1.734
elif kwh <= 200:
    tien = 50 * 1.678 + 50 * 1.734 + (kwh - 100) * 2.014
elif kwh <= 300:
    tien = 50 * 1.678 + 50 * 1.734 + 100 * 2.014 + (kwh - 200) * 2.536
elif kwh <= 400:
    tien = 50 * 1.678 + 50 * 1.734 + 100 * 2.014 + 100 * 2.536 + (kwh - 300) * 2.834
else:
    tien = 50 * 1.678 + 50 * 1.734 + 100 * 2.014 + 100 * 2.536 + 100 * 2.834 + (kwh - 400) * 2.927

print("Tiền điện mà you dùng là : ",tien,"VND")
