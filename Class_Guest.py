### models/guest.py
import Class_User

class Guest(Class_User):
    def __init__(self):
        super().__init__('guest', '', 'guest')

    def create_note(self, title, content):
        if len(self.notes) >= 1:
            raise Exception("Guest chỉ được tạo 1 note. Vui lòng đăng nhập để tạo thêm.")
        return super().create_note(title, content)

    def upgrade_to_user(self, username, password):
        from models.user import User
        new_user = User(username, password)
        new_user.notes = self.notes.copy()
        return new_user
