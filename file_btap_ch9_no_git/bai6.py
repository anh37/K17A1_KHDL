def kiem_tra_so_nt(x):
    if x <2:
        print('x k phải là số nguyên tố ')
    else:
        for  i  in range(2,x):
            nt =  True
            if x % i ==0:
                nt =  False
                break
        if nt :
            print('True ')
        else:
            print('False')

x =  int(input('nhập x ở đây để kiểm tra : '))
kiem_tra_so_nt(x)
