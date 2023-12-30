def tinh_a(n,x):
    A = ((x**2 +x + 1)** n  )+ ((x**2 -x+ 1)**n)
    print('a theo x và n là :',A)
    return A
n =  int(input(' nhập n ở đây :'))
x  =  int(input('nhập x ở đây :'))
tinh_a(n,x)