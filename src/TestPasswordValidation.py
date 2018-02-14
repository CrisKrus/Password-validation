import unittest


def validate_password(password):
    if len(password) < 8:
        return False


class TestPasswordValidation(unittest.TestCase):

    def test__given_password_with_less_than_eight_chars(self):
        self.assertFalse(validate_password(['q', 'w', 'e', 'r', 't']))

    def test__given_password_with_at_least_one_upper_case_char(self):
        self.assertTrue(validate_password(['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'W']))
