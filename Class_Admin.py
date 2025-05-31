# -*- coding: utf-8 -*-
    
import Class_User

class Admin(Class_User):
    def __init__(self, username, password):
        super().__init__(username, password, 'admin')

    def view_all_users(self, users):
        return [(user.username, len(user.notes)) for user in users if user.role != 'admin']