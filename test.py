

query = "SELECT FROM student_manager student_id WHERE student_id = ?"
query = query.strip().lower().startswith('select')

print(query)
