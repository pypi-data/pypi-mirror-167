import sys
import os
import unittest

sys.path.append(os.path.join(os.getcwd(), '..'))

from Project_to_OOP.common.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE
from Project_to_OOP.task_3_server import process_client_message


class TestServer(unittest.TestCase):
    error = {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }
    test_passed = {RESPONSE: 200}

    def test_no_error(self):
        """Корректный запрос"""
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}}), self.test_passed)

    def test_unknown_user(self):
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}}), self.error)

    def test_user_not_stated(self):
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME: '1.1'}), self.error)


if __name__ == '__main__':
    unittest.main()
