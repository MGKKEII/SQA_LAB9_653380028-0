from unittest.mock import patch
import unittest
from currency_exchanger import CurrencyExchanger
from utils import get_mock_currency_api_response

class TestCurrencyExchanger(unittest.TestCase):
    def setUp(self):
        self.exchanger = CurrencyExchanger()
        self.mock_api_response = get_mock_currency_api_response()

    @patch("requests.get")
    def test_get_currency_rate(self, mock_get):
        # Assign mock's return value
        mock_get.return_value = self.mock_api_response

        # Act - execute class under test
        self.exchanger.get_currency_rate()

        # Check whether the mocked method is called
        mock_get.assert_called_once()

        # Check whether the mocked method is called with the right parameters
        params = {'from': self.exchanger.base_currency, 'to': self.exchanger.target_currency}
        mock_get.assert_called_with(self.exchanger.currency_api, params=params)

        # Assert the returned responses
        self.assertIsNotNone(self.exchanger.api_response)
        self.assertEqual(self.exchanger.api_response, self.mock_api_response.json())

    @patch("requests.get")
    def test_currency_exchange(self, mock_get):
        mock_get.return_value = self.mock_api_response

        amount = 100
        result = self.exchanger.currency_exchange(amount)

        # Check if the exchange rate was used correctly
        expected_result = amount * self.mock_api_response.json()['rate']
        self.assertEqual(result, expected_result)

        # Check that the mock request was called with correct parameters
        params = {'from': self.exchanger.base_currency, 'to': self.exchanger.target_currency}
        mock_get.assert_called_once_with(self.exchanger.currency_api, params=params)

if __name__ == '__main__':
    unittest.main()
