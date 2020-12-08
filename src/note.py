class Note:
    def __init__(self, name, note):
        if type(name) is not str:
            raise TypeError('Name must be a string')
        if name is None:
            raise TypeError('Name cannot be None')
        if name == '':
            raise ValueError('Name cannot be empty')
        if type(note) is not float:
            raise TypeError('Note must be a float')
        if note not in [2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0]:
            raise ValueError('Note must be in between 2 and 6')

        self.name = name
        self.note = note

    def get_name(self):
        return self.name

    def get_note(self):
        return self.note
