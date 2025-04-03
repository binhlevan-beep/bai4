input_string = input('Nhập chuỗi: ')
output_string = ''.join(ch for ch in input_string if not ch.isdigit())
print('Chuỗi sau khi loại bỏ chữ số:', output_string)
