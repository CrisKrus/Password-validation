import unittest


def validatePassword(password):
    return False


class TestPasswordValidation(unittest.TestCase):

    def test__given_password_with_less_than_eight_chars(self):
        self.assertFalse(validatePassword(['q', 'w', 'e', 'r', 't']))
        self.assertTrue(validatePassword(['q', 'w', 'e', 'r', 't', 'y', 'u', 'i']))
