__copyright__ = "Copyright (c) 2018-2019 Alex Laird"
__license__ = "MIT"

import os
import time
import unittest

from .testcase import TestCase


class TestCaseE2E(TestCase):
    def tearDown(self):
        time.sleep(2)

    @unittest.skipIf("TWILIO_AUTH_TOKEN" not in os.environ, "TWILIO_AUTH_TOKEN environment variable not set")
    def test_text(self):
        text = "text"

        message = self.client.messages.create(
            to=os.environ.get("AIR_QUALITY_BOT_PHONE_NUMBER"),
            from_=os.environ.get("TWILIO_E2E_FROM_PHONE_NUMBER"),
            body=text)

        message = self.await_reply_message(message.date_created, text)

        self.assertEqual(message.body,
                         "Send us a zip code and we'll reply with the area's Air Quality Index (AQI). Put \"map\" at the end and we'll include the regional map too.")

    @unittest.skipIf("TWILIO_AUTH_TOKEN" not in os.environ, "TWILIO_AUTH_TOKEN environment variable not set")
    def test_00000(self):
        text = "00000"

        message = self.client.messages.create(
            to=os.environ.get("AIR_QUALITY_BOT_PHONE_NUMBER"),
            from_=os.environ.get("TWILIO_E2E_FROM_PHONE_NUMBER"),
            body=text)

        message = self.await_reply_message(message.date_created, text)

        self.assertEqual(message.body, "Sorry, AirNow data is unavailable for this zip code.")

    @unittest.skipIf("TWILIO_AUTH_TOKEN" not in os.environ, "TWILIO_AUTH_TOKEN environment variable not set")
    def test_94501(self):
        text = "94501"

        message = self.client.messages.create(
            to=os.environ.get("AIR_QUALITY_BOT_PHONE_NUMBER"),
            from_=os.environ.get("TWILIO_E2E_FROM_PHONE_NUMBER"),
            body=text)

        message = self.await_reply_message(message.date_created, text)

        self.assertEqual(message.num_media, "0")
        self.assertIn(" AQI of ", message.body)
        self.assertIn(" for Oakland at ", message.body)
        self.assertIn("Source: AirNow", message.body)

    @unittest.skipIf("TWILIO_AUTH_TOKEN" not in os.environ, "TWILIO_AUTH_TOKEN environment variable not set")
    def test_94501_map(self):
        text = "94501 map"

        message = self.client.messages.create(
            to=os.environ.get("AIR_QUALITY_BOT_PHONE_NUMBER"),
            from_=os.environ.get("TWILIO_E2E_FROM_PHONE_NUMBER"),
            body=text)

        message = self.await_reply_message(message.date_created, text)

        self.assertEqual(message.num_media, "1")
        self.assertIn(" AQI of ", message.body)
        self.assertIn(" for Oakland at ", message.body)
        self.assertIn("Source: AirNow", message.body)


if __name__ == "__main__":
    unittest.main()
