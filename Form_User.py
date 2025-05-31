# -*- coding: utf-8 -*-

import tkinter as tk
import Form_Login
import Form_Register
import Form_Note
import Form_SearchNote
from Guest_Account import Guest

def show_user_form(user=None):
    form_chinh = tk.Toplevel()
    form_chinh.title("Note-Taking")
    form_chinh.geometry("360x480")
    form_chinh.resizable(False, False)
    form_chinh.configure(bg="white")

    # Frame chứa nút
    button_frame = tk.Frame(form_chinh, bg="white")
    button_frame.pack(fill="x")
    button_frame.columnconfigure(0, weight=1)
    button_frame.columnconfigure(1, weight=1)
    button_frame.columnconfigure(2, weight=1)

    # Nút thêm mới
    new_button = tk.Button(button_frame, text="+", font=("Times New Roman", 16),
                           command=lambda: Form_Note.show_note())
    new_button.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    def on_login_success(user):
        form_chinh.destroy()
        show_user_form(user)

    # Nút đăng nhập
    login_button = tk.Button(button_frame, text="Login", font=("Times New Roman", 16),
                             command=lambda: Form_Login.dangNhap(form_chinh, on_login_success))
    login_button.grid(row=0, column=1, padx=10, pady=10)

    def on_register_success(user):
        form_chinh.destroy()
        show_user_form(user)

    # Nút đăng ký
    register_button = tk.Button(button_frame, text="Register", font=("Times New Roman", 16),
                                command=lambda: Form_Register.dangKy(form_chinh, on_register_success))
    register_button.grid(row=0, column=2, padx=10, pady=10, sticky="e")

    # Nút dùng thử Guest
    def start_as_guest():
        guest = Guest()
        form_chinh.destroy()
        Form_Note.Form_Note(guest)

    guest_button = tk.Button(form_chinh, text="Dùng thử Guest", font=("Times New Roman", 14),
                             command=start_as_guest)
    guest_button.pack(pady=10)

    # Tiêu đề
    tk.Label(form_chinh, text="Note-Taking", font=("Times New Roman", 30, "bold"), bg="white").pack()

    # Frame tìm kiếm
    find_frame = tk.Frame(form_chinh, bg="white")
    find_frame.pack()

    find_entry = tk.Entry(find_frame, font=("Times New Roman", 16), bg="ghostwhite")
    find_entry.grid(row=2, column=0, padx=10, pady=10)

    def do_guest_search():
        guest = Guest()
        Form_SearchNote.search_note(guest)

    find_button = tk.Button(find_frame, text="Search", font=("Times New Roman", 16),
                            command=do_guest_search)
    find_button.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

    if user:
        tk.Label(form_chinh, text=f"Xin chào, {user.username}", font=("Times New Roman", 14), bg="white").pack(pady=10)

    form_chinh.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw() 
    show_user_form()
