from Class_User import User
from Class_Note import Note

class Guest:
    def __init__(self):
        self.username = "Guest"  
        self.notes = []

    def add_note(self, note):
        if len(self.notes) >= 1:
            return False  
        self.notes.append(note)
        return True

    def upgrade_to_user(self, username, password):
        new_user = User(username, password)
        new_user.notes = self.notes.copy()
        return new_user
    