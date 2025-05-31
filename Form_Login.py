# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import messagebox
from Class_UserManage import UserManage
from Class_User import User
from Form_Note import Form_Note

def dangNhap(parent_window, on_success):
    login_window = tk.Toplevel(parent_window)
    login_window.title("Đăng nhập")
    login_window.geometry("300x230")
    login_window.resizable(False, False)

    tk.Label(login_window, text="Tên đăng nhập:").pack(pady=5)
    entry_username = tk.Entry(login_window)
    entry_username.pack(pady=5)

    tk.Label(login_window, text="Mật khẩu:").pack(pady=5)
    entry_password = tk.Entry(login_window, show="*")
    entry_password.pack(pady=5)

    def login_action():
        username = entry_username.get().strip()
        password = entry_password.get().strip()
        if not username or not password:
            messagebox.showwarning("Lỗi", "Vui lòng nhập đầy đủ tên đăng nhập và mật khẩu")
            return

        user_manager = UserManage()
        if user_manager.login(username, password):
            # Lấy thông tin user từ database
            user_data = user_manager.users.get(username)
            role = user_data.get('role', 'user')
            # Tạo đối tượng User với role tương ứng
            user = User(username, password, role)
            
            # Thông báo tùy theo role
            if user.role == 'admin':
                messagebox.showinfo("Thành công", f"Đăng nhập ADMIN thành công! Chào {username}")
            else:
                messagebox.showinfo("Thành công", f"Đăng nhập thành công! Chào {username}")
        
            # Đóng cửa sổ và gọi callback
            login_window.destroy()
            parent_window.destroy()
            on_success(user)
        else:
            messagebox.showerror("Lỗi", "Tên đăng nhập hoặc mật khẩu không đúng")

    def open_register():
        from Form_Register import dangKy
        dangKy(login_window, on_success)

    tk.Button(login_window, text="Đăng nhập", command=login_action).pack(pady=10)
    tk.Button(login_window, text="Đăng ký", command=open_register).pack(pady=5)
    tk.Button(login_window, text="Hủy", command=login_window.destroy).pack()
