from src.notes_storage import NotesStorage


class NoteService:
    def __init__(self):
        self.storage = NotesStorage()

    def add(self, note):
        return self.storage.add(note)

    def average_of(self, name):
        if type(name) != str:
            raise TypeError('Name must be a string')
        notes = self.storage.get_all_notes_of(name)
        sum_of_notes = 0
        number_of_notes = len(notes)
        for note in notes:
            sum_of_notes += note
        return sum_of_notes / number_of_notes

    def clear(self):
        return self.storage.clear()
