a = int(input("Nhập năm ="))
if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
    print(a , "Là năm nhuận")
else: print(a, " Không phải là năm nhuận")