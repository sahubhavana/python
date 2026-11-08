@app.post('/create')
def create(st: Student):

    file = "student1.json"

    try:
        with open(file, "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    data.append(st.model_dump())

    with open(file, "w") as f:
        json.dump(data, f, indent=4)

    return {
        "message": "Student added successfully",
        "student_data": st
    }
