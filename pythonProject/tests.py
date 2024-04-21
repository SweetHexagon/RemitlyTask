import unittest
from verify_json import verify_json

class verifyJSON(unittest.TestCase):

    def test_with_asterisk(self):
        self.assertFalse(verify_json('test files/contain_asterisk.json'))

    def test_without_asterisk(self):
        self.assertTrue(verify_json('test files/not_contain_asterisk.json'))

    def test_empty_json(self):
        self.assertTrue(verify_json('test files/empty.json'))

    def test_invalid_json(self):
        with self.assertRaises(FileNotFoundError):
            verify_json('blabla.json')

if __name__ == '__main__':
    unittest.main()
