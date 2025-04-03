# Khởi tạo số tiền thực
balance = 0

# Nhập nhật ký giao dịch từ bàn phím
print("Nhập nhật ký giao dịch (nhấn Enter để kết thúc):")
while True:
    transaction = input()
    if not transaction:  # Kết thúc khi không có đầu vào
        break
    action, amount = transaction.split()
    amount = int(amount)
    
    # Cập nhật số dư dựa trên loại giao dịch
    if action == 'D':  # Tiền gửi
        balance += amount
    elif action == 'W':  # Tiền rút
        balance -= amount

# In ra số dư cuối cùng
print('Số tiền thực của tài khoản:', balance)
