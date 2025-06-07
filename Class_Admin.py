from Class_User import User

class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password, 'admin')
        
    def dang_xuat(self, user_manager, admin_window):
        user_manager.logout()
        admin_window.destroy()
        from Form_Main import Form_Main
        Form_Main()
    
    def delete_user(self, username):
        from Class_UserManage import UserManage
        UserManage = UserManage()
        users_data = UserManage.load_users()
        if username in users_data:
            del users_data[username]
            UserManage.users = users_data # xoá xong sẽ cập nhật lại file json
            UserManage.save_users() 
            return True
        else:
            return False
    
    def change_password(self, username, new_password):
        from Class_UserManage import UserManage
        UserManage = UserManage()
        users_data = UserManage.load_users()
        if username in users_data:
            users_data[username]['password'] = new_password
            UserManage.users = users_data # xoá xong sẽ cập nhật lại file json
            UserManage.save_users() 
            return True
        else:
            return False
    
    def change_role(self, username):
        from Class_UserManage import UserManage
        UserManage = UserManage()
        users_data = UserManage.load_users()
        if username in users_data:
            users_data[username]['role'] = 'admin'
            UserManage.users = users_data # thay role xong sẽ cập nhật lại file json
            UserManage.save_users() 
            return True
        else:
            return False