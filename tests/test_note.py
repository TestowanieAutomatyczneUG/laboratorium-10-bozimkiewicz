from src.note import Note
import unittest


class TestNote(unittest.TestCase):
    def test_init(self):
        Note('Bartek', 5.0)

    def test_note_disallow_name_type_not_string(self):
        self.assertRaises(TypeError, Note, 0, 5.0)

    def test_note_disallow_name_none(self):
        self.assertRaises(TypeError, Note, None, 5.0)

    def test_note_disallow_name_empty(self):
        self.assertRaises(ValueError, Note, '', 5.0)

    def test_note_disallow_note_type_not_float(self):
        self.assertRaises(TypeError, Note, 'Bartek', '5')

    def test_note_disallow_note_wrong_value(self):
        self.assertRaises(ValueError, Note, 'Bartek', 4.2)

    def test_note_disallow_note_too_low(self):
        self.assertRaises(ValueError, Note, 'Bartek', 1.0)

    def test_note_disallow_note_too_high(self):
        self.assertRaises(ValueError, Note, 'Bartek', 7.0)

    def test_note_get_name(self):
        self.assertEqual(Note('Bartek', 5.0).get_name(), 'Bartek')

    def test_note_get_note(self):
        self.assertEqual(Note('Bartek', 5.0).get_note(), 5.0)


if __name__ == '__main__':
    unittest.main()
