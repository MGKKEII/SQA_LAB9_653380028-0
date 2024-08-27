from io import BytesIO
from requests.models import Response

def get_mock_currency_api_response():
    """
    Method to create a mock response for the currency exchange API
    """
    mock_api_response = Response()
    mock_api_response.status_code = 200
    mock_api_response._content = b'{ "rate": 0.03 }'
    return mock_api_response
