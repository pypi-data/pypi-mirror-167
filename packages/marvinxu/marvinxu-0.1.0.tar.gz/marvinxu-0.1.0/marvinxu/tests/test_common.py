import unittest

import marvinxu


class TestCommon(unittest.TestCase):
    def test_is_valid_idcard(self):
        r1 = marvinxu.is_valid_idcard("441223197807234511")
        r2 = marvinxu.is_valid_idcard("441223197807234512")
        self.assertTrue(r1, "valid idcard")
        self.assertFalse(r2, "invalid idcard")


if __name__ == "__main__":
    unittest.main()
