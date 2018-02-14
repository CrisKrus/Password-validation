import unittest


class TestPasswordValidation(unittest.TestCase):

    def test__given_password_with_less_than_eight_chars(self):
        self.assertEqual(False, validatePassword(['q', 'w', 'e', 'r', 't']))
