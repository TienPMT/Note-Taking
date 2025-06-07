import tkinter as tk
from Class_Guest import Guest
from Form_Note import Form_Note
from Form_Login import Form_Login

class Form_Main:
    def __init__(self):
        # ==== Color Palette ====
        BG_COLOR = "#e3f2fd"          # Light blue
        HEADER_COLOR = "#1976d2"      # Blue
        BTN_LOGIN = "#1976d2"         # Main blue button
        BTN_LOGIN_HOVER = "#115293"
        BTN_GUEST = "#43a047"         # Green
        BTN_GUEST_HOVER = "#388e3c"
        BTN_EXIT = "#e53935"          # Red
        BTN_EXIT_HOVER = "#b71c1c"
        TEXT_COLOR = "white"

        # ==== Init Window ====
        self.root = tk.Tk()
        self.root.title("Ghi chú App")
        self.root.geometry("400x340")
        self.root.resizable(False, False)
        self.root.configure(bg=BG_COLOR)

        # ==== Header ====
        header = tk.Label(
            self.root,
            text="📝 Chào mừng đến với Note App",
            font=("Segoe UI", 16, "bold"),
            fg=HEADER_COLOR,
            bg=BG_COLOR,
            pady=18
        )
        header.pack()

        # ==== Button Style Helper ====
        def style_button(btn, color, hover_color):
            btn.configure(bg=color, fg=TEXT_COLOR, activebackground=hover_color, activeforeground=TEXT_COLOR, relief=tk.FLAT, font=("Segoe UI", 11, "bold"), cursor="hand2")
            btn.bind("<Enter>", lambda e: btn.config(bg=hover_color))
            btn.bind("<Leave>", lambda e: btn.config(bg=color))

        # ==== Login/Register Button ====
        btn_login = tk.Button(
            self.root,
            text="🔑 Đăng nhập / Đăng ký",
            width=25,
            command=self.open_login
        )
        btn_login.pack(pady=15, ipady=5)
        style_button(btn_login, BTN_LOGIN, BTN_LOGIN_HOVER)

        # ==== Guest Button ====
        btn_guest = tk.Button(
            self.root,
            text="🎮 Dùng thử với Guest",
            width=25,
            command=self.start_as_guest
        )
        btn_guest.pack(pady=5, ipady=5)
        style_button(btn_guest, BTN_GUEST, BTN_GUEST_HOVER)

        # ==== Exit Button ====
        btn_exit = tk.Button(
            self.root,
            text="⏹️ Thoát",
            width=13,
            command=self.root.destroy
        )
        btn_exit.pack(pady=20, ipady=3)
        style_button(btn_exit, BTN_EXIT, BTN_EXIT_HOVER)

        self.root.mainloop()

    def start_as_guest(self):
        guest = Guest()
        self.root.destroy()
        Form_Note(guest)
        
    def open_login(self):
        self.login_form = Form_Login(self.root, self.on_login_success)
    
    def on_login_success(self, user):
        self.root.destroy()
        if user.role == 'admin':
            from Form_Admin import Form_Admin
            Form_Admin(user)
        else:
            from Form_Note import Form_Note
            Form_Note(user)
