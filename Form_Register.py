# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import messagebox
from Class_UserManage import UserManage
from Class_User import User
from Form_Note import Form_Note

def dangKy(parent_window, on_success):
    register_window = tk.Toplevel(parent_window)
    register_window.title("Đăng ký")
    register_window.geometry("300x250")
    register_window.resizable(False, False)

    tk.Label(register_window, text="Tên đăng nhập:").pack(pady=5)
    entry_username = tk.Entry(register_window)
    entry_username.pack(pady=5)

    tk.Label(register_window, text="Mật khẩu:").pack(pady=5)
    entry_password = tk.Entry(register_window, show="*")
    entry_password.pack(pady=5)

    tk.Label(register_window, text="Xác nhận mật khẩu:").pack(pady=5)
    entry_confirm_password = tk.Entry(register_window, show="*")
    entry_confirm_password.pack(pady=5)

    def register_action():
        username = entry_username.get().strip()
        password = entry_password.get().strip()
        confirm_password = entry_confirm_password.get().strip()

        if not username or not password or not confirm_password:
            messagebox.showwarning("Lỗi", "Vui lòng nhập đầy đủ thông tin")
            return

        if password != confirm_password:
            messagebox.showwarning("Lỗi", "Mật khẩu xác nhận không khớp")
            return

        user_manager = UserManage()
        if user_manager.find_user(username):
            messagebox.showwarning("Lỗi", "Tên đăng nhập đã tồn tại")
            return

        if user_manager.add_user(username, password):
            messagebox.showinfo("Thành công", "Đăng ký thành công! Đang đăng nhập...")
            register_window.destroy()
            parent_window.destroy()
            user = User(username, password)
            on_success(user)
        else:
            messagebox.showerror("Lỗi", "Đăng ký thất bại")

    tk.Button(register_window, text="Đăng ký", width=25, bg="#28a745", fg="white", command=register_action).pack(pady=10)
    tk.Button(register_window, text="Hủy", width=25, bg="#dc3545", fg="white", command=register_window.destroy).pack(pady=5)

    def back():
        register_window.destroy()
        if parent_window:
            parent_window.deiconify()

    tk.Button(register_window, text="Quay lại đăng nhập", width=25, bg="#6c757d", fg="white", command=back).pack(pady=5)
