#Bội số chung nhỏ nhất 

def uoc_so_chung_lon_nhat(a, b):
    while b:
        a, b = b, a % b
    return a

a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
bcnn = (a * b) // uoc_so_chung_lon_nhat(a, b)
print(f"BCNN của {a} và {b} là {bcnn}")
