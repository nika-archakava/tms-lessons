import unittest
from unittest.mock import patch, Mock

import requests

from Joining_words import join_words
import datetime


def my_print(text, visible=True):
    if visible:
        print(text)


def mocked_get(*args, **kwargs):
    return join_words("badger", "racoon")


def mocked_get_1(*args, **kwargs):
    return 404


class JoinTwoWords(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("A test suite begins")

    @classmethod
    def tearDownClass(cls):
        print("A test suite ends")

    def setUp(self):
        print("A test begins")

    def tearDown(self):
        print("A test ends")

    def test_join_words(self):
        result = join_words('Hi', 'Veranika')

        self.assertEqual(result, 'Hi-Veranika')

    def test_exception(self):
        with self.assertRaises(TypeError):
            join_words('hello', 'hey', 'Good_afternoon')

    @unittest.skip("Not good!")
    def test_skip_test(self):
        raise Exception("No No No")

    @unittest.expectedFailure
    def test_xfail(self):
        result = join_words('hello', 'world')

        self.assertEqual(result, Helloworld)

    @patch("requests.get", side_effect=mocked_get)
    def test_mock(self, mock):
        response = requests.get("https://www.google.com/search?q=badger")
        self.assertEqual(response, "badger-racoon")

    @unittest.skipIf(datetime.date.today().weekday() in [0, 2, 4], "Because weekday is Monday, Wednesday, Friday")
    def test_skip_if_test(self):
        raise Exception("!!!!!!!")

    @patch("requests.get", side_effect=mocked_get_1)
    def test_mock1(self, mock):
        response = requests.get("https://www.google.com/")
        self.assertEqual(response, 404)
