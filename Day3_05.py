from enum import Enum

class CourseType(Enum):
    LECTURE = 1
    LAB = 2
    SEMINAR = 3

class GradeSystem(Enum):
    LETTER = 1
    PERCENTAGE = 2
    GPA = 3

class CourseStatus(Enum):
    OPEN = 1
    CLOSED = 2
    FULL = 3

class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Student(Person):
    def __init__(self, name, id):
        super().__init__(name, id)
        self.enrolled_courses = {}  # {course_id: grade}

class Professor(Person):
    def __init__(self, name, id, office_hours):
        super().__init__(name, id)
        self.office_hours = office_hours

class Course:
    def __init__(self, id, name, credits, course_type, capacity, prerequisites=None):
        self.id = id
        self.name = name
        self.credits = credits
        self.course_type = course_type
        self.capacity = capacity
        self.enrolled_students = {}  # {student_id: grade}
        self.professor = None
        self.prerequisites = prerequisites or []
        self.status = CourseStatus.OPEN

    def assign_professor(self, professor):
        self.professor = professor

    def enroll_student(self, student):
        if len(self.enrolled_students) < self.capacity:
            self.enrolled_students[student.id] = None # No grade initially
            student.enrolled_courses[self.id] = None
            if len(self.enrolled_students) == self.capacity:
                self.status = CourseStatus.FULL
            return True
        else:
            self.status = CourseStatus.FULL
            return False

    def assign_grade(self, student_id, grade):
        if student_id in self.enrolled_students:
            self.enrolled_students[student_id] = grade
            return True
        return False

class Department:
    def __init__(self, name):
        self.name = name
        self.courses = {}

class University:
    def __init__(self, name):
        self.name = name
        self.departments = {}
        self.students = {}
        self.professors = {}

    def add_department(self, department):
        self.departments[department.name] = department

    def add_course(self, department_name, course):
        if department_name in self.departments:
            self.departments[department_name].courses[course.id] = course

    def add_student(self, student):
        self.students[student.id] = student

    def add_professor(self, professor):
        self.professors[professor.id] = professor

# Example Usage
university = University("NUST")
cs_department = Department("Computer Science")
university.add_department(cs_department)

cs101 = Course("CS101", "Introduction to Programming", 3, CourseType.LECTURE, 30)
university.add_course("Computer Science", cs101)

prof_ali = Professor("Ali", "P001", "Mon 2-4 PM")
cs101.assign_professor(prof_ali)
university.add_professor(prof_ali)

student1 = Student("Ahmed", "S001")
student2 = Student("Sara", "S002")
university.add_student(student1)
university.add_student(student2)

cs101.enroll_student(student1)
cs101.enroll_student(student2)

cs101.assign_grade(student1.id, "A")

print(f"{student1.name}'s grade in {cs101.name}: {cs101.enrolled_students[student1.id]}")
print(f"Course Status of {cs101.name}: {cs101.status}")

#Extensibility Example: Adding Lab Component
class Lab(Course):
    def __init__(self, id, name, credits, capacity, lab_instructor=None, prerequisites=None):
        super().__init__(id, name, credits, CourseType.LAB, capacity, prerequisites)
        self.lab_instructor = lab_instructor

cs101_lab = Lab("CS101L", "Introduction to Programming Lab", 1, 20)
university.add_course("Computer Science", cs101_lab)
print(f"Course Type of CS101L: {cs101_lab.course_type}")