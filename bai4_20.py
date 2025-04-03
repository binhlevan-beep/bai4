def pascal_triangle(n):
    triangle = []
    
    for i in range(n):
        # Khởi tạo dòng mới với 1
        row = [1] * (i + 1)
        # Tính toán các giá trị trong dòng
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    
    return triangle

# Nhập số dòng n từ bàn phím
n = int(input('Nhập số dòng n: '))

# Tạo và in tam giác Pascal
triangle = pascal_triangle(n)
for row in triangle:
    print(' '.join(map(str, row)))
