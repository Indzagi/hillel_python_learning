class Human:
    """
    class creates and describes a person object
    """

    def __init__(self, gender: str, age: int,
                 first_name: str, last_name: str) -> None:
        """
        :param gender: str
        :param age: int
        :param first_name: str
        :param last_name: str
        """
        self.gener = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        """
        :return: str
        """
        return (f"Human: {self.first_name} {self.last_name},"
                f" {self.age} age, gender: {self.gener}")

    def __repr__(self) -> str:
        """
        :return: str
        """
        return f"{self.first_name} {self.last_name} {self.age} {self.gener}"
