# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class School:
    def __init__(self, forms, teachers):
        self.forms = forms
        self.teachers = teachers

    def show_forms(self):
        print("Классы школы: ")
        print(self.forms)

    def show_student_subjects(self, name):
        print("Предметы ученика: ")
        for form in self.forms:
            for student in form.students:
                if student.name == name:
                    for teacher in form.teachers:
                        print(teacher.subject)

    def show_teachers_in_form(self, form_name):
        print("Учителя в классе:")
        for form in self.forms:
            if form_name == form.name:
                for teacher in form.teachers:
                    print(teacher)



class Person:
    def __init__(self, name):
        self.name = name  # фио

    def __repr__(self):
        return self.name


class Form:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []

    def __repr__(self):
        return self.name

    def show_students(self):
        print("Ученики класса {}".format(self))
        print(self.students)


class Student(Person):
    def __init__(self, name, form, mother, father):
        super(Student, self).__init__(name)
        self.form = form
        self.mother = mother
        self.father = father
        form.students.append(self)


class Teacher(Person):
    def __init__(self, name, subject, forms):
        super(Teacher, self).__init__(name)
        self.subject = subject
        self.forms = forms
        for form in forms:
            form.teachers.append(self)


form1 = Form("5 А")
form2 = Form("6 Б")


t1 = Teacher(
    name="Буин В.В.",
    subject="История",
    forms=[form1, ]
)

t2 = Teacher(
    name="Букин Ф.Г.",
    subject="Математика",
    forms=[form1, form2]
)

student1 = Student(
    name="Захаров Ф.Г.",
    form=form1,
    mother="Захарова A.A.",
    father="Захаров Г.A.",
)

student2 = Student(
    name="Жихаров Ф.Г.",
    form=form1,
    mother="Жихарова A.A.",
    father="Жихаров Г.A.",
)

student3 = Student(
    name="Кухаров Ф.Г.",
    form=form2,
    mother="Кухаров A.A.",
    father="Кухаров Г.A.",
)

school = School(forms=[form1, form2], teachers=[t1, t2])

school.show_forms()

for form in school.forms:
    form.show_students()

school.show_student_subjects("Кухаров Ф.Г.")

school.show_teachers_in_form("5 А")
