import random

from models.database import Database
from models.student import Student
from utils.validator import validate_email, validate_password

db = Database()


def login_student():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    student = db.get_student_by_email(email)
    if student and student.password == password:
        print("Login successful!")
        return student
    else:
        print("Invalid credentials.")
        return None


def register_student():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    if not validate_email(email):
        print("Invalid email format.")
        return None
    password = input("Enter your password: ")
    if not validate_password(password):
        print("Invalid password format.")
        return None
    if db.get_student_by_email(email):
        print("Email already registered.")
        return None
    student = Student(name=name, email=email, password=password)
    db.add_student(student)
    print("Registration successful.")
    return student


def change_password(student):
    if student is None:
        print("No student is logged in.")
        return
    new_password = input("Enter new password: ")
    if validate_password(new_password):
        student.password = new_password
        db.update_student(student)
        print("Password updated successfully.")
    else:
        print("Invalid password format.")


def enroll_subject(student):
    if len(student.subjects) >= 4:
        print("You are already enrolled in the maximum number of 4 subjects.")
        return

    # 사전에 정의된 과목 이름 리스트
    subject_names = ["Mathematics", "Physics", "Chemistry", "Biology", "History"]

    # 랜덤 과목 이름 선택
    subject_name = random.choice(subject_names)

    while True:
        # 랜덤 과목 ID 생성 (1 ~ 999 사이의 숫자를 문자열로 변환)
        subject_id = str(random.randint(1, 999)).zfill(3)  # 항상 3자리를 유지

        # 이미 등록된 과목 ID와 중복되는지 확인
        if not any(s["id"] == subject_id for s in student.subjects):
            break  # 중복되지 않는 ID 발견 시 while 루프 탈출

    # 랜덤 성적 생성
    mark = random.randint(25, 100)
    grade = "Pass" if mark >= 50 else "Fail"

    # 과목 정보 생성
    subject_info = {
        "id": subject_id,
        "name": subject_name,
        "mark": mark,
        "grade": grade,
    }

    # 학생의 과목 목록에 과목 정보 추가
    student.subjects.append(subject_info)

    # 데이터베이스에 학생 정보 업데이트
    db.update_student(student)
    print(
        f"Successfully enrolled in {subject_name} with subject ID {subject_id}, mark {mark}, and grade {grade}."
    )


def update_student_performance(student):
    total_marks = sum(sub["mark"] for sub in student.subjects)
    average = total_marks / len(student.subjects)
    student.average = average
    student.pass_status = "Pass" if average >= 50 else "Fail"
    print(f"Updated average mark: {average}, Pass status: {student.pass_status}")


def remove_subject(student):
    if student is None:
        print("No student is logged in.")
        return
    subject_id = input("Enter the subject ID to remove: ")
    original_length = len(student.subjects)
    student.subjects = [
        subject for subject in student.subjects if subject["id"] != subject_id
    ]
    if len(student.subjects) < original_length:
        db.update_student(student)  # 데이터베이스 업데이트
        print("Subject removed successfully.")
    else:
        print("Subject not found in your enrolled list.")


def show_enrolled_subjects(student):
    if student is None:
        print("No student is logged in.")
        return
    if not student.subjects:
        print("No subjects enrolled.")
        return

    print("Enrolled Subjects:")
    for subject in student.subjects:
        print(
            f"{subject['id']} - {subject['name']}, Mark: {subject['mark']}, Grade: {subject['grade']}"
        )
