import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime, timedelta
from Class_UserManage import UserManage


class Form_Admin:
    def __init__(self, admin_user):
        self.admin = admin_user
        self.user_manager = UserManage()
                
        self.users_data = self.doc_du_lieu("Users_Data.json")

        # //* Xây giao diện *\\
        self.admin_window = tk.Tk()
        self.admin_window.title("Admin")
        self.admin_window.geometry("840x520")
        self.admin_window.resizable(True, True)
        self.admin_window.configure(bg="#f0f4f8")
        
        self.style = ttk.Style(self.admin_window)
        self.style.theme_use("clam")
        self.style.configure("Treeview", font=("Segoe UI", 12), rowheight=28)
        self.style.configure("Treeview.Heading", font=("Segoe UI", 13, "bold"))
        self.style.configure("TFrame", background="#f0f4f8")
        self.style.configure("TLabel", background="#f0f4f8", font=("Segoe UI", 12))
        self.style.configure("TButton", font=("Segoe UI", 11, "bold"))
        
        # ========================== Xây Heading ==========================
        self.heading_frame = tk.Frame(self.admin_window)
        self.heading_frame.pack(padx=10, pady=10, fill="x")
        
        self.heading_frame.grid_columnconfigure(0, weight=1)
        self.heading_frame.grid_columnconfigure(1, weight=0)
        self.heading_frame.grid_columnconfigure(2, weight=1)
        
        tk.Label(self.heading_frame,
                 text="Quản lý Note-Taking",
                 font=("Segoe UI", 21, "bold"),
                 foreground="#1976d2"
                 ).grid(row=0, column=1, pady=10)
        
        tk.Button(self.heading_frame,
                  text="Logout",
                  font=("Segoe UI", 11, "bold"),
                  command=lambda:self.dang_xuat(),
                  bg="#e53935",
                  fg="white",
                  relief=tk.FLAT,
                  borderwidth=0,
                  padx=12,
                  pady=4
                  ).grid(row=0, column=2, padx=10, pady=10)
        
        # ========================== Xây Body ==========================
        self.body_frame = tk.Frame(self.admin_window)
        self.body_frame.pack(padx=10, pady=10, fill="both", expand=True)
        
        # ======== Xây Treeview ========
        self.ds_user_frame = tk.Frame(self.body_frame)
        self.ds_user_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ewsn")
        self.tree = ttk.Treeview(self.ds_user_frame, columns=("username"), show="headings")
        self.tree.heading("username", text="Danh sách User")
        self.tree.pack()
        for username, info in self.users_data.items():
            if info.get("role", "user") == "user":
                self.tree.insert("", "end", values=(username,))
        self.tree.bind("<<TreeviewSelect>>", self.chon_dong)

        # ============ Xây dụng thống kê =============
        self.thongke_frame = tk.Frame(self.body_frame)
        self.thongke_frame.grid(row=0, column=1, padx=10, sticky="ewsn")
        tk.Label(self.thongke_frame,
                 text="Thống kê",
                 font=("Segoe UI", 15, "bold"),
                 ).grid(row=0, column=0, columnspan=2, padx=10, sticky="w")
        tk.Label(self.thongke_frame,
                 text="Username: ",
                 font=("Segoe UI", 13)
                 ).grid(row=1, column=0, padx=10, sticky="w")
        self.username_var = tk.StringVar()
        tk.Entry(self.thongke_frame,
                textvariable=self.username_var,
                font=("Segoe UI", 13),
                state="readonly",
                width=15
                ).grid(row=1, column=1, padx=10, sticky="w", columnspan=2)
        tk.Label(self.thongke_frame,
                 text="Số lượng Note: ",
                 font=("Segoe UI", 13)
                 ).grid(row=2, column=0, padx=10, sticky="w")
        self.soluong_var = tk.StringVar()
        tk.Entry(self.thongke_frame,
                textvariable=self.soluong_var,
                font=("Segoe UI", 13),
                state="readonly",
                width=15
                ).grid(row=2, column=1, padx=10, sticky="w", columnspan=2)
        tk.Label(self.thongke_frame,
                 text="Lịch sử tạo note",
                 font=("Segoe UI", 13)
                 ).grid(row=3, column=0, padx=10, sticky="w")
        
        # Treeview hiển thị note của user
        self.notes_frame = tk.Frame(self.thongke_frame)
        self.notes_frame.grid(row=4, rowspan=2, column=0, columnspan=2, padx=10, pady=10)
        
        self.notes_tree = ttk.Treeview(
            self.notes_frame, 
            columns=("title", "created_at", "updated_at"), 
            show="headings",
            height=6
        )
        self.notes_tree.heading("title", text="Tiêu đề")
        self.notes_tree.heading("created_at", text="Ngày tạo")
        self.notes_tree.heading("updated_at", text="Ngày sửa")
        self.notes_tree.column("title", width=100)
        self.notes_tree.column("created_at", width=200)
        self.notes_tree.column("updated_at", width=200)
        self.notes_tree.pack(expand=True)
        
        
        self.admin_window.mainloop()
    
    def chon_dong(self, event):
        chon = self.tree.selection()
        if chon:
            username = self.tree.item(chon[0])['values'][0]
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
    
    def doc_du_lieu(self, tenfile):
        if os.path.exists(tenfile):
            with open(tenfile, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    def cap_nhat_du_lieu(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for username in self.users_data:
            self.tree.insert("", tk.END, values=(username,))
    
    def dang_xuat(self):
        self.user_manager.logout()
        self.admin_window.destroy()
        from Form_Main import show_main_form
        show_main_form()
        
    def date(self, dt_str):
        try:
            # Nếu chuỗi đúng định dạng ISO, cắt lấy ngày
            return datetime.fromisoformat(dt_str).strftime('%Y-%m-%d')
        except Exception:
            # Nếu lỗi (ví dụ chuỗi trống hoặc không hợp lệ), lấy 10 ký tự đầu
            return dt_str[:10] if dt_str else ''     