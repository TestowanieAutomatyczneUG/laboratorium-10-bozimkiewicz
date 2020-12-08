from src.note import Note
from src.notes_storage import NotesStorage
from src.notes_service import NoteService
import unittest
from unittest.mock import *


class TestNoteService(unittest.TestCase):
    def setUp(self):
        self.temp = NoteService()

    @patch.object(NotesStorage, 'add')
    def test_notes_service_add(self, mock_method):
        mock_method.return_value = True
        self.assertEqual(self.temp.add(Note('Bartek', 5.0)), True)

    @patch.object(NotesStorage, 'get_all_notes_of')
    def test_notes_service_average_of(self, mock_method):
        mock_method.return_value = [3.5, 4.5]
        self.assertEqual(self.temp.average_of('Bartek'), 4.0)

    def test_note_disallow_service_get_all_notes_of_name_not_string(self):
        self.assertRaises(TypeError, Note, 0, 5.0)

    @patch.object(NotesStorage, 'clear')
    def test_note_service_clear(self, mock_method):
        mock_method.return_value = True
        self.assertEqual(self.temp.clear(), True)


if __name__ == '__main__':
    unittest.main()
