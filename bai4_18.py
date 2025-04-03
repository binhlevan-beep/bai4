# Nhập số nguyên n từ bàn phím
n = int(input('Nhập số nguyên n: '))

# Tạo danh sách các số Fibonacci nhỏ hơn n
fibonacci_numbers = []
a, b = 0, 1

while a < n:
    fibonacci_numbers.append(a)
    a, b = b, a + b  # Cập nhật giá trị của a và b

# In ra danh sách các số Fibonacci
print('Các số Fibonacci nhỏ hơn', n, ':', fibonacci_numbers)
