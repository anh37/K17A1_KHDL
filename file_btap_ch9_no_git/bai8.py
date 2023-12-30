def kiem_tra_so_hh(x):
    if  x  == 1:
        print(x,'là số hoàn hảo')
    else:
        list = []
        for  i in range(1,x):
            if  x % i == 0:
                list.append(i)
        if sum(list) ==  x:
            print(x,' là số hoàn hảo')
        else:
            print(x,'không phải là số hoàn hảo')

x =  int(input('nhập số nguyên x ở đây để kiểm tra có phải là số hoàn  hảo không :  '))
kiem_tra_so_hh(x)