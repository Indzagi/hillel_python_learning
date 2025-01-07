def is_even(digit):
    """
    Function returns bool value where
    the number is even or not
    :param digit:
    :return: False ore True
    """
    return digit % 2 == 0


assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print('OK')
