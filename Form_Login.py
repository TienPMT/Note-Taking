import tkinter as tk
from tkinter import messagebox
from Class_UserManage import UserManage
from Class_User import User

class Form_Login:
    def __init__(self, parent_window, on_success):
        self.parent_window = parent_window
        self.on_success = on_success
        self.parent_window.withdraw()
        # ========== CỬA SỔ ĐĂNG NHẬP ==========
        self.window = tk.Toplevel(parent_window)
        self.window.title("Đăng nhập")
        self.window.geometry("350x260")
        self.window.resizable(False, False)
        self.window.grab_set()  # Chặn tương tác với parent_window

        # ========== TIÊU ĐỀ ==========
        tk.Label(self.window, text="ĐĂNG NHẬP", font=("Segoe UI", 14, "bold"), fg="#1976d2").pack(pady=(15, 8))

        # ========== INPUT ==========
        frame = tk.Frame(self.window)
        frame.pack(pady=5, padx=15, fill="x")

        tk.Label(frame, text="Tên đăng nhập:", anchor="w").pack(fill="x", pady=(0,2))
        self.entry_username = tk.Entry(frame, font=("Segoe UI", 11))
        self.entry_username.pack(fill="x", pady=(0,8))
        self.entry_username.focus_set()

        tk.Label(frame, text="Mật khẩu:", anchor="w").pack(fill="x", pady=(0,2))
        self.entry_password = tk.Entry(frame, show="*", font=("Segoe UI", 11))
        self.entry_password.pack(fill="x")

        # ========== BUTTON ==========
        btn_frame = tk.Frame(self.window)
        btn_frame.pack(pady=15)

        tk.Button(btn_frame, text="Đăng nhập", width=14, bg="#1976d2", fg="white", font=("Segoe UI", 10, "bold"),
                  command=self.login_action, cursor="hand2").grid(row=0, column=0, padx=5, ipadx=2)
        tk.Button(btn_frame, text="Đăng ký", width=10, bg="#43a047", fg="white", font=("Segoe UI", 10),
                  command=self.open_register, cursor="hand2").grid(row=0, column=1, padx=5, ipadx=2)
        tk.Button(btn_frame, text="Hủy", width=8, bg="#f44336", fg="white", font=("Segoe UI", 10),
                  command=self.on_cancel, cursor="hand2").grid(row=0, column=2, padx=5, ipadx=2)
        self.window.protocol("WM_DELETE_WINDOW", self.on_cancel)
    
    def on_cancel(self):
        self.window.destroy()
        self.parent_window.deiconify()  # Hiện lại cửa sổ cha

    def login_action(self):
        username = self.entry_username.get().strip()
        password = self.entry_password.get().strip()
        if not username or not password:
            messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập đầy đủ tên đăng nhập và mật khẩu.", parent=self.window)
            return

        user_manager = UserManage()
        if user_manager.login(username, password):
            user_data = user_manager.users.get(username)
            role = user_data.get('role', 'user')
            # Tạo object user đúng loại
            if role == 'admin':
                from Class_Admin import Admin
                user = Admin(username, password)
            else:
                user = User(username, password, role)
            
            # Thông báo
            if user.role == 'admin':
                messagebox.showinfo("Thành công", f"Đăng nhập ADMIN thành công! Chào {username}", parent=self.window)
            else:
                messagebox.showinfo("Thành công", f"Đăng nhập thành công! Chào {username}", parent=self.window)
            
            self.window.destroy()
            self.on_success(user)
        else:
            messagebox.showerror("Lỗi", "Tên đăng nhập hoặc mật khẩu không đúng.", parent=self.window)

    def open_register(self):
        from Form_Register import Form_Register
        self.window.withdraw()
        def after_register(user=None):
            self.window.deiconify()
            if user:
                self.window.destroy()
                self.on_success(user)
        Form_Register(self.window, after_register)