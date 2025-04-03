# Nhập chuỗi các số từ bàn phím
input_string = input('Nhập các số (cách nhau bởi dấu phẩy): ')

# Tách chuỗi thành danh sách các số và chuyển đổi thành kiểu int
numbers = [int(num.strip()) for num in input_string.split(',')]

# Lọc các số lẻ
odd_numbers = [num for num in numbers if num % 2 != 0]

# In ra các số lẻ, phân tách bởi dấu phẩy
print('Các số lẻ:', ','.join(map(str, odd_numbers)))
