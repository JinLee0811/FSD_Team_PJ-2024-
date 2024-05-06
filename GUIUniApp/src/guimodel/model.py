

import os
import sys

# 현재 작업 디렉토리 가져오기
currentPath = os.getcwd()

# rootDir 설정
rootDir = currentPath.replace('GUIUniApp', '')

# 모델 디렉토리 경로 추가
modelsPath = os.path.join(rootDir, 'CLIUniApp/src/models/')
sys.path.append(modelsPath)

# 경로 확인을 위해 출력
print(sys.path)

# database 모듈 임포트 시도
import database


class GUIUniAppModel:
    def __init__(self):
        self.database = database.Database()
        self.logged_in_user = None

    def authenticate(self, email, password):
        student = self.database.get_student_by_email(email)
        if student and student.password == password:
            self.logged_in_user = student
            return True
        return False

    def register_student(self, email, password, name, student_id):
        if not self.database.get_student_by_email(email) and not self.database.get_student_by_id(student_id):
            new_student = Student(email, password, name, student_id)
            self.database.add_student(new_student)
            return True, "Registration successful."
        return False, "Email or student ID already registered."

    def get_subjects(self):
        if self.logged_in_user:
            return self.logged_in_user.subjects
        return []

    def add_subject(self, subject):
        if self.logged_in_user:
            self.logged_in_user.subjects.append(subject)
            self.database.update_student(self.logged_in_user)
            return True
        return False

    def remove_subject(self, subject):
        if self.logged_in_user:
            self.logged_in_user.subjects.remove(subject)
            self.database.update_student(self.logged_in_user)
            return True
        return False