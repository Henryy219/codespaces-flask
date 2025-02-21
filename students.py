import json

# 讀取 JSON 檔案
with open('students.json', 'r') as file:
    data = json.load(file)

# 檢查讀取的資料
print(data)

# 訪問 JSON 資料中的列表
students = data['students']
print(students)

# 遍歷列表中的每個學生
for student in students:
    print(f"ID: {student['id']}")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Grades: {student['grades']}")
    print()

# 計算每個學生的平均成績
for student in students:
    grades = student['grades']
    average_grade = sum(grades.values()) / len(grades)
    print(f"Name: {student['name']}, Average Grade: {average_grade}")

