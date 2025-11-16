from student import Student
from my_exception import MyException

class Group:
    """
    A class of a group of students.
    """
    def __init__(self, number: str) -> None:
        self.number = number
        self.group = set()

    def add_student(self, student: Student) -> None:
        """
        Adds a student to a group.
        """
        if len(self.group) >= 10:
            raise MyException("не можна додавати до групи більше 10-ти студентів")
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

    def __str__(self):
        """
        Returns a str representation of the group.
        """
        all_students = '\n'.join(str(s) for s in self.group)
        return f'Number: {self.number}\n{all_students}'
