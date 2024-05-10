import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

import random

from colorama import *
from models.database import *
from models.subject import *

init(autoreset=True)
db = Database()


def enroll_subject(student, db):
    if len(student.subjects) >= 4:
        print(Fore.RED + "Students are allowed to enroll in up to 4 subjects only.")
        return False

    subject_ids = {s.id for s in student.subjects}
    new_id = random.choice(
        [str(i).zfill(3) for i in range(1, 1000) if str(i).zfill(3) not in subject_ids]
    )

    new_subject = Subject(new_id)
    new_subject.assign_random_mark()
    student.subjects.append(new_subject)
    db.update_student(student)
    print(Fore.YELLOW + f"Enrolling in Subject - {new_id}")
    print(
        Fore.YELLOW
        + f"You are now enrolled in {len(student.subjects)} out of 4 subjects."
    )
    return True


def remove_subject(student, db):
    if student is None:
        print("No student is logged in.")
        return False

    subject_id = input("Remove subject by ID: ")
    if any(s.id == subject_id for s in student.subjects):
        student.subjects = [s for s in student.subjects if s.id != subject_id]
        db.update_student(student)
        print(Fore.YELLOW + f"Dropping Subject - {subject_id}")
        print(
            Fore.YELLOW
            + f"You are now enrolled in {len(student.subjects)} out of 4 subjects."
        )
        return True
    else:
        print(Fore.RED + "Subject not found in your enrolled list.")
        return False


def show_enrolled_subjects(student):
    if student is None:
        print("No student is logged in.")
        return
    if not student.subjects:
        print(Fore.YELLOW + "Showing 0 subjects.")
        return

    print(Fore.YELLOW + f"Showing {len(student.subjects)} subjects.")
    for subject in student.subjects:
        print(
            f"[ Subject::{subject.id} -- Mark = {subject.mark} -- Grade = {subject.grade} ]"
        )
