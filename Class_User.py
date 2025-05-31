# -*- coding: utf-8 -*-
from Class_Note import Note  

class User:
    def __init__(self, username, password, role="user"):
        self.username = username
        self.password = password
        self.notes = []
        self.role = role

    def to_dict(self):
        return {
            'username': self.username,
            'password': self.password,
            'role': self.role,
            'notes': [note.to_dict() for note in self.notes]
        }

    @staticmethod
    def from_dict(data):
        user = User(data['username'], data['password'], data.get('role', 'user'))
        user.notes = [Note.from_dict(n) for n in data.get('notes', [])] 
        return user

