import unittest
from filter import filter_magnitude


class TestMagnitudeFiltser(unittest.TestCase):
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
        entry = filter_magnitude(self.data, 5.0, 5.0)

        self.assertEqual(entry, expected)

    def test_string_params(self):
        """Should accept parameters as string"""
        total = len(filter_magnitude(self.data, "2.0", "2.0"))

        self.assertEqual(total, 2)

    def test_float_params(self):
        """Should accept parameters as float"""
        total = len(filter_magnitude(self.data, 2.0, 2.0))

        self.assertEqual(total, 2)

    def test_filter_range(self):
        total = len(filter_magnitude(self.data, "1.0", "2.0"))

        self.assertEqual(total, 3)

    def test_noparams(self):
        total = len(filter_magnitude(self.data))

        self.assertEqual(total, 7)