import tkinter as tk
from tkinter import messagebox
import Class_UserManage
import Form_User
user_manager = Class_UserManage.UserManage()
user_manager.docDuLieu()

def dangNhap(current_form=None):
    if (current_form):
        current_form.destroy()
    
    # Xây dựng Form
    login = tk.Tk()
    login.title("Login")
    login.geometry("360x280")
    login.resizable(width=False, height=False)

    # Header
    dangnhap_label = tk.Label(login, text="Đăng nhập", font=("Times New Roman",20,"bold"))
    dangnhap_label.grid(row=0, column=1, columnspan=2, pady=10)

    # Username
    taikhoan_label = tk.Label(login, text="Username:", font=("Times New Roman", 11), anchor="w")
    taikhoan_label.grid(row=1, column=0, padx=10, pady=5, sticky="we")

    taikhoan_entry = tk.Entry(login, font=("Times New Roman", 11))
    taikhoan_entry.grid(row=1, column=1, padx=10, pady=5, sticky="we")

    
    # Password
    password_label = tk.Label(login, text="Password:", font=("Times New Roman", 11), anchor="w")
    password_label.grid(row=2, column=0, padx=10, pady=5, sticky="we")

    password_entry = tk.Entry(login, font=("Times New Roman", 11))
    password_entry.grid(row=2, column=1, padx=10, pady=5, sticky="we")
    
    def HoTroDangNhap():
        taikhoan = taikhoan_entry.get()
        matkhau = password_entry.get()
        user = user_manager.login(taikhoan, matkhau)
        if user:
            messagebox.showinfo("Succesfull!", "Đăng nhập thành công")
            login.destroy()
            Form_User.show_user_form(user)
        else:
            messagebox.showerror("Error!", "Đăng nhập thất bại!")
            
    # Button đăng nhập
    dangnhap_button = tk.Button(login,
                                text="Login",
                                font=("Times New Roman", 11),
                                command=HoTroDangNhap
                                )
    dangnhap_button.grid(row=3,column=1, padx=10, pady=10)

    # Link tới form đăng ký
    tk.Label(login, text="Bạn chưa có tài khoản? Đăng ký tại đây!", font=("Times New Roman", 11,"bold")).grid(row=4,column=0, columnspan=2,padx=10, pady=10)
    dangky_button = tk.Button(login, text="Register", font=("Times New Roman", 11), command=lambda:open_register(login))
    dangky_button.grid(row=5,column=1, padx=10, pady=10)

    
    
def open_register(current_form):
    # Import cục bộ để tránh circular import
    import Form_Register
    Form_Register.dangKy(current_form)