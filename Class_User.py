### models/user.py
import Class_Note

class User:
    def __init__(self, username, password, role='normal'):
        self.username = username
        self.password = password
        self.role = role
        self.notes = []

    def taoNote(self, title, content):
        note = Class_Note(title, content)
        self.notes.append(note)
        return note

    def timNote(self, keyword):
        return [note for note in self.notes if keyword in note.title or keyword in note.content]

    # Lưu vào JSON
    def to_dict(self):
        return {
            'username': self.username,
            'password': self.password,
            'role': self.role,
            'notes': [note.to_dict() for note in self.notes]
        }

    # Đọc từ JSON
    @staticmethod
    def from_dict(data):
        from Class_Note import Note
        user = User(data['username'], data['password'], data['role'])
        user.notes = [Note.from_dict(note_data) for note_data in data.get('notes', [])]
        return user