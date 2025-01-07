def is_even(number):
    """
    Function checking the last digit value
    and returns bool value where
    the number is even or not
    :param number: int number
    :return: True or False
    """
    odd_numbers = ["1", "2", "3", "5", "7", "9"]
    number_str = str(number)
    return number_str[-1:] not in odd_numbers


assert is_even(2494563894038 ** 2) == True, 'Test1'
assert is_even(1056897 ** 2) == False, 'Test2'
assert is_even(24945638940387 ** 3) == False, 'Test3'
print('OK')
