import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from models.subject import *


class Student:
    def __init__(self, name, email, password, student_id):
        self.name = name
        self.email = email
        self.password = password
        self.student_id = student_id
        self.subjects = []
        self.average_mark = None
