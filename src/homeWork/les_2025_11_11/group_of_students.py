# DZ 13.1. Group of students
class Human:
    """
    A class that describes a person.
    """

    def __init__(
            self, gender: str, age: int, first_name: str,
            last_name: str
    ) -> None:
        self.gender: str = gender
        self.age: int = age
        self.first_name: str = first_name
        self.last_name: str = last_name

    def __str__(self) -> str:
        """
        Returns a str representation of a person.
        """
        return (
            f'Gender : {self.gender}\n'
            f'Age : {self.age}\n'
            f'First name : {self.first_name}\n'
            f'Last name : {self.last_name}'
        )


class Student(Human):
    """
    Student class, inherits Human and adds a record book.
    """

    def __init__(
            self, gender: str, age: int, first_name: str,
            last_name: str, record_book: str
    ) -> None:
        super().__init__(gender, age, first_name, last_name)
        self.record_book: str = record_book

    def __str__(self) -> str:
        """
        Returns a str representation of the student.
        """
        return f'{self.first_name} {self.last_name}, age: {self.age}, record: {self.record_book}'


class Group:
    """
    A class of a group of students.
    """

    def __init__(self, number: str) -> None:
        self.number: str = number
        self.group = set()

    def add_student(self, student: Student) -> None:
        """
        Adds a student to a group.
        """
        self.group.add(student)

    def delete_student(self, last_name: str) -> None:
        """
        Removes a student from a group by last name.
        """
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name: str):
        """
        Finds a student in a group by last name.
        return: Student or None if not found
        """
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self) -> str:
        """
        Returns a str representation of the group.
        """
        all_students = '\n'.join(str(s) for s in self.group)
        return f'Number: {self.number}\n{all_students}'


# ---Перевірка---
st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
print(str(gr.find_student('Jobs')))
print(gr.find_student('Jobs2'))
print(isinstance(gr.find_student('Jobs'), Student))
gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!
