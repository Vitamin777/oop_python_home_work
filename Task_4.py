list_students = []
list_lecturers = []


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.mean_grades = 0
        global list_students
        list_students += [self]

    def mean(self):
        grade_values = []
        for value in self.grades.values():
            grade_values += value
        self.mean_grades = round(sum(grade_values) / len(grade_values), 1)
        return self.mean_grades

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        self.mean()
        other.mean()
        return self.mean_grades < other.mean_grades

    def __str__(self):
        some_student = f'Имя: {self.name}\nФамилия: {self.surname}\n' + \
                       f'Средняя оценка за домашние задания: {self.mean()}\n' + \
                       f'Курсы в процессе изучения: {self.courses_in_progress}\n' + \
                       f'Завершенные курсы:  {self.finished_courses}\n'
        return some_student

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course \
                in lecturer.courses_attached and grade in range(11):
            if course in lecturer.lectures:
                lecturer.lectures[course] += [grade]
            else:
                lecturer.lectures[course] = [grade]
        else:
            print('Ошибка')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lectures = {}
        self.mean_grade = 0
        global list_lecturers
        list_lecturers += [self]

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        self.mean()
        other.mean()
        return self.mean_grades < other.mean_grades

    def mean(self):
        grade_values = []
        for value in self.lectures.values():
            grade_values += value
        self.mean_grades = round(sum(grade_values) / len(grade_values), 1)
        return self.mean_grades

    def __str__(self):
        some_lecturer = f'Имя: {self.name}\nФамилия: {self.surname}\n' + \
                        f'Средняя оценка за лекции: {self.mean()}\n'
        return some_lecturer


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress \
                and grade in range(11):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print('Ошибка')

    def __str__(self):
        some_reviewer = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return some_reviewer


def mean_grades_students_course(list_students,course):
    total = 0
    counter_student = 0
    for student in list_students:
        if course in student.courses_in_progress:
            mean_grades = sum(student.grades[course])/len(student.grades[course])
            total += mean_grades
            counter_student += 1
    if counter_student == 0:
        return f'Курс {course} студенты не изучают'
    else:
        return f'Средняя оценка студентов за домашние задания по курсу {course}: {round(total/counter_student,1)}'


def mean_grades_lecturers_course(list_lecturers,course):
    total = 0
    counter_lecturers = 0
    for lecturer in list_lecturers:
        if course in lecturer.courses_attached:
            mean_grades = sum(lecturer.lectures[course])/len(lecturer.lectures[course])
            total += mean_grades
            counter_lecturers += 1
    if counter_lecturers == 0:
        return f'Лекторы курс {course} не преподают'
    else:
        return f'Средняя оценка лекторов по курсу {course}: {round(total/counter_lecturers,1)}'

# Creating instances of classes and setting parameters

best_student = Student('Bruce', 'Lee', 'male')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

other_student = Student('Petr', 'Petrov', 'male')
other_student.courses_in_progress += ['Python']
other_student.courses_in_progress += ['Git']
other_student.finished_courses += ['Введение в программирование']

cool_lecturer = Lecturer('Albert', 'Enstein')
cool_lecturer.courses_attached += ['Python']

other_lecturer = Lecturer('Vasiliy', 'Ivanov')
other_lecturer.courses_attached += ['Git']

cool_reviewer = Reviewer('Garry', 'Kasparov')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']

other_reviewer = Reviewer('Karl', 'Marks')
other_reviewer.courses_attached += ['Python']
other_reviewer.courses_attached += ['Git']

other_student.rate_hw(other_lecturer, 'Git', 9)
other_student.rate_hw(other_lecturer, 'Git', 8)
other_student.rate_hw(other_lecturer, 'Git', 7)
other_student.rate_hw(other_lecturer, 'Git', 10)

best_student.rate_hw(cool_lecturer, 'Python', 7)
best_student.rate_hw(cool_lecturer, 'Python', 10)
best_student.rate_hw(cool_lecturer, 'Python', 8)
best_student.rate_hw(cool_lecturer, 'Python', 10)

cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 7)
cool_reviewer.rate_hw(best_student, 'Python', 7)
cool_reviewer.rate_hw(best_student, 'Git', 10)
cool_reviewer.rate_hw(best_student, 'Git', 8)
cool_reviewer.rate_hw(best_student, 'Git', 7)

other_reviewer.rate_hw(other_student, 'Python', 5)
other_reviewer.rate_hw(other_student, 'Python', 8)
other_reviewer.rate_hw(other_student, 'Python', 7)
other_reviewer.rate_hw(other_student, 'Git', 9)
other_reviewer.rate_hw(other_student, 'Git', 8)
other_reviewer.rate_hw(other_student, 'Git', 7)


# method override test __str__

print(best_student)
print(other_student)

print(cool_lecturer)
print(other_lecturer)

print(cool_reviewer)
print(other_reviewer)

# method override test __lt__

print(best_student < other_student)
print(cool_lecturer > other_lecturer)

# mean_grades_students_course() function test

print(mean_grades_students_course(list_students, 'Python'))
print(mean_grades_students_course(list_students, 'Git'))

# mean_grades_students_course() function test

print(mean_grades_lecturers_course(list_lecturers, 'Python'))
print(mean_grades_lecturers_course(list_lecturers, 'Git'))


