from datetime import datetime
day   =   int(input('nhập ngày ở đây : '))
thang  =  int(input('nhập tháng ở đây :'))
year  =  int(input('nhập năm ở đây :'))

date = datetime(year, thang, day)

print('ngày tháng năm bạn vừa nhập là :',day,'-',thang,'-',year)


if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year,'là năm nhuận ')
    if thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12:
        print('tháng ',thang,'có 31 ngày ')
    elif thang == 2:
        print('tháng 2 có 29 ngày ')
    else:
        print('tháng ',thang,'có 30 ngày ')
else:
    print(year,'kp là năm nhuận ')
    if thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12:
        print('tháng ',thang,'có 31 ngày ')
    elif thang == 2:
        print('tháng 2 có 28 ngày ')
    else:
        print('tháng ',thang,'có 30 ngày ')

thuw =  date.weekday()
thuws  =  ['Thứ 2','Thứ 3','Thứ 4','Thứ 5','Thứ 6','Thứ 7','Chủ Nhật']
thuw_name =  thuws[thuw]
print(day,'-',thang,'-',year,'là :',thuw_name)