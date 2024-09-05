import unittest
from q2 import EmailValidator

class TestEmailValidator(unittest.TestCase):
    def setUp(self):
        self.validator = EmailValidator()
        # pass
#     def test_valid_emails(self):
#         valid_emails = ['user.name+tag+sorting@example.com']
#         for email in valid_emails:
#             with self.subTest(email=email):
#                 self.assertTrue(self.validator.is_valid(email))                       


    def test_valid_emails(self):
        valid_emails = [
            'test@example.com',
            'user.name+tag+sorting@example.com',
            'user_name@example.co.uk',
            'user-name@example.com',
            'user@subdomain.example.com',
            'user@example.travel',
            'user@123.123.123.123',
            # 'user@[IPv6:2001:db8::1]'
        ]
        for email in valid_emails:
            with self.subTest(email=email):
                self.assertTrue(self.validator.is_valid(email))

    def test_invalid_emails(self):
        invalid_emails = [
            'plainaddress',
            '@missingusername.com',
            'username@.com',
            'username@domain..com',
            'username@domain.com.',
            'username@-domain.com',
            'username@domain.com-',
            'username@domain..com',
            'user@domain.c',
            'user@domain..com'
        ]
        for email in invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(self.validator.is_valid(email))

if __name__ == '__main__':
    unittest.main()