import fcntl
import os
import pickle
import sys
import threading

from colorama import *

init(autoreset=True)

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)


# single thread에서만 동작하는 코드
# 여러 곳에서 데이터 간섭 못하고 하나의 데이터만 사용 가능
class SingletonMeta(type):
    _instances = {}
    _lock: threading.Lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
            return cls._instances[cls]


class Database(metaclass=SingletonMeta):
    def __init__(self):
        self.filename = os.path.join(parent_dir, "data", "students.data")
        self.file_lock = threading.Lock()
        self.students = self.load_students()

    def load_students(self):
        try:
            print(f"Trying to load from: {self.filename}")  # 파일 경로 출력 추가
            with self.file_lock, open(self.filename, "rb") as f:
                fcntl.flock(f, fcntl.LOCK_EX)
                # Python 2에서 생성된 파일을 Python 3에서 읽을 경우 추가 옵션
                if sys.version_info[0] > 2:
                    data = pickle.load(f, encoding="latin1", errors="ignore")
                else:
                    data = pickle.load(f)
                fcntl.flock(f, fcntl.LOCK_UN)
                return data
        except FileNotFoundError:
            print("Student data file not found.")
            return []
        except (EOFError, pickle.UnpicklingError) as e:
            print(f"Error reading student data: {e}")
            return []
        except Exception as e:
            print(f"Unexpected error: {e}")
            return []

    def save_students(self):
        try:
            with self.file_lock, open(self.filename, "wb") as f:
                fcntl.flock(f, fcntl.LOCK_EX)
                # 호환성을 유지하기 위해 protocol=2 사용
                pickle.dump(self.students, f, protocol=2)
                fcntl.flock(f, fcntl.LOCK_UN)
        except Exception as e:
            print(f"Error saving data: {e}")

    def get_student_by_email(self, email):
        return next(
            (student for student in self.students if student.email == email), None
        )

    def get_student_by_id(self, student_id):
        return next(
            (student for student in self.students if student.student_id == student_id),
            None,
        )

    def add_student(self, student):
        if not self.get_student_by_email(student.email) and not self.get_student_by_id(
            student.student_id
        ):
            self.students.append(student)
            self.save_students()
        else:
            print(Fore.BLUE + f"Student {student.email} already exists.")

    def update_student(self, student):
        for i, s in enumerate(self.students):
            if s.student_id == student.student_id:
                self.students[i] = student
                self.save_students()
                return True
        print("Student not found.")
        return False

    def remove_student_by_id(self, student_id):
        original_len = len(self.students)
        self.students = [s for s in self.students if s.student_id != student_id]
        if len(self.students) < original_len:
            self.save_students()
            return True
        return False

    def get_all_students(self):
        return self.students

    def clear_all(self):
        self.students = []
        self.save_students()

    def remove_student_by_email(self, email):
        original_len = len(self.students)
        self.students = [s for s in self.students if s.email != email]
        if len(self.students) < original_len:
            self.save_students()
