class Human:
    def __init__(
                self, gender: str, age: int, first_name: str,
                 last_name: str
                 ) -> None:
        """
        A class that describes a person.
        """
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self)-> str:
        """
        Returns a str representation of a person.
        """
        return (
            f'Gender : {self.gender}\n'
            f'Age : {self.age}\n'
            f'First name : {self.first_name}\n'
            f'Last name : {self.last_name}'
        )
