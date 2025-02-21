# 建立一個空的字典
fruits = {}
print(fruits)  # 輸出: {}
# 向字典中添加鍵值對
fruits['apple'] = 10
print(fruits)  # 輸出: {'apple': 10}

# 添加更多的鍵值對
fruits['banana'] = 5
fruits['orange'] = 8
print(fruits)  # 輸出: {'apple': 10, 'banana': 5, 'orange': 8}

# 訪問字典中的值
apple_count = fruits['apple']
print(apple_count)  # 輸出: 10

# 更新字典中的值
fruits['apple'] = 15
print(fruits)  # 輸出: {'apple': 15, 'banana': 5, 'orange': 8}

# 刪除字典中的鍵值對
del fruits['banana']
print(fruits)  # 輸出: {'apple': 15, 'orange': 8}

# 檢查鍵是否存在於字典中
is_apple_in_fruits = 'apple' in fruits
print(is_apple_in_fruits)  # 輸出: True

is_banana_in_fruits = 'banana' in fruits
print(is_banana_in_fruits)  # 輸出: False