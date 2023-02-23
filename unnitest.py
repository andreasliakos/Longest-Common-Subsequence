import unittest
from lcs import brute_force, lcs, lcs_table

class MyTestCase(unittest.TestCase):
    # test brute force method
    def test_brute_force(self):
        X = "AATCGAG"
        Y = "CCATCGG"
        self.assertEqual(brute_force(X, Y), (5, "ATCGG"))

    # test lcs method
    def test_lcs(self):
        X = "AATCGAG"
        Y = "CCATCGG"
        self.assertEqual(lcs(X, Y), (5, "ATCGG"))

    # test lcs table method
    def test_lcs_table_list(self):
        self.assertEqual(
            lcs_table("ABCDE", "CEFGH"),
            [
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1],
                [0, 1, 1, 1, 1, 1],
                [0, 1, 2, 2, 2, 2],
            ],
        )


if __name__ == "__main__":
    unittest.main()
