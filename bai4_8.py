words = input('Nhập dãy các từ: ').split()

# Tìm độ dài lớn nhất
max_length = max(len(word) for word in words)

# Tìm tất cả các từ có độ dài bằng max_length
longest_words = [word for word in words if len(word) == max_length]

# In ra kết quả
print ('Từ dài nhất (hoặc các từ dài nhất):', ', '.join(longest_words))