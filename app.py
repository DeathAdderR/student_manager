
from flask import Flask, request, jsonify, render_template
from tables import StudentTable

app = Flask(__name__)
db = StudentTable()



app.route('/') # main route to serve the HTML file

def index():
    return render_template('index.html')



@app.route('/add_student', methods=['POST'])

def add_student():
    data = request.get_json()

    student_name = data.get('student_name')
    student_age = data.get('student_age')
    student_grade = data.get('student_grade')

    db.execute_query('''INSTERT INTO student_manager (student_name, student_age, student_grade)''', (student_name, student_age, student_grade,))

    return jsonify({"message": "Student added"})




@app.route('/update_student_grade', methods=['POST'])

def update_student_grade():
    data = request.get_json()
    student_id = data.get('student_id')
    student_grade = data.get('student_grade')

    if student_id is None:
        return jsonify({"message": "No student_id provided"})
    db.execute_query('''UPDATE student_manager SET student_grade = ? WHERE student_id = ?''', (student_grade, student_id))

    return jsonify({"message": f"Student: {student_id} grade changed to {student_grade}"}), 200



@app.route('/update_student_age', methods=['POST'])

def update_student_age():
    data = request.json()
    student_id = data.get('student_id')
    student_age = data.get('student_age')

    if student_id is None:
        return jsonify({"message": "No student_id provided"})
    db.execute_query('''UPDATE student_manager SET student_age = ? WHERE student_id = ?''', (student_age, student_id))



@app.route('/view_all_students', methods=['GET'])

def view_all_students():
    students = db.execute_query('''SELECT * FROM student_manager''')

    if students:
        return jsonify(students), 200
    else:
        return jsonify([]), 200
    


@app.route('/view_student', methods=['GET'])

def view_student():
    data = request.get_json()
    student_id = data.get('student_id')

    if student_id is None:
        return jsonify({"message": "Student Id not found"}), 400
    
    db.execute_query('''SELECT * FROM student_manager WHERE student_id = ?''', (student_id,))


if __name__ == '__main__':
    app.run(debug=True)
    db.close_connection()
