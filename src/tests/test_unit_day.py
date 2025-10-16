import unittest
from oxrse_unit_conv.units import day, hour, second


class TestDay(unittest.TestCase):
    def test_SI(self):
        self.assertTrue(day.si_unit.matches(second))

    def test_basic_conversion(self):
        self.assertEqual(day.to_si(1), 86400)
        self.assertEqual(day.to_unit(10, day), 10)

    def test_hour_conversion(self):
        self.assertEqual(day.to_unit(1, hour), 24)
        self.assertEqual(hour.to_unit(24, day), 1)


if __name__ == '__main__':
    unittest.main()