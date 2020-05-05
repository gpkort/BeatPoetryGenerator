import unittest
from bs4 import BeautifulSoup
from WebScrapper import PoemsScrapper
from mock import patch





class MyTestCase(unittest.TestCase):
    # 'http://famouspoetsandpoems.com//poets/allen_ginsberg/poems/8315'
    def test_get_poem_urls_happy(self):
        with patch('requests.get') as mock_request:
            url = 'http://google.com'

            # set a `status_code` attribute on the mock object
            # with value 200
            mock_request.return_value.status_code = 200

            mock_request.assert_called_once_with(url)


        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
