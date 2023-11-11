def e_mu_x(x, n):
    result = 1
    for i in range(1, n):
        result += (x ** i) / (1 if i == 0 else i)
    return result

x_value = 2  # Giá trị x cần tính
n_value = 10  # Số lượng phần tử trong chuỗi

result = e_mu_x(x_value, n_value)
print(f"e^{x_value} dựa trên chuỗi Taylor với {n_value} phần tử là: {result}")
