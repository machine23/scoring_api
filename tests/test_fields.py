import unittest
from api import CharField, ArgumentsField, EmailField


class TestCharField(unittest.TestCase):
    def test_not_nullable(self):
        f = CharField()
        self.assertEqual('test', f.clean('test'))
        with self.assertRaisesRegex(ValueError, r'This field cannot be empty.'):
            f.clean('')
        with self.assertRaisesRegex(ValueError, r'This field cannot be empty.'):
            f.clean(None)
        with self.assertRaisesRegex(ValueError, r'This field must be a string.'):
            f.clean(123)

    def test_nullable(self):
        f = CharField(nullable=True)
        self.assertEqual('', f.clean(None))
        self.assertEqual('', f.clean(''))
        self.assertEqual('test', f.clean('test'))
        with self.assertRaisesRegex(ValueError, r'This field must be a string.'):
            f.validate(123)


class TestArgumentsField(unittest.TestCase):
    def test_not_nullable(self):
        f = ArgumentsField()
        self.assertEqual({'a': 'b'}, f.clean({'a': 'b'}))
        with self.assertRaisesRegex(ValueError, r'This field cannot be empty.'):
            f.clean({})
        with self.assertRaisesRegex(ValueError, r'This field cannot be empty.'):
            f.clean(None)
        with self.assertRaisesRegex(ValueError, r'This field must be a dict.'):
            f.clean('123')

    def test_nullable(self):
        f = ArgumentsField(nullable=True)
        self.assertEqual({}, f.clean(None))
        self.assertEqual({}, f.clean({}))
        self.assertEqual({'a': 'b'}, f.clean({'a': 'b'}))
        with self.assertRaisesRegex(ValueError, r'This field must be a dict.'):
            f.clean(123)


class TestEmailField(unittest.TestCase):
    def test_not_nullable(self):
        f = EmailField()
        self.assertEqual('a@b.c', f.clean('a@b.c'))
        with self.assertRaisesRegex(ValueError, r'This field cannot be empty.'):
            f.clean('')
        with self.assertRaisesRegex(ValueError, r'This field cannot be empty.'):
            f.clean(None)
        with self.assertRaisesRegex(ValueError, r'Not valid email.'):
            f.clean('123')

    def test_nullable(self):
        f = EmailField(nullable=True)
        self.assertEqual('', f.clean(None))
        self.assertEqual('', f.clean(''))
        self.assertEqual('a@b.c', f.clean('a@b.c'))
        with self.assertRaisesRegex(ValueError, r'Not valid email.'):
            f.clean('123')



if __name__ == '__main__':
    unittest.main()
