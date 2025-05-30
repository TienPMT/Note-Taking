# -*- coding: utf-8 -*-

import json
import os
import hashlib

class UserManage:
    def __init__(self, filepath='Users_Data.json'):
        self.filepath = filepath
        self.users = self.load_users()

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


    def hash_password(self, password):
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def find_user(self, username):
        return username in self.users

    def add_user(self, username, password):
        if self.find_user(username):
            return False
        hashed_pw = self.hash_password(password)
        self.users[username] = {
            'password': hashed_pw,
            'notes': [],
            'role': "user"
        }
        self.save_users()
        return True

    def login(self, username, password):
        if not self.find_user(username):
            return False
        hashed_pw = self.hash_password(password)
        if self.users[username]['password'] == hashed_pw:
            return True
        return False

    def get_user_data(self, username):
     
        if self.find_user(username):
            data = self.users[username].copy()
            data.pop('password', None)
            return data
        return None
    
    def update_user_notes(self, username, notes):
        if not self.find_user(username):
            return False
        self.users[username]['notes'] = notes
        self.save_users()
        return True