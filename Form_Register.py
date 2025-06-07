import tkinter as tk
from tkinter import messagebox
from Class_UserManage import UserManage
from Class_User import User

class Form_Register:
    def __init__(self, parent_window, on_success):
        self.parent_window = parent_window
        self.on_success = on_success

        self.register_window = tk.Toplevel(parent_window)
        self.register_window.title("Đăng ký")
        self.register_window.geometry("300x320")
        self.register_window.resizable(False, False)

        tk.Label(self.register_window, text="Tên đăng nhập:").pack(pady=5)
        self.entry_username = tk.Entry(self.register_window)
        self.entry_username.pack(pady=5)

        tk.Label(self.register_window, text="Mật khẩu:").pack(pady=5)
        self.entry_password = tk.Entry(self.register_window, show="*")
        self.entry_password.pack(pady=5)

        tk.Label(self.register_window, text="Xác nhận mật khẩu:").pack(pady=5)
        self.entry_confirm_password = tk.Entry(self.register_window, show="*")
        self.entry_confirm_password.pack(pady=5)

        tk.Button(
            self.register_window, text="Đăng ký", width=25, bg="#28a745", fg="white",
            command=self.register_action
        ).pack(pady=10)
        tk.Button(
            self.register_window, text="Hủy", width=25, bg="#dc3545", fg="white",
            command=self.register_window.destroy
        ).pack(pady=5)
        tk.Button(
            self.register_window, text="Quay lại đăng nhập", width=25, bg="#6c757d", fg="white",
            command=self.back
        ).pack(pady=5)

    def register_action(self):
        username = self.entry_username.get().strip()
        password = self.entry_password.get().strip()
        confirm_password = self.entry_confirm_password.get().strip()

        if not username or not password or not confirm_password:
            messagebox.showwarning("Lỗi", "Vui lòng nhập đầy đủ thông tin", parent=self.register_window)
            return

        if password != confirm_password:
            messagebox.showwarning("Lỗi", "Mật khẩu xác nhận không khớp", parent=self.register_window)
            return

        user_manager = UserManage()
        if user_manager.find_user(username):
            messagebox.showwarning("Lỗi", "Tên đăng nhập đã tồn tại", parent=self.register_window)
            return

        if user_manager.add_user(username, password):
            messagebox.showinfo("Thành công", "Đăng ký thành công! Đang đăng nhập...", parent=self.register_window)
            self.register_window.destroy()
            user = User(username, password)
            self.on_success(user)
        else:
            messagebox.showerror("Lỗi", "Đăng ký thất bại", parent=self.register_window)

    def back(self):
        self.register_window.destroy()
        if self.parent_window:
            self.parent_window.deiconify()