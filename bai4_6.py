full_name = input('Nhập tên người: ')
parts = full_name.split()
if len(parts) >= 2:
    last_name = parts[0]  
    first_name = parts[1]  
else:
    last_name = full_name  
    first_name = ''
print('Họ:', last_name)
print('Tên riêng:', first_name)
