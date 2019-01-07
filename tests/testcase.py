import os
import time
import unittest
from twilio.rest import Client

__author__ = "Alex Laird"
__copyright__ = "Copyright 2018, Alex Laird"
__version__ = "0.1.1"


class TestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client(os.environ.get("TWILIO_ACCOUNT_SID"), os.environ.get("TWILIO_AUTH_TOKEN"))

    def await_reply_message(self, now, text, retries=0):
        if retries >= 10:
            raise TimeoutError(
                "A response from the Air Quality Bot for \"{}\" was not seen after {} retries.".format(text, retries))

        time.sleep(retries * 3 if retries > 0 else 2)

        latest_message = None
        for message in self.client.messages.list(from_=os.environ.get("AIR_QUALITY_BOT_PHONE_NUMBER"),
                                                 to=os.environ.get("TWILIO_E2E_FROM_PHONE_NUMBER"),
                                                 date_sent=now.date()):
            if message.direction != "inbound" or message.date_created < now:
                continue

            latest_message = message

        if latest_message is None:
            latest_message = self.await_reply_message(now, text, retries + 1)

        return latest_message
