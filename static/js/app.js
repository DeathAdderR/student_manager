
async function addStudent(event) {
    event.preventDefault()

    const studentName = event.target.student_name.value;
    const studentAge = event.target.student_age.value;
    const studentGrade = event.target.student_grade.value;

    if (!studentName || !studentAge || !studentGrade) {
        alert("Please fill in all fields to add a student.")
        return
    }

    const response = await fetch('/add_student', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            name: studentName,
            age: studentAge,
            grade: studentGrade
        })
    });

    const result = await response.json()
    alert(result.message)
    await viewAllStudents()
}

async function updateStudentGrade(event) {
    event.preventDefault()
    const studentId = event.target.student_id.value
    const newStudentGrade = event.target.new_grade.value

    if (!studentId || !newStudentGrade) {
        alert("Provide a valid student ID")
        return;
    }

    const response = await fetch('/update_student_grade', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            id: studentId,
            grade: newStudentGrade
        })
    })

    const result = await response.json()
    alert(result.message);
    await viewAllStudents()
}

async function updateStudentAge(event) {
    event.preventDefault()
    const studentId = event.target.student_id.value
    const newStudentAge = event.target.new_age.value

    if (!studentId || !newStudentAge) {
        alert("Provide a student ID and student Age")
        return
    }

    const response = fetch('/update_student_age', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            id: studentId,
            grade: newStudentAge
        })
    })

    const result = await response.json()
    alert(result.message)
    await viewAllStudents()
}

async function viewAllStudents() {
    const response = await fetch('/view_students', {
        method: 'GET',
        headers: {'Content-Type': 'application/json'}
    });

    const students = await response.json()
}

async function viewStudent(event) {
    event.preventDefault()
    const studentId = event.target.student_id.value;

    if(!studentId) {
        alert('Please provide a student ID.')
        return
    }

    const response = await fetch(`/view_student/${studentId}`, {
        method: 'GET',
        headers: {'Content-Type': 'application/json'}
    });

    const student = await response.json();
}

document.addEventListener("DOMContentLoaded", () => {

    const updateAgeForm = document.getElementById('update-age')
    const updateGradeForm = document.getElementById('update-grade')
    const addStudentForm = document.getElementById('add-student')

    updateAgeForm.addEventListener('submit', updateStudentAge)
    updateGradeForm.addEventListener('submit', updateStudentGrade)
    addStudentForm.addEventListener('submit', addStudent)

})
