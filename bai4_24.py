# Nhập câu từ bàn phím
input_string = input('Nhập một câu: ')

# Khởi tạo biến đếm
uppercase_count = 0
lowercase_count = 0

# Duyệt qua từng ký tự trong câu
for char in input_string:
    if char.isupper():  # Kiểm tra xem ký tự có phải là chữ hoa không
        uppercase_count += 1
    elif char.islower():  # Kiểm tra xem ký tự có phải là chữ thường không
        lowercase_count += 1

# In ra kết quả
print('Chữ hoa:', uppercase_count)
print('Chữ thường:', lowercase_count)
