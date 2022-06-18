class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

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


best_student = Student('Bruce', 'Lee', 'male')
best_student.courses_in_progress += ['Python']

cool_lecturer = Lecturer('Albert', 'Ensstein')
cool_lecturer.courses_attached += ['Python']

cool_reviewer = Reviewer('Garry', 'Kasparov')
cool_reviewer.courses_attached += ['Python']

best_student.rate_hw(cool_lecturer, 'Python', 9)
best_student.rate_hw(cool_lecturer, 'Python', 10)
best_student.rate_hw(cool_lecturer, 'Python', 8)

cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Python', 7)

print(f'\nОценки лектора {cool_lecturer.name} {cool_lecturer.surname} от студентов:{cool_lecturer.lectures} \n')
print(f'Оценки домашних работ студента {best_student.name} {best_student.surname}',
      f'от экспертов:{best_student.grades} \n')
