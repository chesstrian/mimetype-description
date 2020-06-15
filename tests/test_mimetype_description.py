import unittest

from mimetype_description import get_mime_type_description, guess_mime_type


class MimeTypeDescriptionCase(unittest.TestCase):

    def test_valid_extension(self):
        self.assertEqual(
            guess_mime_type('document.docx'),
            'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        )

    def test_invalid_extension(self):
        self.assertIsNone(guess_mime_type('document.abc'))

    def test_invalid_mime_type(self):
        self.assertIsNone(get_mime_type_description('application/x-chess'))

    def test_invalid_language(self):
        self.assertIsNone(get_mime_type_description('application/x-python', 'es-CO'))

    def test_default_language(self):
        self.assertEqual(get_mime_type_description('text/plain'), 'plain text document')

    def test_other_language(self):
        self.assertEqual(get_mime_type_description('text/plain', 'es'), 'documento de texto sencillo')


if __name__ == '__main__':
    unittest.main()
