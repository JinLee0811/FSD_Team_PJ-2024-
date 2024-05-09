import os
import sys

# rootDir 설정
currentPath = os.getcwd()
rootDir = currentPath.replace("GUIUniApp", "")
modelsPath = os.path.join(rootDir, "CLIUniApp/src/models/")
sys.path.append(modelsPath)

import database


class GUIUniAppModel:
    def __init__(self):
        self.database = database.Database()
        self.logged_in_user = None

    # 로그인 인증
    def authenticate(self, email, password):
        student = self.database.get_student_by_email(email)
        if student and student.password == password:
            self.logged_in_user = student
            return True
        return False
