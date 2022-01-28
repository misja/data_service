import unittest
from filter import filter_place


class TestPlaceFilter(unittest.TestCase):
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
        entry = filter_place(self.data, "Gron")

        self.assertEqual(entry, expected)

    def test_lowercase(self):
        total = len(filter_place(self.data, "groningen"))

        self.assertEqual(total, 1)

    def test_uppercase(self):
        total = len(filter_place(self.data, "EN"))

        self.assertEqual(total, 3)

    def test_mixedcase(self):
        total = len(filter_place(self.data, "Weer"))

        self.assertEqual(total, 2)

    def test_noparams(self):
        total = len(filter_place(self.data))

        self.assertEqual(total, 7)
