# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class AccessTokenTestCase(IntegrationTestCase):

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.verify.v2.services("VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .entities("identity") \
                                 .access_tokens.create(factor_type="push")

        values = {'FactorType': "push", }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://verify.twilio.com/v2/Services/VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Entities/identity/AccessTokens',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "token": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.verify.v2.services("VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .entities("identity") \
                                      .access_tokens.create(factor_type="push")

        self.assertIsNotNone(actual)