import unittest


def validate_password_recursive(password, length, has_upper, has_lower):
    if has_upper and has_lower:
        return True

    if len(password) == 0:
        return False

    if password[0].isupper():
        return validate_password_recursive(password[1:length], length, True, has_lower)

    if password[0].islower():
        return validate_password_recursive(password[1:length], length, has_upper, True)

    return False


def validate_password(password, length):
    if length < 8:
        return False
    return validate_password_recursive(password, length, False, False)


class TestPasswordValidation(unittest.TestCase):

    def test__given_password_with_less_than_eight_chars(self):
        self.assertFalse(validate_password(['q', 'w', 'e', 'r', 't'], 5))

    def test__given_password_without_one_upper_case_char(self):
        self.assertFalse(validate_password(['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'w'], 11))

    def test__given_password_with_at_least_one_lower_case_char(self):
        self.assertFalse(validate_password(['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'W'], 11))
