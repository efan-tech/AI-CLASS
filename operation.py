# these are the ages of students in 2 years 
students = [
    {"name": "Albert", "age": 20},
    {"name": "john", "age": 20},
    {"name": "frank", "age": 21},
    {"name": "suzzi", "age": 22}
]

print("Ages in 2 years:")
for s in students:
    future_age = s["age"] + 2
    print(s["name"], "will be", future_age)

students.append({"name": "john", "age": 17})
students[1]["age"] = 21
del students[2]
