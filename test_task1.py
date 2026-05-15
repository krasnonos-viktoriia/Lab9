from task1 import process_data
def test_empty_list():
    assert process_data([]) == 0
def test_negative_number():
    assert process_data([-1]) == 0
def test_zero():
    assert process_data([0]) == 0
def test_positive_number():
    assert process_data([3]) == 2
def test_mixed_numbers():
    assert process_data([-1, 3, 4]) == 4

# 2. Branch coverage tests
def test_outer_loop_not_entered():
    assert process_data([]) == 0
def test_data_negative_continue():
    assert process_data([-1]) == 0
def test_data_zero_inner_loop_skipped():
    assert process_data([0]) == 0
def test_inner_loop_entered_even_and_odd_branches():
    assert process_data([3]) == 2

# 3. Condition coverage tests
def test_condition_data_negative_true():
    assert process_data([-1]) == 0
def test_condition_data_negative_false():
    assert process_data([0]) == 0
def test_condition_j_even_true():
    assert process_data([1]) == 0
def test_condition_j_even_false():
    assert process_data([2]) == 0

# 5. Loop coverage tests
def test_loop_outer_zero_iterations():
    assert process_data([]) == 0
def test_loop_inner_one_iteration():
    assert process_data([1]) == 0
def test_loop_outer_many_inner_zero_and_many_iterations():
    assert process_data([-1, 0, 3]) == 2