from Class_User import User

class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password, 'admin')
        
    def dang_xuat(self, user_manager, admin_window):
        user_manager.logout()
        admin_window.destroy()
        from Form_Main import show_main_form
        show_main_form()
    
    