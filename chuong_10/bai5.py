while True:
    try:
        a  =  input('nhập chuỗi để kiểm tra zip code ở đây :')
        if  a.isdigit():
           if len(a) == 6:
            print('True')
           else:
            print('Fasle')
        else:
           print('chỉ nhập chuỗi toàn số ')
    except ValueError:
       print('chỉ nhập số nguyên ')









