import unittest


def validate_password(password, length):
    if length < 8:
        return False
    if password[0].isupper():
        return True
    else:
        return validate_password(password[1:length], length)

    return False

class TestPasswordValidation(unittest.TestCase):

    def test__given_password_with_less_than_eight_chars(self):
        self.assertFalse(validate_password(['q', 'w', 'e', 'r', 't'], 5))

    def test__given_password_with_at_least_one_upper_case_char(self):
        self.assertTrue(validate_password(['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'W'], 11))
