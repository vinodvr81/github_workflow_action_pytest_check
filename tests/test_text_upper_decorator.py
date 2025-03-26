import pytest
import unittest
from unittest.mock import MagicMock
from src.text_upper_decorator import string_cap, my_type_dec


class TestTextUpperDecorator:
    @pytest.mark.parametrize(
        "a, b, expected",
        [
        ("hello", "vinod", "decorator call successful"),
        ("hello", "nevaan", "decorator call successful"),
        ("hello", "skanda", "decorator call successful")
        ])
    def test_string_cap(self, a, b, expected):
        assert string_cap(a, b) == expected

class TestTextUpperDecoratorCheck(unittest.TestCase):
    def test_string_cap(self):
        self.assertEqual(string_cap("hi", "vinod"), "decorator call successful")

    def test_my_type_dec(self):
        mock_func = MagicMock()
        mock_func.return_value = "MOCK YOURSELF VINOD"
        decorated_func = my_type_dec(mock_func)
        result = decorated_func("hi", "vinod")
        mock_func.assert_called_once_with("hi", "vinod")
        self.assertEqual(result, 'decorator call successful')

if __name__ == '__main__':
    unittest.main()
