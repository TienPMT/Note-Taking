import tkinter as tk
import Form_Login
import Form_Register
import Form_Note
import Form_SearchNote
from Guest_Account import Guest

def show_guest_form():
    guest_window = tk.Tk()
    guest_window.title("Guest - Note Taking")
    guest_window.geometry("360x480")
    guest_window.resizable(False, False)
    guest_window.configure(bg="white")

    # Frame chứa các nút: Thêm mới, Đăng nhập, Đăng ký
    button_frame = tk.Frame(guest_window, bg="white")
    button_frame.pack(fill="x", pady=10)
    button_frame.columnconfigure(0, weight=1)
    button_frame.columnconfigure(1, weight=1)
    button_frame.columnconfigure(2, weight=1)

    # Nút thêm mới (chức năng Guest)
    new_button = tk.Button(button_frame, text="+", font=("Times New Roman", 16),
                           command=lambda: Form_Note.show_note())
    new_button.grid(row=0, column=0, padx=10, sticky="w")

    # Nút Đăng nhập
    def on_login_success(user):
        guest_window.destroy()
        from Form_User import show_user_form
        show_user_form(user)

    login_button = tk.Button(button_frame, text="Đăng nhập", font=("Times New Roman", 16),
                             command=lambda: Form_Login.dangNhap(guest_window, on_login_success))
    login_button.grid(row=0, column=1, padx=10)

    # Nút Đăng ký
    def on_register_success(user):
        guest_window.destroy()
        from Form_User import show_user_form
        show_user_form(user)

    register_button = tk.Button(button_frame, text="Đăng ký", font=("Times New Roman", 16),
                                command=lambda: Form_Register.dangKy(guest_window, on_register_success))
    register_button.grid(row=0, column=2, padx=10, sticky="e")

    # Tiêu đề
    tk.Label(guest_window, text="Note-Taking (Guest)", font=("Times New Roman", 30, "bold"), bg="white").pack(pady=20)

    # Frame tìm kiếm
    find_frame = tk.Frame(guest_window, bg="white")
    find_frame.pack(pady=10)

    find_entry = tk.Entry(find_frame, font=("Times New Roman", 16), bg="ghostwhite")
    find_entry.grid(row=0, column=0, padx=10)

    def do_guest_search():
        guest = Guest()
        Form_SearchNote.search_note(guest)

    find_button = tk.Button(find_frame, text="Search", font=("Times New Roman", 16),
                            command=do_guest_search)
    find_button.grid(row=0, column=1, padx=10)

    guest_window.mainloop()

if __name__ == "__main__":
    show_guest_form()
