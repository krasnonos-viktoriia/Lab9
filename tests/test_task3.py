from task3 import process_matrix


# Порожня матриця
def test_empty():
    assert process_matrix([]) == 0


# Від’ємні числа
def test_negative():
    assert process_matrix([[-1, -2]]) == 0


# Нуль
def test_zero():
    assert process_matrix([[0]]) == 0


# Додатне число
def test_positive():
    assert process_matrix([[2]]) == 1


# Декілька рядків
def test_multiple_rows():
    assert process_matrix([[1, 2], [3]]) == 4