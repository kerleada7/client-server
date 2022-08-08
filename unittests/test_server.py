import unittest

from server import process_client_message


class TestClass(unittest.TestCase):
    def test_process_client_message(self):
        client_message = {
            "action": "presence",
            "time": 1,
            "type": "status",
            "user": {
                "account_name": 'Guest'
            }
        }
        server_message = process_client_message(client_message)
        server_message['time'] = 1
        self.assertEqual(server_message, {
            "response": 200,
            "time": 1,
            "alert": 'OK'
        })


if __name__ == '__main__':
    unittest.main()
