"""
Write a test for your Bitcoin program (from the API topic) that converts a number of Bitcoin to their value in US Dollars.

Structure your program so you don't need to mock user input. 

Structure your program so it's possible to isolate and then mock the API call. 

Mock the API call by providing a mock JSON response. Assert that your program calculates the correct value in dollars.

To submit: a link to your GitHub repository.
"""

import bitcoin

import unittest
from unittest import TestCase
from unittest.mock import patch

class TestTimeSheet(TestCase):
    """ mock input() and force it to return a value """

    @patch('builtins.input', side_effect=['2'])
    def test_get_bitcoin_amount(self, mock_input):
        mock_api_call = {'time': 
            {'updated': 'Feb 28, 2024 21:40:46 UTC', 'updatedISO': '2024-02-28T21:40:46+00:00', 
            'updateduk': 'Feb 28, 2024 at 21:40 GMT'}, 'disclaimer': 'This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org', 
            'chartName': 'Bitcoin', 
            'bpi': {'USD': {'code': 'USD', 'symbol': '&#36;', 
            'rate': '60,502.017', 'description': 'United States Dollar', 'rate_float': 60502.0172}, 
            'GBP': {'code': 'GBP', 'symbol': '&pound;', 'rate': '47,786.308', 
            'description': 'British Pound Sterling', 'rate_float': 47786.3082}, 
            'EUR': {'code': 'EUR', 'symbol': '&euro;', 'rate': '55,823.517', 
            'description': 'Euro', 'rate_float': 55823.5172}}}
        bitcoin_amount = bitcoin.user_input()
        bitcoin_amount_in_dollars = bitcoin.dollar_value_of_bitcoin(bitcoin_amount, mock_api_call['bpi']['USD']['rate_float'])
        self.assertEqual(121004.0344, bitcoin_amount_in_dollars)


if __name__ == '__main__': # doing this allows you to run unit test without typing it into console everytime.
    unittest.main()