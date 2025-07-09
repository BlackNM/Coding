# student_crud.py
import sqlite3

def connect():
    return sqlite3.connect("students.db")

def add_student(name, age, grade):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", (name, age, grade))
    conn.commit()
    conn.close()

def view_students():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    conn.close()
    return rows

def search_student(name):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students WHERE name LIKE ?", ('%' + name + '%',))
    rows = cur.fetchall()
    conn.close()
    return rows

def update_student(student_id, name, age, grade):
    conn = connect()
    cur = conn.cursor()
    cur.execute("UPDATE students SET name=?, age=?, grade=? WHERE id=?", (name, age, grade, student_id))
    conn.commit()
    conn.close()

def delete_student(student_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()
    conn.close()

# CLI Interface
def menu():
    while True:
        print("\n=== STUDENT MANAGEMENT SYSTEM ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            grade = input("Enter Grade: ")
            add_student(name, age, grade)
            print("Student added.")

        elif choice == '2':
            for row in view_students():
                print(row)

        elif choice == '3':
            name = input("Enter name to search: ")
            results = search_student(name)
            for row in results:
                print(row)

        elif choice == '4':
            student_id = int(input("Enter Student ID to update: "))
            name = input("Enter New Name: ")
            age = int(input("Enter New Age: "))
            grade = input("Enter New Grade: ")
            update_student(student_id, name, age, grade)
            print("Student updated.")

        elif choice == '5':
            student_id = int(input("Enter Student ID to delete: "))
            delete_student(student_id)
            print("Student deleted.")

        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
