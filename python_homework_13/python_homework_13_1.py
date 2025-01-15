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

    def __str__(self) -> str:
        """
        :return: str
        """
        return (f"{self.first_name} {self.last_name}"
                f" {self.age} {self.gener} {self.record_book}")


class Group:
    """
    class creates a Group object with the group name
    attribute has multiple functions, adding student,
    searching student and deleting student
    """

    def __init__(self, number: str) -> None:
        """
        Function get number of group and
        creates a set of students
        :param number: str
        """
        self.number = number
        self.group = set()

    def add_student(self, student: Student) -> None:
        """
        Function add object to set group
        :param student: class Student
        """
        self.group.add(student)

    def delete_student(self, last_name: str) -> None:
        """
        Function get student's last name and
        removes the Student object from the
        group using function - find_student
        (search function)
        :param last_name: str
        """
        self.group.discard(self.find_student(last_name))

    def find_student(self, last_name: str) -> object or None:
        """
        Function
        :param last_name: str
        :return: Object or None
        """
        my_stud_list = list(self.group)
        my_iter = 0
        for my_stud_list[my_iter] in my_stud_list:
            my_temp_stud = str(my_stud_list[my_iter]).split()
            if my_temp_stud[1] == last_name:
                return my_stud_list[my_iter]
            elif my_temp_stud[1] != last_name:
                my_iter += 1
            else:
                return None

    def __str__(self) -> str:
        """
        Function returns information about
        the group and students in the group
        :return: str
        """
        my_stud_list = list(self.group)
        my_iter = 0
        all_students = ""
        for my_stud_list[my_iter] in my_stud_list:
            my_temp_stud = str(my_stud_list[my_iter]).split()
            all_students = (f"{all_students}\nStudent {my_iter + 1}:"
                            f" {my_temp_stud[0]} {my_temp_stud[1]}"
                            f", {my_temp_stud[2]} age, {my_temp_stud[3]}")
            my_iter += 1
        return f'Number: {self.number}{all_students}'


st1 = Student('Male', 30, 'Steve',
              'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza',
              'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'
gr.delete_student('Taylor')
print(gr)
gr.delete_student('Taylor')
