import unittest
from filter import filter_year


class TestYearFilter(unittest.TestCase):
    def setUp(self):
        self.data = [
            {"mag": "5.0", "date": "1999-01-01", "place": "Groningen"},
            {"mag": "2.0", "date": "2000-01-01", "place": "Siddeburen"},
            {"mag": "3.5", "date": "2000-01-02", "place": "Appingedam"},
            {"mag": "0.5", "date": "2001-01-01", "place": "Siddeburen"},
            {"mag": "4.0", "date": "2001-01-02", "place": "Garrelsweer"},
            {"mag": "1.0", "date": "2002-01-01", "place": "Loppersum"},
            {"mag": "2.0", "date": "2002-01-02", "place": "Winneweer"},
        ]

    def test_match(self):
        expected = [self.data[0].copy()]
        entry = filter_year(self.data, 1999, 1999)

        self.assertEqual(entry, expected)

    def test_string_params(self):
        """Should accept parameters as string"""
        total = len(filter_year(self.data, "2000", "2000"))

        self.assertEqual(total, 2)

    def test_integer_params(self):
        """Should accept parameters as integer"""
        total = len(filter_year(self.data, 2000, 2000))

        self.assertEqual(total, 2)

    def test_filter_range(self):
        total = len(filter_year(self.data, "2000", "2001"))

        self.assertEqual(total, 4)

    def test_noparams(self):
        total = len(filter_year(self.data))

        self.assertEqual(total, 7)
