import unittest
import requests

class TestATGWorldWebsite(unittest.TestCase):

    def test_website_loads_successfully(self):
        url = 'https://atg.world'
        response = requests.get(url)
        if response.status_code == 200:
            print('The website loaded successfully!')
        else:
            print('The website did not load successfully.')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()