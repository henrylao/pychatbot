import unittest
import requests

BASE = "http://127.0.0.1:5000/"


class MyTestCase(unittest.TestCase):
    def test_bot(self):
        response = requests.post(BASE + "/api/v1/bot/reply",
                                 data={"message": "Hi there! How are you doing?",
                                            "timestamp": "01/01/01",
                                            "user": "henry",
                                            })
        print(response.json())


if __name__ == '__main__':
    unittest.main()
