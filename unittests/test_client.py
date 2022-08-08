import unittest

from client import create_message_presence


class TestClass(unittest.TestCase):
    def test_create_message_presence(self):
        message = create_message_presence()
        message['time'] = 1
        self.assertEqual(message, {
            "action": "presence",
            "time": 1,
            "type": "status",
            "user": {
                "account_name": 'Guest'
            }
        })


if __name__ == '__main__':
    unittest.main()
