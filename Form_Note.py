import tkinter as tk
from tkinter import messagebox, ttk
from Class_Note import Note  
from Form_NoteList import show_note_list
from Form_SearchNote import search_note
from Class_UserManage import UserManage
from Class_Guest import Guest

class Form_Note:
    def __init__(self, user):
        self.user = user
        self.username = user.username
        self.user_manager = UserManage()
        self.notes = []
        
        try:
            user_data = self.user_manager.get_user_data(self.username)
            if user_data and 'notes' in user_data:
                # Thêm bộ lọc cho note hợp lệ
                self.notes = [Note.from_dict(n) for n in user_data['notes'] if isinstance(n, dict)]
                self.user.notes = self.notes
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể tải dữ liệu note: {str(e)}")
            self.notes = []
    
        self.is_guest = isinstance(user, Guest)

        self.window = tk.Tk()
        self.window.title(f"Tạo ghi chú - {self.username}")
        self.window.geometry("800x720")
        self.window.configure(bg="#f0f6fb")
        self.window.resizable(False, False)

        # ===== HEADER =====
        header_frame = tk.Frame(self.window, bg="#f0f6fb")
        header_frame.pack(fill="x", pady=(20, 0))

        icon_label = tk.Label(header_frame, text="✍️", font=("Segoe UI", 28), bg="#f0f6fb")
        icon_label.pack(side="left", padx=(40, 10))
        title_label = tk.Label(header_frame, text="Tạo Ghi Chú", font=("Segoe UI", 24, "bold"), bg="#f0f6fb", fg="#1976d2")
        title_label.pack(side="left", pady=0)
        user_label = tk.Label(header_frame, text=f"👤 {self.username}", font=("Segoe UI", 12), bg="#f0f6fb", fg="#445")
        user_label.pack(side="right", padx=(0, 40), pady=8)

        # ===== INPUT FRAME =====
        input_frame = tk.Frame(self.window, bg="#f0f6fb")
        input_frame.pack(pady=18, padx=30, fill="x")

        # Tiêu đề
        lbl_title = tk.Label(input_frame, text="Tiêu đề", font=("Segoe UI", 13, "bold"), bg="#f0f6fb")
        lbl_title.grid(row=0, column=0, sticky="w", padx=(0, 10), pady=5)
        self.entry_title = tk.Entry(input_frame, width=56, font=("Segoe UI", 12), bg="#fff", relief=tk.GROOVE, borderwidth=2)
        self.entry_title.grid(row=0, column=1, sticky="ew", padx=(0, 10), pady=5)
        self.entry_title.config(highlightthickness=1, highlightbackground="#1976d2")

        # Gợi ý nhập
        hint_title = tk.Label(input_frame, text="VD: Công việc hôm nay, Lịch học tuần 6...", font=("Segoe UI", 10, "italic"), bg="#f0f6fb", fg="#869ab8")
        hint_title.grid(row=1, column=1, sticky="w", padx=(0, 10))

        # Nội dung
        lbl_content = tk.Label(input_frame, text="Nội dung", font=("Segoe UI", 13, "bold"), bg="#f0f6fb")
        lbl_content.grid(row=2, column=0, sticky="nw", padx=(0, 10), pady=(12, 5))
        self.text_content = tk.Text(input_frame, height=8, width=68, font=("Segoe UI", 12), bg="#fff", relief=tk.GROOVE, borderwidth=2, wrap="word")
        self.text_content.grid(row=2, column=1, padx=(0, 10), pady=(12, 5))
        self.text_content.config(highlightthickness=1, highlightbackground="#1976d2")
        # Gợi ý nhập nội dung
        hint_content = tk.Label(input_frame, text="Nhập nội dung ghi chú của bạn...", font=("Segoe UI", 10, "italic"), bg="#f0f6fb", fg="#869ab8")
        hint_content.grid(row=3, column=1, sticky="w", padx=(0, 10), pady=(0, 5))

        input_frame.grid_columnconfigure(1, weight=1)

        # ===== BUTTONS =====
        button_frame = tk.Frame(self.window, bg="#f0f6fb")
        button_frame.pack(pady=20)

        # Lưu ghi chú
        btn_save = tk.Button(button_frame, text="💾 Lưu ghi chú", width=28, bg="#28a745", fg="white",
                             font=("Segoe UI", 11, "bold"), command=self.save_note, cursor="hand2", relief=tk.RAISED, borderwidth=0)
        btn_save.grid(row=0, column=0, padx=12, pady=6, ipadx=4, ipady=2, sticky="ew")
        btn_save.bind("<Enter>", lambda e: btn_save.config(bg="#218838"))
        btn_save.bind("<Leave>", lambda e: btn_save.config(bg="#28a745"))

        # Xem danh sách
        btn_list = tk.Button(button_frame, text="📋 Xem danh sách ghi chú", width=28, bg="#007bff", fg="white",
                             font=("Segoe UI", 11), command=self.go_to_list, cursor="hand2", relief=tk.RAISED, borderwidth=0)
        btn_list.grid(row=0, column=1, padx=12, pady=6, ipadx=4, ipady=2, sticky="ew")
        btn_list.bind("<Enter>", lambda e: btn_list.config(bg="#0056b3"))
        btn_list.bind("<Leave>", lambda e: btn_list.config(bg="#007bff"))

        # Tìm kiếm
        btn_search = tk.Button(button_frame, text="🔍 Tìm kiếm ghi chú", width=28, bg="#fd7e14", fg="white",
                               font=("Segoe UI", 11), command=self.go_to_search, cursor="hand2", relief=tk.RAISED, borderwidth=0)
        btn_search.grid(row=1, column=0, padx=12, pady=6, ipadx=4, ipady=2, sticky="ew")
        btn_search.bind("<Enter>", lambda e: btn_search.config(bg="#c46309"))
        btn_search.bind("<Leave>", lambda e: btn_search.config(bg="#fd7e14"))

        # Đăng xuất
        btn_logout = tk.Button(button_frame, text="⛔ Đăng xuất", width=28, bg="#e53935", fg="white",
                               font=("Segoe UI", 11), command=self.logout, cursor="hand2", relief=tk.RAISED, borderwidth=0)
        btn_logout.grid(row=1, column=1, padx=12, pady=6, ipadx=4, ipady=2, sticky="ew")
        btn_logout.bind("<Enter>", lambda e: btn_logout.config(bg="#b71c1c"))
        btn_logout.bind("<Leave>", lambda e: btn_logout.config(bg="#e53935"))

        # Đăng nhập/Đăng ký (chỉ guest)
        if self.is_guest:
            # Thêm label cảnh báo to, nổi bật
            lbl_guest_warning = tk.Label(
                self.window,
                text="⚠️ Bạn đang sử dụng quyền GUEST.\nDữ liệu sẽ không được lưu khi thoát chương trình!",
                font=("Segoe UI", 13, "bold"),
                bg="#f0f6fb",
                fg="#e53935",  # Đỏ cảnh báo
                justify="center")
            
            lbl_guest_warning.pack(pady=(8, 0))
            btn_login = tk.Button(self.window, text="🔑 Đăng nhập / Đăng ký", width=28, bg="#17a2b8", fg="white",
                                  font=("Segoe UI", 11), command=self.open_login_register, cursor="hand2", relief=tk.RAISED, borderwidth=0)
            btn_login.pack(pady=10)
            btn_login.bind("<Enter>", lambda e: btn_login.config(bg="#117a8b"))
            btn_login.bind("<Leave>", lambda e: btn_login.config(bg="#17a2b8"))
        
        # Đổi Password (chỉ user)
        if not self.is_guest:
            btn_login = tk.Button(self.window, text="🔑 Đổi mật khẩu", width=28, bg="#17a2b8", fg="white",
                                  font=("Segoe UI", 11), command=self.doi_password, cursor="hand2", relief=tk.RAISED, borderwidth=0)
            btn_login.pack(pady=10)
            btn_login.bind("<Enter>", lambda e: btn_login.config(bg="#117a8b"))
            btn_login.bind("<Leave>", lambda e: btn_login.config(bg="#17a2b8"))

        # Nút đóng
        btn_close = tk.Button(self.window, text="❌ Đóng", width=28, bg="#dc3545", fg="white",
                              font=("Segoe UI", 11), command=self.window.destroy, cursor="hand2", relief=tk.RAISED, borderwidth=0)
        btn_close.pack(pady=10)
        btn_close.bind("<Enter>", lambda e: btn_close.config(bg="#a71d2a"))
        btn_close.bind("<Leave>", lambda e: btn_close.config(bg="#dc3545"))

        # Đường kẻ trang trí
        tk.Frame(self.window, height=2, bg="#e0e6ed").pack(fill="x", padx=30, pady=(15, 10))

        # Hiện cửa sổ
        self.window.mainloop()

    def save_note(self):
        title = self.entry_title.get().strip()
        content = self.text_content.get("1.0", "end-1c").strip()

        if not title or not content:
            messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập đầy đủ tiêu đề và nội dung.")
            return

        note = Note(title, content)

        if self.is_guest:
            if not self.user.add_note(note):
                messagebox.showwarning("Giới hạn", "Tài khoản Guest chỉ được lưu 1 ghi chú. Vui lòng đăng ký để sử dụng thêm.")
                return
            self.notes = self.user.notes
        else:
            self.notes.append(note)
            self.user.notes = self.notes
            notes_dict_list = [n.to_dict() for n in self.notes]
            self.user_manager.update_user_notes(self.username, notes_dict_list)

        messagebox.showinfo("Thành công", "Ghi chú đã được lưu.") 
        self.entry_title.delete(0, tk.END)
        self.text_content.delete("1.0", tk.END)

    def go_to_list(self):
        self.window.withdraw()
        show_note_list(self.user, self.window)
    
    def go_to_search(self):
        self.window.withdraw()
        search_note(self.user, self.window)

    def open_login_register(self):
        from Form_Login import Form_Login
        Form_Login(self.window, self.handle_login_success)
        self.window.withdraw()
    
    def handle_login_success(self, user):
        if user.role == 'admin':
            from Form_Admin import Form_Admin
            Form_Admin(user)
        else:
            from Form_Note import Form_Note
            Form_Note(user)
    
    def logout(self):
        self.user_manager.logout()
        self.window.destroy()
        from Form_Main import Form_Main
        Form_Main()
    
    def doi_password(self):
        username = self.username
        # Lấy mật khẩu thật của user
        users_data = self.user_manager.load_users()
        user_password = users_data[username]['password']
        
        if user_password == "":
            messagebox.showerror("Lỗi!", "Lỗi truy xuất mật khẩu cũ!")
            return
        
        # ======= Giao diện hiện đại với ttk =======
        change_password_window = tk.Toplevel(self.window)
        change_password_window.geometry("370x360")
        change_password_window.title("Đổi mật khẩu User")
        change_password_window.resizable(False, False)
        change_password_window.configure(bg="#f1f5f9")
        change_password_window.grab_set()
    
        # Tiêu đề & icon
        tk.Label(change_password_window, text="🔒", font=("Segoe UI Emoji", 28), bg="#f1f5f9").pack(pady=(18,0))
        tk.Label(change_password_window, text="Đổi mật khẩu User", font=("Segoe UI", 16, "bold"), fg="#2563eb", bg="#f1f5f9").pack(pady=(4,14))
    
        frm = tk.Frame(change_password_window, bg="#f1f5f9")
        frm.pack(expand=True, fill="both", padx=30, pady=6)
    
        # Trường nhập
        tk.Label(frm, text="Mật khẩu cũ:", bg="#f1f5f9", anchor="w", font=("Segoe UI", 12)).grid(row=0, column=0, sticky="w", pady=5)
        old_password_entry = ttk.Entry(frm, show="*")
        old_password_entry.grid(row=0, column=1, pady=5, padx=10)
    
        tk.Label(frm, text="Mật khẩu mới:", bg="#f1f5f9", anchor="w", font=("Segoe UI", 12)).grid(row=1, column=0, sticky="w", pady=5)
        new_password_entry = ttk.Entry(frm, show="*")
        new_password_entry.grid(row=1, column=1, pady=5, padx=10)
    
        tk.Label(frm, text="Xác nhận mật khẩu:", bg="#f1f5f9", anchor="w", font=("Segoe UI", 12)).grid(row=2, column=0, sticky="w", pady=5)
        new_password_confirm_entry = ttk.Entry(frm, show="*")
        new_password_confirm_entry.grid(row=2, column=1, pady=5, padx=10)
    
        def xac_nhan():
            old_password = old_password_entry.get().strip()
            new_password = new_password_entry.get().strip()
            new_password_confirm = new_password_confirm_entry.get().strip()
    
            if not old_password:
                messagebox.showerror("Lỗi", "Mật khẩu cũ không được để trống!", parent=change_password_window)
                return
            if not new_password:
                messagebox.showerror("Lỗi", "Mật khẩu mới không được để trống!", parent=change_password_window)
                return
            if old_password != user_password:
                messagebox.showerror("Lỗi", "Mật khẩu cũ không đúng!", parent=change_password_window)
                return
            if old_password == new_password:
                messagebox.showerror("Lỗi", "Mật khẩu mới không được trùng với mật khẩu cũ!", parent=change_password_window)
                return
            if new_password != new_password_confirm:
                messagebox.showerror("Lỗi", "Mật khẩu xác nhận không khớp!", parent=change_password_window)
                return
    
            if self.user_manager.change_password(username, new_password):
                messagebox.showinfo("Thành công!", f"Đổi mật khẩu user '{username}' thành công!", parent=change_password_window)
                change_password_window.destroy()
            else:
                messagebox.showerror("Lỗi!", f"Đổi mật khẩu user '{username}' không thành công!", parent=change_password_window)
    
        # Nút xác nhận
        style = ttk.Style(change_password_window)
        style.theme_use("clam")
        style.configure(
            "Accent.TButton",
            font=("Segoe UI", 12, "bold"),
            background="#2563eb",   # Xanh dương chủ đạo
            foreground="white",
            padding=10,
            borderwidth=0
        )

        btn_xac_nhan = ttk.Button(
            change_password_window,
            text="✅ Xác nhận",
            style="Accent.TButton",
            command=xac_nhan,
            cursor="hand2"
        )
        btn_xac_nhan.pack(pady=24, ipadx=12, ipady=4)
        