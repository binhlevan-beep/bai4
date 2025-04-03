even_digit_numbers = []
for num in range(1000, 3001):
    str_num = str(num)
    if all(int(digit) % 2 == 0 for digit in str_num):
        even_digit_numbers.append(str_num)
print(', '.join(even_digit_numbers))
