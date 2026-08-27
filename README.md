# Student Management Flask API

A simple REST API for managing student records using Python and Flask. The API supports basic CRUD operations such as creating, reading, updating, and deleting student records.

## 🚀 Features

- Get all students
- Get a student by ID
- Add a new student
- Update an existing student
- Delete a student
- Simple REST API endpoints

## 🛠️ Technologies Used

- Python
- Flask

## 📁 Project Structure

```text
student-management-flask-api/
│
├── app.py
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/pegadapallyadithya/student-management-flask-api.git
```

### 2. Move into the project folder

```bash
cd student-management-flask-api
```

### 3. Install Flask

```bash
pip install flask
```

## ▶️ Run the Application

Run the following command:

```bash
python app.py
```

The API will start running locally.

## 🔗 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Check if the API is running |
| GET | `/students` | Get all students |
| GET | `/student/<id>` | Get a student by ID |
| POST | `/add_student` | Add a new student |
| PUT | `/update_student/<id>` | Update a student |
| DELETE | `/delete_student/<id>` | Delete a student |

## 📦 Example Student Data

```json
{
    "id": 3,
    "name": "John"
}
```

## 🧠 How It Works

Student data is currently stored in an in-memory Python list.

The API receives HTTP requests and performs CRUD operations on the student records:

1. **Create** → Add a new student using `POST`
2. **Read** → Retrieve student information using `GET`
3. **Update** → Update a student's name using `PUT`
4. **Delete** → Remove a student using `DELETE`

> **Note:** Since the data is stored in memory, the data will reset when the application is restarted.

## 🚀 Future Improvements

- Add a database such as SQLite or PostgreSQL
- Add input validation
- Improve error handling
- Add unique ID generation
- Add authentication
- Deploy the API

## 👨‍💻 Author

**Adithya Pegadapally**

Aspiring AI Engineer | Python | Machine Learning | Generative AI
