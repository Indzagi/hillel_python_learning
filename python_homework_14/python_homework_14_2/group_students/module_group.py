from .module_student import Student


class Group:
    """
    class creates a Group object with the group name
    attribute has multiple functions, adding student if
    there are no more than 10, searching student and deleting student
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
        Function adds an object to set group
        provided that there are no more than 10 students
        :param student: class Student
        """
        group_size = len(self.group)
        if group_size < 10:
            self.group.add(student)
        else:
            raise ValueError("Group size exceeded, "
                             "group can only consist of 10 people")

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
        Function finds the student by last name
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