class Counter:
    """
    Digital counter can be set to initial value,
    minimum and maximum value and return
    current value counter
    """

    def __init__(self, current: int = 1, min_value: int = 0,
                 max_value: int = 10) -> None:
        """
        Function initializes object with starting
        min and max value attributes
        (with default parameters)
        :param current: int (start value)
        :param min_value: int
        :param max_value: int
        """
        self.current = current
        self.min_value = min_value
        self.max_value = max_value

    def set_current(self, start: int) -> None:
        """
        Function set start parameter
        :param start: int
        """
        self.current = start

    def set_max(self, max_max: int) -> None:
        """
        Function set maximum parameter
        :param max_max: int
        """
        self.max_value = max_max

    def set_min(self, min_min: int) -> None:
        """
        Function set minimum parameter
        :param min_min: int
        """
        self.min_value = min_min

    def step_up(self) -> None or ValueError:
        """
        Function adds one to the counter until
        it reaches the maximum value,
        and returns an error on the next call
        :return: None or ValueError
        """
        if self.current < self.max_value:
            self.current += 1
        else:
            raise ValueError("Досягнуто максимального значення")

    def step_down(self) -> None or ValueError:
        """
        Function subtraction one to the counter until
        it reaches the minimum value,
        and returns an error on the next call
        :return: None or ValueError
        """
        if self.current > self.min_value:
            self.current -= 1
        else:
            raise ValueError("Досягнуто мінімального значення")

    def get_current(self) -> int:
        """
        Function returns the current counter value
        :return: int
        """
        return self.current


counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
assert counter.get_current() == 10, 'Test1'
try:
    counter.step_up()  # ValueError
except ValueError as e:
    print(e)  # Достигнут максимум
assert counter.get_current() == 10, 'Test2'

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
assert counter.get_current() == 7, 'Test3'
try:
    counter.step_down()  # ValueError
except ValueError as e:
    print(e)  # Достигнут минимум
assert counter.get_current() == 7, 'Test4'
