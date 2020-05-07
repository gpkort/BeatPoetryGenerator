import unittest
from bs4 import BeautifulSoup
from WebScrapper import PoemsScrapper
from WebScrapper.UnitTests import TestData
from unittest import mock


def mocked_requests_get(*args, **kwargs):
    class MockResponse(object):
        def __init__(self, content_data, status_code):
            self.content = content_data
            self.status_code = status_code

    if args[0] == TestData.HAPPY_LINKS_URL:
        return MockResponse(TestData.GOOD_POET_LINKS, 200)
    elif args[0] == TestData.EMPTY_LINKS_URL:
        return MockResponse(TestData.EMPTY_LINKS, 200)
    elif args[0] == TestData.NOPOEM_LINKS_URL:
        return MockResponse(TestData.NO_POET_LINKS, 200)
    elif args[0] == TestData.MIXED_LINKS_URL:
        return MockResponse(TestData.MIXED_POET_LINKS, 200)
    elif args[0] == TestData.NO_CONTENT_URL:
        return MockResponse(None, 404)
    elif args[0] == TestData.BAD_CONTENT_URL:
        return MockResponse(TestData.BAD_CONTENT, 200)
    elif args[0] == TestData.HAPPY_POEM_URL:
        return MockResponse(TestData.HAPPY_POEM_TAGS, 200)
    elif args[0] == TestData.BAD_DIV_POEM_URL:
        return MockResponse(TestData.BAD_DIV_POEM_TAGS, 200)
    elif args[0] == TestData.EMPTY_DIV_POEM_URL:
        return MockResponse(TestData.EMPTY_POEM_TAGS, 200)

    return MockResponse(None, 404)


class GetPoemURLTestCases(unittest.TestCase):

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_poem_urls_happy(self, mock_get):
        links = PoemsScrapper.get_poem_urls(TestData.HAPPY_LINKS_URL)
        self.assertEqual(10, len(links))
        self.assertIn(mock.call(TestData.HAPPY_LINKS_URL), mock_get.call_args_list)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_poem_urls_empty(self, mock_get):
        self.assertRaises(PoemsScrapper.UnexpectedResponse,
                          PoemsScrapper.get_poem_urls,
                          TestData.EMPTY_LINKS_URL)
        self.assertIn(mock.call(TestData.EMPTY_LINKS_URL), mock_get.call_args_list)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_poem_urls_NoPoems(self, mock_get):
        self.assertRaises(PoemsScrapper.UnexpectedResponse,
                          PoemsScrapper.get_poem_urls,
                          TestData.NOPOEM_LINKS_URL)
        self.assertIn(mock.call(TestData.NOPOEM_LINKS_URL), mock_get.call_args_list)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_poem_urls_Mixed(self, mock_get):
        links = PoemsScrapper.get_poem_urls(TestData.MIXED_LINKS_URL)
        self.assertEqual(2, len(links))
        self.assertIn(mock.call(TestData.MIXED_LINKS_URL), mock_get.call_args_list)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_poem_urls_not_found(self, mock_get):
        self.assertRaises(PoemsScrapper.UnexpectedResponse,
                          PoemsScrapper.get_poem_urls,
                          TestData.NO_CONTENT_URL)
        self.assertIn(mock.call(TestData.NO_CONTENT_URL), mock_get.call_args_list)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_poem_urls_bad_content(self, mock_get):
        self.assertRaises(PoemsScrapper.UnexpectedResponse,
                          PoemsScrapper.get_poem_urls,
                          TestData.BAD_CONTENT_URL)
        self.assertIn(mock.call(TestData.BAD_CONTENT_URL), mock_get.call_args_list)


class GetPoemLinesTestCase(unittest.TestCase):
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_poems_tags_happy(self, mock_get):
        tags = PoemsScrapper.get_poems_tags(TestData.HAPPY_POEM_URL)
        self.assertEqual(12, len(tags))
        self.assertIn(mock.call(TestData.HAPPY_POEM_URL), mock_get.call_args_list)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_poems_tags_bad_div(self, mock_get):
        self.assertRaises(PoemsScrapper.UnexpectedResponse,
                          PoemsScrapper.get_poems_tags,
                          TestData.BAD_DIV_POEM_URL)
        self.assertIn(mock.call(TestData.BAD_DIV_POEM_URL), mock_get.call_args_list)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_poems_tags_empty_div(self, mock_get):
        self.assertRaises(PoemsScrapper.UnexpectedResponse,
                          PoemsScrapper.get_poems_tags,
                          TestData.EMPTY_DIV_POEM_URL)
        self.assertIn(mock.call(TestData.EMPTY_DIV_POEM_URL), mock_get.call_args_list)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_poem_urls_bad_content(self, mock_get):
        self.assertRaises(PoemsScrapper.UnexpectedResponse,
                          PoemsScrapper.get_poems_tags,
                          TestData.BAD_CONTENT_URL)
        self.assertIn(mock.call(TestData.BAD_CONTENT_URL), mock_get.call_args_list)


if __name__ == '__main__':
    unittest.main()
