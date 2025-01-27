"""
класс логгер
сберігати в приватному словникові атрібути
логує всі операції з атрибутами
доступ
видалення встановлення
за наявності спробувати отримати доступ до атрибуту, якого нема і додати до словнику
"""


class Logger:

    def __init__(self):
        self.__my_dict_logger = {}
        self.my_dict_attr = {}
        object.__setattr__(self, "name", "1")

    def __getattribute__(self, name):
        self.__my_dict_logger["getattribute"] = self.__getattribute__(name)
        print(f"Робить Getattribute. Атрибут {name}")
        try:
            return super().__getattribute__(name)
        except AttributeError:
            print(f"Робить Getattribute. атрибут {name} не знайдено.")
            return self.__getattr__(name)

    def __getattr__(self, name):
        self.__my_dict_logger["getattr"] = self.__getattr__(name)
        if name in self.my_dict_attr:
            print(f"Робить Getattr. Атрибут {name}")
            return self.my_dict_attr[name]
        print(f"Робить Getattr. Атрибут {name} не знайдено")
        return None

    def __setattr__(self, name, value):
        self.__my_dict_logger["setattr"] = f"Робить Setattr. Атрибут {name}"
        self.my_dict_attr[name] = value
        print(f"Робить Setattr. Атрибут {name}")


obj = Logger()

obj.name = "One"
obj.value = 1

print(obj.name)
