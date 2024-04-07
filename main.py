class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, Gender: {self.gender}, Age: {self.age}"


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return super().__str__() + f", Record Book: {self.record_book}"


class GroupOverflowError(Exception):
    def __init__(self, message="Group capacity exceeded"):
        self.message = message
        super().__init__(self.message)


class Group:
    MAX_CAPACITY = 10 

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= self.MAX_CAPACITY:
            raise GroupOverflowError
        else:
            self.group.add(student)

    def delete_student(self, last_name):
        student_to_remove = self.find_student(last_name)
        if student_to_remove:
            self.group.remove(student_to_remove)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Number:{self.number}\n{all_students}'


try:
    st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
    st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
    st3 = Student('Male', 22, 'John', 'Doe', 'AN146')
    st4 = Student('Female', 28, 'Emma', 'Watson', 'AN147')
    st5 = Student('Male', 26, 'Tom', 'Cruise', 'AN148')
    st6 = Student('Female', 23, 'Jennifer', 'Lopez', 'AN149')
    st7 = Student('Male', 21, 'Michael', 'Jordan', 'AN150')
    st8 = Student('Female', 27, 'Scarlett', 'Johansson', 'AN151')
    st9 = Student('Male', 24, 'Leonardo', 'DiCaprio', 'AN152')
    st10 = Student('Female', 29, 'Angelina', 'Jolie', 'AN153')
    st11 = Student('Male', 31, 'Brad', 'Pitt', 'AN154')

    gr = Group('PD1')
    gr.add_student(st1)
    gr.add_student(st2)
    gr.add_student(st3)
    gr.add_student(st4)
    gr.add_student(st5)
    gr.add_student(st6)
    gr.add_student(st7)
    gr.add_student(st8)
    gr.add_student(st9)
    gr.add_student(st10)
    gr.add_student(st11)

except GroupOverflowError:
    print("Error: Group capacity exceeded")

print(gr)


assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)

gr.delete_student('Taylor')
