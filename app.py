from flask import Flask,request

app = Flask(__name__)
students = [
    {"id": 1, "name": "Adithya"},
    {"id": 2, "name": "Vijju"}
]

@app.route("/")
def home():
    return "Student Management API Running"

@app.route("/students")
def get_students():
    return students

@app.route("/student/<int:id>")
def get_student(id):
    if id ==1:
        return{"id":1,"name":'Adithya'}
    elif id ==2:
        return{"id":2,"name":"Vijju"}
    return{"Message":"Student not Found"}

@app.route("/add_student",methods =['POST'])
def add_student():
    data = request.get_json()
    students.append(data)
    return {
        "Message":"Student Added",
        "Student": data
    }

@app.route('/update_student/<int:id>', methods=['PUT'])
def update_student(id):

    data = request.get_json()

    for student in students:

        if student["id"] == id:

            student["name"] = data["name"]

            return {
                "Message": "Student Updated",
                "Student": student
            }

    return {"Message": "Student Not Found"}


@app.route('/delete_student/<int:id>', methods=['DELETE'])
def delete_student(id):

    for student in students:

        if student["id"] == id:

            students.remove(student)

            return {
                "Message": "Student Deleted"
            }

    return {
        "Message": "Student Not Found"
    }





if __name__=="__main__":
    app.run(debug=True)