from flask import Flask, request, jsonify

app = Flask(__name__)

students = [
    {'id': 1, 'name': 'Yugam', 'age': 21},
    {'id': 2, 'name': 'Shivam', 'age': 23}
]

@app.route('/students', methods=['GET'])
def getStudents():
    return jsonify(students)

@app.route('/students', methods=['POST'])
def addStudent():
    data = request.get_json()
    data['id'] = len(students)+1
    students.append(data)
    return jsonify(data), 201

@app.route('/students/<int:id>', methods=['PUT'])
def updateDetails(id):
    newData = request.get_json()
    for student in students:
        if student['id'] == id:
            student.update(newData)
            return jsonify(student), 200

    return jsonify({'error': 'Student not found'}), 404

@app.route('/students/<int:id>', methods=['DELETE'])
def deleteStudent(id):
    for student in students:
        if student['id'] == id:
            students.remove(student)
            return jsonify({"message" : "Student deleted"}), 200

    return jsonify({'error': 'Student not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)