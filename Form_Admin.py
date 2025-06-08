import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from Class_UserManage import UserManage
from Class_Admin import Admin

class Form_Admin:
    def __init__(self, admin_user):
        self.admin_user = admin_user
        self.admin = Admin(admin_user.username, admin_user.password)
        self.user_manager = UserManage()
        self.users_data = self.user_manager.load_users()

        self.window = tk.Tk()
        self.window.title("Quản lý Note-Taking")
        self.window.geometry("900x550")
        self.window.resizable(False, False)
        self.window.configure(bg="#e3e8f0")

        style = ttk.Style(self.window)
        style.theme_use("clam")
        # Treeview user (list)
        style.configure("Treeview",
                        font=("Segoe UI", 12),
                        rowheight=30,
                        borderwidth=1,
                        relief="flat",
                        background="#f8fafc",
                        fieldbackground="#f8fafc",
                        foreground="#222b45")
        style.configure("Treeview.Heading",
                        font=("Segoe UI", 13, "bold"),
                        background="#2563eb",
                        foreground="#fff")
        # Hiệu ứng khi chọn
        style.map("Treeview",
                  background=[('selected', '#2563eb')],
                  foreground=[('selected', '#fff')])

        # Nút
        style.configure("TButton",
                        font=("Segoe UI", 11, "bold"),
                        padding=6,
                        background="#2563eb",
                        foreground="#fff",
                        borderwidth=0)
        style.map("TButton",
                  background=[('active', '#1e40af'), ('!active', '#2563eb')])

        # Label
        style.configure("TLabel",
                        font=("Segoe UI", 12),
                        background="#e3e8f0")

        # ========================== HEADING ==========================
        heading_frame = tk.Frame(self.window, bg="#e3e8f0")
        heading_frame.pack(padx=10, pady=10, fill="x")
        heading_frame.grid_columnconfigure(0, weight=1)
        heading_frame.grid_columnconfigure(1, weight=0)
        heading_frame.grid_columnconfigure(2, weight=1)

        tk.Label(heading_frame,
                 text="Quản lý Note-Taking",
                 font=("Segoe UI", 22, "bold"),
                 bg="#e3e8f0",
                 fg="#2563eb"
                 ).grid(row=0, column=1, pady=10)

        tk.Button(heading_frame,
                  text="Đăng xuất",
                  font=("Segoe UI", 11, "bold"),
                  command=lambda: self.admin.dang_xuat(self.user_manager, self.window),
                  bg="#e11d48",
                  fg="white",
                  relief=tk.FLAT,
                  borderwidth=0,
                  padx=16,
                  pady=6,
                  activebackground="#be123c"
                  ).grid(row=0, column=2, padx=10, pady=10)

        # ========================== BODY ==========================
        body_frame = tk.Frame(self.window, bg="#e3e8f0")
        body_frame.pack(padx=10, pady=0, fill="both", expand=True)

        # ======== TREEVIEW USERS LIST ========
        ds_user_frame = tk.Frame(body_frame, bg="#e3e8f0", highlightbackground="#2563eb", highlightthickness=1)
        ds_user_frame.grid(row=0, column=0, padx=(0, 20), pady=10, sticky="ns")
        tk.Label(ds_user_frame, text="Danh sách User", font=("Segoe UI", 14, "bold"), bg="#e3e8f0", fg="#2563eb").pack(pady=(0, 5))
        self.tree = ttk.Treeview(ds_user_frame, columns=("username"), show="headings", selectmode="browse", height=10)
        self.tree.heading("username", text="Username")
        self.tree.column("username", width=200, anchor="center")
        self.tree.pack(fill="y", expand=True)
        for username, info in self.users_data.items():
            if info.get("role", "user") == "user":
                self.tree.insert("", "end", values=(username,))
        self.tree.bind("<<TreeviewSelect>>", self.chon_dong)

        # ============ Thống kê ============
        thongke_frame = tk.Frame(body_frame, bg="#e3e8f0")
        thongke_frame.grid(row=0, column=1, padx=10, sticky="nsew")
        tk.Label(thongke_frame,
                 text="Thống kê",
                 font=("Segoe UI", 15, "bold"),
                 fg="#2563eb",
                 bg="#e3e8f0"
                 ).grid(row=0, column=0, columnspan=2, padx=10, sticky="w")
        tk.Label(thongke_frame,
                 text="Username:",
                 font=("Segoe UI", 13),
                 bg="#e3e8f0"
                 ).grid(row=1, column=0, padx=10, sticky="w")
        self.username_var = tk.StringVar()
        ttk.Entry(thongke_frame,
                textvariable=self.username_var,
                font=("Segoe UI", 13),
                state="readonly",
                width=18
                ).grid(row=1, column=1, padx=10, sticky="w", columnspan=2)
        tk.Label(thongke_frame,
                 text="Số lượng Note:",
                 font=("Segoe UI", 13),
                 bg="#e3e8f0"
                 ).grid(row=2, column=0, padx=10, sticky="w")
        self.soluong_var = tk.StringVar()
        ttk.Entry(thongke_frame,
                textvariable=self.soluong_var,
                font=("Segoe UI", 13),
                state="readonly",
                width=18
                ).grid(row=2, column=1, padx=10, sticky="w", columnspan=2)
        tk.Label(thongke_frame,
                 text="Lịch sử tạo note",
                 font=("Segoe UI", 13),
                 bg="#e3e8f0"
                 ).grid(row=3, column=0, padx=10, sticky="w")

        notes_frame = tk.Frame(thongke_frame, bg="#dbeafe", highlightbackground="#2563eb", highlightthickness=1)
        notes_frame.grid(row=4, rowspan=2, column=0, columnspan=2, padx=10, pady=10)
        self.notes_tree = ttk.Treeview(
            notes_frame,
            columns=("title", "created_at", "updated_at"),
            show="headings",
            height=6
        )
        self.notes_tree.heading("title", text="Tiêu đề")
        self.notes_tree.heading("created_at", text="Ngày tạo")
        self.notes_tree.heading("updated_at", text="Ngày sửa")
        self.notes_tree.column("title", width=220)
        self.notes_tree.column("created_at", width=120)
        self.notes_tree.column("updated_at", width=120)
        self.notes_tree.pack(expand=True, fill="both")

        # ========================== LIST BUTTON ==========================
        button_frame = tk.Frame(body_frame, bg="#e3e8f0")
        button_frame.grid(row=1, column=1, padx=10, pady=20, sticky="ew")
        ttk.Button(button_frame, text="Xoá User", width=14, command=self.xoa_user).grid(row=0, column=0, padx=12)
        ttk.Button(button_frame, text="Đổi mật khẩu", width=14, command=self.doi_password).grid(row=0, column=1, padx=12)
        ttk.Button(button_frame, text="Cấp quyền", width=14, command=self.cap_quyen).grid(row=0, column=2, padx=12)

        self.window.mainloop()


    def chon_dong(self, event):
        chon = self.tree.selection()
        if chon:
            username = self.tree.item(chon[0])['values'][0] # lấy Username
            self.username_var.set(username)
            notes = self.users_data.get(username, {}).get('notes', [])
            self.soluong_var.set(str(len(notes)))
            
            # Xóa bảng note cũ
            for i in self.notes_tree.get_children():
                self.notes_tree.delete(i)
            # Thêm note mới
            for note in notes:
                title = note.get('title', '')
                created_goc = note.get('created', note.get('created_at', ''))
                updated_goc = note.get('updated', note.get('updated_at', ''))
                created = self.date(created_goc)
                updated = self.date(updated_goc)
                self.notes_tree.insert("", tk.END, values=(title, created, updated))
    
    def cap_nhat_tree_users(self):
        # Reload dữ liệu mới nhất
        self.users_data = self.user_manager.load_users()
        # Xóa tree cũ
        for i in self.tree.get_children():
            self.tree.delete(i)
        # Thêm lại các user mới
        for username, info in self.users_data.items():
            if info.get("role", "user") == "user":
                self.tree.insert("", "end", values=(username,))
            
    def date(self, dt_str):
        try:
            return datetime.fromisoformat(dt_str).strftime('%Y-%m-%d')
        except Exception:
            return dt_str[:10] if dt_str else ''
    
    def xoa_user(self):
        chon = self.tree.selection()
        if not chon:
            messagebox.showwarning("Thông báo", "Hãy chọn user cần xoá!")
            return
        username = self.tree.item(chon[0])['values'][0] # lấy Username
        
        if not messagebox.askyesno("Xác nhận", f"Bạn chắc chắn muốn xoá user '{username}'?"):
            return
        if self.admin.delete_user(username):
            messagebox.showinfo("Thành công", f"Đã xoá user '{username}'")
            self.cap_nhat_tree_users()
            # Xoá thông tin thống kê bên phải nếu user vừa bị xoá đang được xem
            self.username_var.set("")
            self.soluong_var.set("")
            for i in self.notes_tree.get_children():
                self.notes_tree.delete(i)
        else:
            messagebox.showwarning("Lỗi", f"Không thể xoá user '{username}'")
    
    def doi_password(self):
        chon = self.tree.selection()
        if not chon:
            messagebox.showwarning("Thông báo", "Hãy chọn User cần đổi mật khẩu", parent=self.window)
            return
        username = self.tree.item(chon[0])['values'][0]
    
        # ======= Giao diện hiện đại với ttk =======
        change_password_window = tk.Toplevel(self.window)
        change_password_window.geometry("370x320")
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
        tk.Label(frm, text="Mật khẩu mới:", bg="#f1f5f9", anchor="w", font=("Segoe UI", 12)).grid(row=1, column=0, sticky="w", pady=5)
        new_password_entry = ttk.Entry(frm, show="*")
        new_password_entry.grid(row=1, column=1, pady=5, padx=10)
    
        tk.Label(frm, text="Xác nhận mật khẩu:", bg="#f1f5f9", anchor="w", font=("Segoe UI", 12)).grid(row=2, column=0, sticky="w", pady=5)
        new_password_confirm_entry = ttk.Entry(frm, show="*")
        new_password_confirm_entry.grid(row=2, column=1, pady=5, padx=10)
    
        def xac_nhan():
            new_password = new_password_entry.get().strip()
            new_password_confirm = new_password_confirm_entry.get().strip()
    
            if not new_password or not new_password_confirm:
                messagebox.showerror("Lỗi", "Mật khẩu mới không được để trống!", parent=change_password_window)
                return
            
            if new_password != new_password_confirm:
                messagebox.showerror("Lỗi", "Mật khẩu xác nhận không khớp!", parent=change_password_window)
                return
    
            if self.admin.change_password(username, new_password):
                messagebox.showinfo("Thành công!", f"Đổi mật khẩu user '{username}' thành công!", parent=change_password_window)
                change_password_window.destroy()
            else:
                messagebox.showerror("Lỗi!", f"Đổi mật khẩu user '{username}' không thành công!", parent=change_password_window)
    
        # Nút xác nhận
        style = ttk.Style()
        style.configure("Accent.TButton", font=("Segoe UI", 12, "bold"), background="#2563eb", foreground="white", padding=6)
        style.map("Accent.TButton",
                  background=[('active', '#1e40af'), ('!active', '#2563eb')],
                  foreground=[('pressed', '#fff'), ('active', '#fff')])
        ttk.Button(
            change_password_window,
            text="Xác nhận",
            style="Accent.TButton",
            command=xac_nhan
        ).pack(pady=16)
        
    def cap_quyen(self):
        chon = self.tree.selection()
        if not chon:
            messagebox.showwarning("Thông báo", "Hãy chọn User cần cấp quyền")
            return
        
        username = self.tree.item(chon[0])['values'][0]        

        if not messagebox.askyesno("Xác nhận", f"Bạn chắc chắn muốn cấp quyền ADMIN cho user '{username}'?"):
            return
        if self.admin.change_role(username):
            messagebox.showinfo("Thành công!", f"Cấp quyền ADMIN cho user '{username}' thành công!")
            self.cap_nhat_tree_users()
            return
        else:
            messagebox.showerror("Lỗi", f"Cấp quyền ADMIN cho user '{username}' KHÔNG thành công!")