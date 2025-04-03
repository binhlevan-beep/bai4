input_string = input('Nhập chuỗi các số nhị phân 4 chữ số (cách nhau bởi dấu phẩy): ')
binary_numbers = input_string.split(',')
divisible_by_5 = []
for binary in binary_numbers:
    decimal_value = int(binary, 2)
    if decimal_value % 5 == 0:
        divisible_by_5.append(binary)
print('Các số chia hết cho 5:', ','.join(divisible_by_5))
