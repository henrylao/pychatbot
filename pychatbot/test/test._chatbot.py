import unittest
import requests
import datetime as dt
import pytz

BASE = "http://127.0.0.1:5000/"


class MyTestCase(unittest.TestCase):
    def test_bot_POST(self):
        datetime_fmt = "%a, %d %b %Y %H:%M:%S %Z"
        tz = pytz.timezone("US/Pacific")
        payload = {"message": "Hi there! How are you doing?",
                   "created_at": dt.datetime.strftime(dt.datetime.now(tz=tz), datetime_fmt),
                   "user": "henry",
                   }
        print("POST request:", payload)
        response = requests.post(BASE + "/api/v1/bot/reply",
                                 data=payload)
        print("POST response:", response.json())


if __name__ == '__main__':
    unittest.main()
