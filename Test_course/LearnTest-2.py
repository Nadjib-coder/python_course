import unittest


class LearnTest(unittest.TestCase):
    def test_sample(self):
        a = [1, 2, 3]
        # b = [1, 3, 3]
        c = a
        # self.assertEqual(a, b, msg="1 is not equal to 10 haha")
        self.assertIs(a, c)


if __name__ == "__main__":
    unittest.main()
