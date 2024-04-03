import unittest
import sys
sys.path.append('.')
from SimpleProblem2.Cody import validate_email

class TestEmailValidation(unittest.TestCase):

    def test_valid_email(self):
        self.assertTrue(validate_email('test@example.com'))
        
    def test_invalid_email_missing_at(self):
        self.assertFalse(validate_email('testexample.com'))
        
    def test_invalid_email_too_short(self):
        self.assertFalse(validate_email('a@b.com'))

    def test_invalid_email_too_long(self):
        self.assertFalse(validate_email('a' * 50 + '@example.com'))
        
    def test_invalid_email_invalid_domain(self):
        self.assertFalse(validate_email('test@example'))

if __name__ == '__main__':
    unittest.main()