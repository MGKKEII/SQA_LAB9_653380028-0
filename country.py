import requests

class Country:
    def __init__(self):
        self.country_name_response = None
        self.api_url = "https://example-country.com/name"

    def get_country_name(self):
        """
        Method to get data/response from API
        """
        try:
            response = requests.get(self.api_url)
            if response.status_code in (200, 201):
                self.country_name_response = response.json()
        except requests.exceptions.RequestException:
            self.country_name_response = None

    def get_country_name_start_with_letter(self, letter="a"):
        """
        Method to query the country name starting with specific letter
        """
        self.get_country_name()
        if not self.country_name_response:
            return []

        all_country_name = self.country_name_response.get("data", [])
        result = [name for name in all_country_name if name.lower().startswith(letter.lower())]
        return result
