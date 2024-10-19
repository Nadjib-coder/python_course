import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self):
        # Set up resources needed for tests
        self.file = open("test_file.txt", "w")

    def tearDown(self):
        # Clean up resources after tests
        self.file.close()
        # Clean up any other resources if needed

    def test_file_write(self):
        self.file.write("Hello, World!")
        self.file.seek(0)
        content = self.file.read()
        self.assertEqual(content, "Hello, World!")

    def test_file_append(self):
        self.file.write("Second Test")
        self.file.seek(0)
        content = self.file.read()
        self.assertEqual(content, "Second Test")


if __name__ == '__main__':
    unittest.main()
