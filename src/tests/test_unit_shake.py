import unittest
from oxrse_unit_conv.units import shake, s


class TestShake(unittest.TestCase):
    def test_SI(self):
        self.assertTrue(shake.si_unit.matches(s))

    def test_basic_conversion(self):
        self.assertEqual(shake.to_si(1), 1/10**8)
        self.assertEqual(shake.to_unit(10, shake), 10)


if __name__ == '__main__':
    unittest.main()
