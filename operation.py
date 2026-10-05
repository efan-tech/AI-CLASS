# these are the ages of students in 2 years 
students = [
    {"name": "mark", "age": 22},
    {"name": "john", "age": 24},
    {"name": "paul", "age": 23},
    {"name": "george", "age": 21}
]

print("Ages in 2 years:")
for s in students:
    future_age = s["age"] + 2
    print(s["name"], "will be", future_age)

students.append({"name": "john", "age": 17})
students[1]["age"] = 21
del students[2]
