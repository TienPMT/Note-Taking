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
        
        def doc_du_lieu(tenfile):
            if os.path.exists(tenfile):
                with open(tenfile, "r", encoding="utf-8") as f:
                    return json.load(f)
            return []

        def cap_nhat_du_lieu():
            for i in self.tree.get_children():
                self.tree.delete(i)
            for username in self.users_data:
                self.tree.insert("", tk.END, values=(username,))
        
        def chon_dong(event):
            chon = self.tree.selection()
            if chon:
                username = self.tree.item(chon[0])['values'][0]
                self.username_var.set(username)
                notes = self.users_data.get(username, {}).get('notes', [])
                self.soluong_var.set(str(len(notes)))

                
        self.users_data = doc_du_lieu("Users_Data.json")

        # //* Xây giao diện *\\
        self.admin_window = tk.Tk()
        self.admin_window.title("Admin")
        self.admin_window.geometry("800x480")
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
        tk.Label(self.heading_frame,
                 text="Quản lý Note-Taking",
                 font=("Segoe UI", 21, "bold"),
                 foreground="#1976d2"
                 ).pack(padx=10, pady=10)
        self.heading_frame.pack(padx=10, pady=10, fill="x")
        
        # ========================== Xây Body ==========================
        self.body_frame = tk.Frame(self.admin_window)
        self.body_frame.pack(padx=10, pady=10, fill="both", expand=True)
        
        # ======== Xây Treeview ========
        self.ds_user_frame = tk.Frame(self.body_frame)
        self.ds_user_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ewsn")
        self.tree = ttk.Treeview(self.ds_user_frame, columns=("username"), show="headings")
        self.tree.heading("username", text="Danh sách User")
        self.tree.pack()
        for username in self.users_data:
            self.tree.insert("", "end", values=(username,))
        self.tree.bind("<<TreeviewSelect>>", chon_dong)

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
        
        self.ngay_var = tk.IntVar(value=3)
        tk.Radiobutton(self.thongke_frame,
                      text="3 days",
                      font=("Segoe UI", 13),
                      variable=self.ngay_var,
                      value=3).grid(row=3, column=1, padx=10, sticky="w")
        tk.Radiobutton(self.thongke_frame,
                      text="7 days",
                      font=("Segoe UI", 13),
                      variable=self.ngay_var,
                      value=7).grid(row=3, column=2, padx=10, sticky="w")
        tk.Radiobutton(self.thongke_frame,
                      text="30 days",
                      font=("Segoe UI", 13),
                      variable=self.ngay_var,
                      value=30).grid(row=3, column=3, padx=10, sticky="w")
        
        self.admin_window.mainloop()