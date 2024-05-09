import os
import sys
import random
# rootDir 설정
currentPath = os.getcwd()
rootDir = currentPath.replace('GUIUniApp', '')
modelsPath = os.path.join(rootDir, 'CLIUniApp/src/models/')
sys.path.append(modelsPath)

import database,subject

class GUIUniAppModel:
    def __init__(self):
        self.database = database.Database()
        self.logged_in_user = None

    #로그인 인증
    def authenticate(self, email, password):
        student = self.database.get_student_by_email(email)
        if student and student.password == password:
            self.logged_in_user = student
            return True
        return False
    
    def enroll_subject(self, student):
        if len(student.subjects) >= 4:
            return False
        
        while True:
            subject_id = str(random.randint(1, 999)).zfill(3)
            if not any(s.id == subject_id for s in student.subjects):
                break
        
        new_subject = subject.Subject(subject_id)
        new_subject.assign_random_mark()
        student.subjects.append(new_subject)
        
        return True
    
    def add_subject(self, subject):
        if self.logged_in_user:
            return self.enroll_subject(self.logged_in_user)
        return False

    def remove_subject(self, subject_id):
        if self.logged_in_user:
            subject_to_remove = next((s for s in self.logged_in_user.subjects if s.id == subject_id), None)
            if subject_to_remove:
                self.logged_in_user.subjects.remove(subject_to_remove)
                self.database.update_student(self.logged_in_user)  
                return True
        return False