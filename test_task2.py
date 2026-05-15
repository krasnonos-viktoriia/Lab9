import unittest
from task2 import check_access

class TestCheckAccess(unittest.TestCase):
    def test_tc3_guest_active_not_admin(self):
        result = check_access("guest", True, False)
        self.assertFalse(result, "Помилка: Гість не повинен мати доступ")
    def test_tc5_user_inactive_not_admin(self):
        result = check_access("user", False, False)
        self.assertFalse(result, "Помилка: Неактивний користувач не повинен мати доступ")
    def test_tc6_user_inactive_admin(self):
        result = check_access("user", False, True)
        self.assertTrue(result, "Помилка: Адмін завжди повинен мати доступ")
    def test_tc7_user_active_not_admin(self):
        result = check_access("user", True, False)
        self.assertTrue(result, "Помилка: Активний користувач повинен мати доступ")