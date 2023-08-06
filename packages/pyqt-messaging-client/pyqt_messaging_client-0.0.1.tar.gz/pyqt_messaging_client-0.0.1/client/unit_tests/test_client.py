import sys
import os
import unittest
sys.path.append(os.path.join(os.getcwd(), '..'))  # правильная адресная строка, чтобы тест был универсальным

from Project_to_OOP.common.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE
from Project_to_OOP.task_3_client import create_presence, process_ans


class TestClass(unittest.TestCase):
    def test_200_response(self):
        self.assertEqual(process_ans({RESPONSE: 200}), '200 : OK')

    def test_400_response(self):
        self.assertEqual(process_ans({RESPONSE: 400, ERROR: 'Bad Request'}), '400 : Bad Request')

    def test_def_presense(self):
        test = create_presence()
        test[TIME] = 1.1
        self.assertEqual(test, {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'LoggedUser'}})


if __name__ == '__main__':
    unittest.main()