import unittest
from oxrse_unit_conv.units import kelvin, celsius


class TestCelsius(unittest.TestCase):
    def test_SI(self):
        self.assertTrue(celsius.si_unit.matches(kelvin))

    def test_basic_conversion(self):
        self.assertEqual(celsius.to_si(-273.15), 0)
        self.assertEqual(celsius.to_unit(0, celsius), 0)


if __name__ == '__main__':
    unittest.main()
