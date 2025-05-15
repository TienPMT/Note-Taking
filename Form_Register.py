import tkinter as tk

def dangKy(current_form=None):
    if (current_form):
        current_form.destroy()
        
    # Xây dựng Form
    register = tk.Tk()
    register.title("Register")
    register.geometry("360x310")
    register.resizable(width=False, height=False)

    # Header
    dangnhap_label = tk.Label(register, text="Đăng ký", font=("Times New Roman",20,"bold"))
    dangnhap_label.grid(row=0, column=0, columnspan=2, pady=10)

    # Username
    taikhoan_label = tk.Label(register, text="Username:", font=("Times New Roman", 11), anchor="w")
    taikhoan_label.grid(row=1, column=0, padx=10, pady=5, sticky="we")

    taikhoan_entry = tk.Entry(register, font=("Times New Roman", 11))
    taikhoan_entry.grid(row=1, column=1, padx=10, pady=5, sticky="we")

    # Password
    password_label = tk.Label(register, text="Password:", font=("Times New Roman", 11), anchor="w")
    password_label.grid(row=2, column=0, padx=10, pady=5, sticky="we")
    password_entry = tk.Entry(register, font=("Times New Roman", 11))
    password_entry.grid(row=2, column=1, padx=10, pady=5, sticky="we")
    # Xác nhận Password
    password_check_label = tk.Label(register, text="Nhập lại Password:", font=("Times New Roman", 11), anchor="w")
    password_check_label.grid(row=3, column=0, padx=10, pady=5, sticky="we")
    password_check_entry = tk.Entry(register, font=("Times New Roman", 11))
    password_check_entry.grid(row=3, column=1, padx=10, pady=5, sticky="we")

    # Button đăng ký
    dangky_button = tk.Button(register, text="Register", font=("Times New Roman", 11))
    dangky_button.grid(row=4,column=1, padx=10, pady=10)
    
    # Link tới form đăng nhập
    tk.Label(register, text="Bạn đã có tài khoản? Đăng nhập tại đây!", font=("Times New Roman", 11,"bold")).grid(row=5,column=0, columnspan=2,padx=10, pady=10)
    dangnhap_button = tk.Button(register, text="Login", font=("Times New Roman", 11), command=lambda:open_login(register))
    dangnhap_button.grid(row=6,column=1, padx=10, pady=10)
    
    # Chạy giao diện
    register.mainloop()


def open_login(current_form):
    # Import cục bộ để tránh circular import
    import Form_Login
    Form_Login.dangNhap(current_form)