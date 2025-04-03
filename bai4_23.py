# Nhập câu từ bàn phím
input_string = input('Nhập một câu: ')

# Khởi tạo biến đếm
letter_count = 0
digit_count = 0

# Duyệt qua từng ký tự trong câu
for char in input_string:
    if char.isalpha():  # Kiểm tra xem ký tự có phải là chữ cái không
        letter_count += 1
    elif char.isdigit():  # Kiểm tra xem ký tự có phải là chữ số không
        digit_count += 1

# In ra kết quả
print('Số chữ cái là:', letter_count)
print('Số chữ số là:', digit_count)
