input_string = input('Nhập các số nhị phân (cách nhau bởi dấu phẩy): ')
binary_numbers = input_string.split(',')
print('Các số nhị phân đã nhập:')
for binary in binary_numbers:
    print(binary.strip())  
