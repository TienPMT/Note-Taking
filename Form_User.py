import tkinter as tk
import Form_Login
import Form_Note
import Form_Guest
import Class_User

def show_user_form(user):
    # Xây dựng khung
    form_chinh = tk.Tk()
    form_chinh.title("Note-Taking")
    form_chinh.geometry("360x480")
    form_chinh.resizable(False, False)
    form_chinh.configure(bg="white")

    # Login và thêm mới Frame
    logout_new_frame = tk.Frame(form_chinh,
                               bg="white")
    logout_new_frame.pack(fill="x")

    # Cấu hình lưới cho frame
    logout_new_frame.columnconfigure(0, weight=1)
    logout_new_frame.columnconfigure(1, weight=1)
    logout_new_frame.columnconfigure(2, weight=1)

    # Nút thêm mới (New)
    new_button = tk.Button(logout_new_frame,
                           text="+",
                           font=("Times New Roman", 16),
                           command=lambda:Form_Note.show_note()
                           )
    new_button.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    # Nút đăng xuất (logout)
    
    tk.Label(logout_new_frame,
             text=f"Xin chào, {user.username}",
             font=("Times New Roman", 16),
             ).grid(row=0, column=2, padx=10, pady=10, sticky="e")
    
    logout_button = tk.Button(logout_new_frame,
                             text="Logout",
                             font=("Times New Roman", 16),
                             command=lambda:Form_Guest.show_user_form()
                             )
    logout_button.grid(row=1, column=2, padx=10, pady=10, sticky="e")


    # Header - tiêu đề app
    tk.Label(form_chinh,
             text="Note-Taking",
             font=("Times New Roman", 30, "bold"),
             bg="white"
             ).pack()

    # Find Frame
    find_frame = tk.Frame(form_chinh,
                          bg="white")
    find_frame.pack()

    # Thanh tìm kiếm
    find_entry = tk.Entry(find_frame,
                          font=("Times New Roman", 16),
                          bg="ghostwhite"
                          )
    find_entry.grid(row=2, column=0, padx=10, pady=10)

    find_button = tk.Button(find_frame,
                            text="Search",
                            font=("Times New Roman", 16)
                            )
    find_button.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

    # Chạy chương trình
    form_chinh.mainloop()