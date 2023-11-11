a = 13850
so_to_500 = a // 500
if so_to_500 > 0:
    print("Số tờ 500:", so_to_500)
    tien_thua_500 = a - so_to_500 * 500

so_to_200 = tien_thua_500 // 200
if so_to_200 > 0:
    print("Số tờ 200:", so_to_200)
    tien_thua_200 = tien_thua_500 - so_to_200 * 200

so_to_100 = tien_thua_200 // 100
if so_to_100 > 0:
    print("Số tờ 100:", so_to_100)
    tien_thua_100 = tien_thua_200 - so_to_100 * 100

so_to_50 = tien_thua_100 // 50
if so_to_50 > 0:
    print("Số tờ 50:", so_to_50)
