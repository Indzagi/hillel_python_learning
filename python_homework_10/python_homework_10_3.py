def is_even(digit: int) -> bool:
    """
    Function returns bool value where
    the number is even or not
    :param digit:
    :return: False or True
    """
    return not digit % 2


assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print('OK')
