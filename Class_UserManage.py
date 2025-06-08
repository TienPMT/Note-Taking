import json
import os

class UserManage:
    def __init__(self, filepath='Users_Data.json'):
        self.filepath = filepath
        self.users = self.load_users()
        self.current_user = None

    def load_users(self):
        if not os.path.exists(self.filepath):
            return {}
        with open(self.filepath, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
                return data
            except json.JSONDecodeError:
                return {}

    def save_users(self):
        try:
            with open(self.filepath, 'w', encoding='utf-8') as f:
                json.dump(self.users, f, indent=4, ensure_ascii=False)
        except Exception as e:
                print(f"Lỗi khi lưu file {self.filepath}: {e}")

    def find_user(self, username):
        return username in self.users

    def add_user(self, username, password):
        if self.find_user(username):
            return False
        self.users[username] = {
            'password': password,
            'notes': [],
            'role': "user"
        }
        self.save_users()
        return True

    def login(self, username, password):
        if not self.find_user(username):
            return False
        if self.users[username]['password'] == password:
            self.current_user = username
            return True
        return False
    
    def logout(self):
        self.current_user = None

    def get_user_data(self, username):
        if self.find_user(username):
            data = self.users[username].copy()
            data.pop('password', None)
            return data
        return None
    
    def update_user_notes(self, username, notes):
        # Chuyển object Note thành dict nếu có
        notes_to_save = []
        for note in notes:
            if hasattr(note, '__dict__'):
                notes_to_save.append(note.__dict__)
            elif isinstance(note, dict):
                notes_to_save.append(note)
            else:
                # Không xác định được kiểu, bỏ qua hoặc raise error
                continue
        self.users[username]['notes'] = notes_to_save
        self.save_users()
        return True
    
    def change_password(self, username, new_password):
        if username in self.users:
            self.users[username]['password'] = new_password
            self.save_users()
            return True
        else:
            return False