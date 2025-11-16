from human import Human

class Student(Human):
    """
    Student class, inherits Human and adds a record book.
    """
    def __init__(
            self, gender: str, age: int, first_name: str,
            last_name: str, record_book: str
    ) -> None:
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self) -> str:
        """
        Returns a str representation of the student.
        """
        return f'{self.first_name} {self.last_name}, age: {self.age}, record: {self.record_book}'

    def __eq__(self, other: object) -> bool:
        """
        Compares students by their string representation (__str__).
        Returns True if both objects are Student and have the same str().
        """
        if not isinstance(other, Student):
            return False
        return str(self) == str(other)

    def __hash__(self) -> int:
        """
        Student is a set or dictionary key.
        Hashes a student by its string representation (__str__).
        """
        return hash(str(self))

