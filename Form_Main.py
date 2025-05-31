# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import messagebox
from Class_Guest import Guest
from Class_UserManage import UserManage
from Class_User import User
from Form_Note import Form_Note

def start_as_guest(current_window):
    guest = Guest()
    current_window.destroy()
    Form_Note(guest)

def open_register(parent_window, on_success):
    register_window = tk.Toplevel(parent_window)
    register_window.title("Đăng ký")
    register_window.geometry("300x300")
    register_window.resizable(False, False)

    tk.Label(register_window, text="Tên đăng nhập").pack(pady=5)
    entry_username = tk.Entry(register_window)
    entry_username.pack(pady=5)

    tk.Label(register_window, text="Mật khẩu").pack(pady=5)
    entry_password = tk.Entry(register_window, show="*")
    entry_password.pack(pady=5)

    tk.Label(register_window, text="Xác nhận mật khẩu").pack(pady=5)
    entry_confirm_password = tk.Entry(register_window, show="*")
    entry_confirm_password.pack(pady=5)

    def register_action():
        username = entry_username.get().strip()
        password = entry_password.get().strip()
        confirm = entry_confirm_password.get().strip()

        if not username or not password or not confirm:
            messagebox.showwarning("Lỗi", "Vui lòng nhập đầy đủ thông tin.")
            return
        if password != confirm:
            messagebox.showwarning("Lỗi", "Mật khẩu xác nhận không khớp.")
            return

        manager = UserManage()
        if manager.find_user(username):
            messagebox.showwarning("Lỗi", "Tên đăng nhập đã tồn tại.")
            return
        if manager.add_user(username, password):
            messagebox.showinfo("Thành công", "Đăng ký thành công!")
            register_window.destroy()
            parent_window.destroy()
            user = User(username, password)
            on_success(user)
        else:
            messagebox.showerror("Lỗi", "Đăng ký thất bại.")

    tk.Button(register_window, text="Đăng ký", bg="lightblue", command=register_action).pack(pady=10)
    tk.Button(register_window, text="Hủy", command=register_window.destroy).pack()

def open_login(main_window, on_success):
    main_window.withdraw()

    login_window = tk.Toplevel(main_window)
    login_window.title("Đăng nhập")
    login_window.geometry("300x200")
    login_window.resizable(False, False)

    tk.Label(login_window, text="Tên đăng nhập").pack(pady=5)
    entry_user = tk.Entry(login_window)
    entry_user.pack(pady=5)

    tk.Label(login_window, text="Mật khẩu").pack(pady=5)
    entry_pass = tk.Entry(login_window, show="*")
    entry_pass.pack(pady=5)

    def try_login():
        username = entry_user.get().strip()
        password = entry_pass.get().strip()
        if not username or not password:
            messagebox.showwarning("Lỗi", "Vui lòng nhập đầy đủ tên đăng nhập và mật khẩu.")
            return
        manager = UserManage()
        if manager.login(username, password):
            user = User(username, password)
            login_window.destroy()
            main_window.destroy()
            on_success(user)
        else:
            messagebox.showerror("Thất bại", "Sai tên đăng nhập hoặc mật khẩu.")

    tk.Button(login_window, text="Đăng nhập", command=try_login).pack(pady=10)
    tk.Button(login_window, text="Đăng ký", command=lambda: open_register(login_window, on_success)).pack(pady=5)

    def on_close():
        login_window.destroy()
        main_window.deiconify()
    login_window.protocol("WM_DELETE_WINDOW", on_close)

def show_main_form():
    root = tk.Tk()
    root.title("Ghi chú App")
    root.geometry("360x300")
    root.resizable(False, False)

    tk.Label(root, text="Chào mừng đến với Note App", font=("Arial", 16, "bold")).pack(pady=20)

    def on_login_success(user):
        from Form_Note import Form_Note
        Form_Note(user)

    tk.Button(root, text="Đăng nhập / Đăng ký", width=25, command=lambda: open_login(root, on_login_success)).pack(pady=10)
    tk.Button(root, text="Dùng thử với Guest", width=25, command=lambda: start_as_guest(root)).pack(pady=10)
    tk.Button(root, text="Thoát", width=15, command=root.destroy).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    show_main_form()
