### models/user_manage.py
import json
import Class_User

class UserManage:
    def __init__(self):
        self.users = []
    
    def docDuLieu(self):
        try:
            with open("Users_Data.JSON", 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.users = [Class_User.User.from_dict(user_data) for user_data in data]
        except FileNotFoundError:
            self.users = []
    
    def register(self, username, password):
        if self.get_user(username):
            raise Exception("Username đã tồn tại.")
        new_user = Class_User(username, password)
        self.users.append(new_user)
        return new_user

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return user
        return None

    def get_user(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None

    def save_to_file(self, filename):
        data = [user.to_dict() for user in self.users]
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
