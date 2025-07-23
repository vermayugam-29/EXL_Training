import json

student = {
    'name' : 'Tanmay',
    'age' : 23,
    'subjects' : ['Python', 'Java','CN'],
    'marks' : [67,56,69]
}

with open('student.json', 'w') as file:
    json.dump(student, file)

with open('student.json', 'r') as file:
    data = json.load(file)

print("Student Data:")
print("Name =", data['name'])
print("Age =", data['age'])
print("Subjects =", data['subjects'])
print("Marks =", data['marks'])
