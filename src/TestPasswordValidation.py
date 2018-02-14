import unittest


def validate_password(password):
    if len(password) < 8:
        return False


class TestPasswordValidation(unittest.TestCase):

    def test__given_password_with_less_than_eight_chars(self):
        self.assertFalse(validate_password(['q', 'w', 'e', 'r', 't']))

