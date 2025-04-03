input_string = input('Nhập các từ tiếng Anh: ')
words = input_string.split()
words.sort()
print('Các từ theo thứ tự từ điển:')
for word in words:
    print(word)
