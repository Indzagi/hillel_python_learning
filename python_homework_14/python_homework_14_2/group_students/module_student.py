from .module_human import Human


class Student(Human):
    """
    class inherits main class Human reassigning output information
    """

    def __init__(self, gender: str, age: int, first_name: str,
                 last_name: str, record_book: str) -> None:
        """
        :param gender: str
        :param age: int
        :param first_name: str
        :param last_name: str
        :param record_book: str
        """
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def comparison(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        """
        :return: str
        """
        return f"{self.first_name} {self.last_name}"
#                f" {self.age} {self.gener} {self.record_book}")
