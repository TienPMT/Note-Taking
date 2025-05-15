### models/note.py
from datetime import datetime

class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.created_at = datetime.now().isoformat()

    def to_dict(self):
        return {
            'title': self.title,
            'content': self.content,
            'created_at': self.created_at
        }

    @staticmethod
    def from_dict(data):
        note = Note(data['title'], data['content'])
        note.created_at = data['created_at']
        return note