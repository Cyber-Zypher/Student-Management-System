# Code made by Sidharth Everett and friends at M E D U S A  Infosystems International.

import pymysql

# Database Configuration
db = pymysql.connect(host="localhost", user="UNAME", password="password", database="DB_NAME")
cursor = db.cursor()

# Function to Add a Student
def add_student(name, age, grade):
    sql = "INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)"
    values = (name, age, grade)
    cursor.execute(sql, values)
    db.commit()

# Function to Display All Students
def display_students():
    sql = "SELECT * FROM students"
    cursor.execute(sql)
    students = cursor.fetchall()
    
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Grade: {student[3]}")

# Function to Remove a Student
def remove_student(student_id):
    sql = "DELETE FROM students WHERE id = %s"
    cursor.execute(sql, (student_id,))
    db.commit()

# Main Program
if __name__ == "__main__":
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Remove Student")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            grade = input("Enter student grade: ")
            add_student(name, age, grade)
            print("Student added successfully!")
        elif choice == "2":
            print("\nList of Students:")
            display_students()
        elif choice == "3":
            student_id = int(input("Enter student ID to remove: "))
            remove_student(student_id)
            print("Student removed successfully!")
        elif choice == "4":
            print("Exiting...")
            break
        elif choice == '':
            print("Please select a valid option.")
        else:
            print("Invalid choice. Please select a valid option.")
            
    db.close()
