import pytest

def validate_input(user, password):
    if not user:
        return "Missing user"
    if len(password) < 8:
        return "Weak password"
    if any(char.isdigit() for char in password) and any(char.isupper() for char in password):
        return "Valid"
    return "Invalid"

ALL_COMBINATIONS = [
    ("",      "ValidPass1",   "Missing user"),  # Немає користувача
    ("user1", "Short1A",      "Weak password"), # Короткий пароль (< 8)
    ("user1", "alllowercase", "Invalid"),       # Довгий, але без цифр і великих
    ("user1", "ALLUPPERCASE", "Invalid"),       # Довгий, є великі, без цифр
    ("user1", "alllower1234", "Invalid"),       # Довгий, є цифри, без великих
    ("user1", "ValidPass1",   "Valid"),         # Довгий, є цифри і великі
]

@pytest.mark.parametrize("user, password, expected", ALL_COMBINATIONS)
def test_condition_combination_coverage(user, password, expected):
    assert validate_input(user, password) == expected

MCDC_TESTS = [
    pytest.param("admin", "ValidPass1", "Valid",         id="Base_All_Conditions_Met"),
    pytest.param("",      "ValidPass1", "Missing user",  id="MCDC_Missing_User"),
    pytest.param("admin", "Short1A",    "Weak password", id="MCDC_Weak_Password"),
    pytest.param("admin", "VALIDPASS",  "Invalid",       id="MCDC_Missing_Digit"),
    pytest.param("admin", "validpass1", "Invalid",       id="MCDC_Missing_Upper"),
]

@pytest.mark.parametrize("user, password, expected", MCDC_TESTS)
def test_mcdc_validation(user, password, expected):
    assert validate_input(user, password) == expected