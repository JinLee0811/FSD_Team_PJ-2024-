# CLIUniApp

CLIUniApp is a university management system that provides a command-line interface for managing various needs of students and administrators. This system allows students to register for courses, delete courses, change passwords, and more, while administrators can manage student information, grades, and other administrative tasks.

## Features

### Students
- Register and delete courses
- Change password
- View course enrollments
- Login and manage profile

### Administrators
- View student information
- Manage grades and courses
- Manage student accounts
- Login and manage permissions

## Installation

CLIUniApp requires Python 3.12 or higher. Follow these steps to install:

1. Clone the project:
   ```bash
   git clone https://your-repository-url.com 

2. Install the required libraries:
    ```pip install -r requirements.txt

3. Run the application:
    ```python src/main.py


## Usage

CLIUniApp is operated through a command-line interface. Below are the commands available for students and administrators:

### For Students

- **Login**
  ```bash
  login --student [student_id] [password]


### For Students

- **Enroll in a Course**
  - Command:
    ```
    enroll [subject_id]
    ```
  - Description: Use this command to register for a course. Replace `[subject_id]` with the actual ID of the course you wish to enroll in.

## how to use git
- git clone first check your all folders
- after git clone
- check your branch (git branch (your name ex "jin"))
- git checkout your branch

## if you want to push your branch
- check your branch first and commit to team member
- git add .
- git commit -m "your message"
- git push origin (your branch name)