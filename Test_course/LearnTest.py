import unittest


def _sum(a, b):
    return a + b


class LearnTest1(unittest.TestCase):
    def setUp(self):
        print('SETUP Called ...')
        # Arrange
        self.a = 10
        self.b = 20

    def tearDown(self):
        self.a = 0
        self.a = 0
        print('tearDown Called ...')

    def test_sum_func_1(self):
        print('TEST - 1 Called ...')
        # Act
        result = _sum(self.a, self.b)
        # Assert
        self.assertEqual(result, self.a + self.b)

    def test_sum_func_2(self):
        print('TEST - 2 Called ...')
        # Act
        result = _sum(self.b, self.a)
        # Assert
        self.assertEqual(result, self.a + self.b)


if __name__ == "__main__":
    unittest.main()
