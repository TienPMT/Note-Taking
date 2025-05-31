import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

def show_admin_form():
    def doc_du_lieu(tenfile):
        if os.path.exists(tenfile):
            with open(tenfile, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    def cap_nhat_du_lieu():
        for i in tree.get_children():
            tree.delete(i)
        for username in users_data:
            tree.insert("", tk.END, values=(username,))
    
    def chon_dong(event):
        chon = tree.selection()
        if chon:
            username = tree.item(chon[0])['values'][0]
            username_var.set(username)
            notes = users_data.get(username, {}).get('notes', [])
            soluong_var.set(str(len(notes)))

            
    users_data = doc_du_lieu("Users_Data.json")

    # //* Xây giao diện *\\
    admin_window = tk.Tk()
    admin_window.title("Admin")
    admin_window.geometry("800x480")
    admin_window.resizable(True, True)
    admin_window.configure(bg="#f0f4f8")
    
    style = ttk.Style(admin_window)
    style.theme_use("clam")
    style.configure("Treeview", font=("Segoe UI", 12), rowheight=28)
    style.configure("Treeview.Heading", font=("Segoe UI", 13, "bold"))
    style.configure("TFrame", background="#f0f4f8")
    style.configure("TLabel", background="#f0f4f8", font=("Segoe UI", 12))
    style.configure("TButton", font=("Segoe UI", 11, "bold"))
    
    # ========================== Xây Heading ==========================
    heading_frame = tk.Frame(admin_window)
    tk.Label(heading_frame,
             text="Quản lý Note-Taking",
             font=("Segoe UI", 21, "bold"),
             foreground="#1976d2"
             ).pack(padx=10, pady=10)
    heading_frame.pack(padx=10, pady=10, fill="x")
    
    # ========================== Xây Body ==========================
    body_frame = tk.Frame(admin_window)
    body_frame.pack(padx=10, pady=10, fill="both", expand=True)
    
    # ======== Xây Treeview ========
    ds_user_frame = tk.Frame(body_frame)
    ds_user_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ewsn")
    tree = ttk.Treeview(ds_user_frame, columns=("username"), show="headings")
    tree.heading("username", text="Danh sách User")
    tree.pack()
    for username in users_data:
        tree.insert("", "end", values=(username,))
    tree.bind("<<TreeviewSelect>>", chon_dong)

    # ============ Xây dụng thống kê =============
    thongke_frame = tk.Frame(body_frame)
    thongke_frame.grid(row=0, column=1, padx=10, sticky="ewsn")
    tk.Label(thongke_frame,
             text="Thống kê",
             font=("Segoe UI", 15, "bold"),
             ).grid(row=0, column=0, columnspan=2, padx=10, sticky="w")
    tk.Label(thongke_frame,
             text="Username: ",
             font=("Segoe UI", 13)
             ).grid(row=1, column=0, padx=10, sticky="w")
    username_var = tk.StringVar()
    username_entry = tk.Entry(thongke_frame,
                              textvariable=username_var,
                              font=("Segoe UI", 13),
                              state="readonly",
                              width=15
                              ).grid(row=1, column=1, padx=10, sticky="w", columnspan=2)
    tk.Label(thongke_frame,
             text="Số lượng Note: ",
             font=("Segoe UI", 13)
             ).grid(row=2, column=0, padx=10, sticky="w")
    soluong_var = tk.StringVar()
    soluong_entry = tk.Entry(thongke_frame,
                             textvariable=soluong_var,
                              font=("Segoe UI", 13),
                              state="readonly",
                              width=15
                              ).grid(row=2, column=1, padx=10, sticky="w", columnspan=2)
    tk.Label(thongke_frame,
             text="Lịch sử tạo note",
             font=("Segoe UI", 13)
             ).grid(row=3, column=0, padx=10, sticky="w")
    
    ngay_var = tk.IntVar(value=3)
    tk.Radiobutton(thongke_frame,
                   text="3 days",
                   font=("Segoe UI", 13),
                   variable=ngay_var,
                   value=3).grid(row=3, column=1, padx=10, sticky="w")
    tk.Radiobutton(thongke_frame,
                   text="7 days",
                   font=("Segoe UI", 13),
                   variable=ngay_var,
                   value=7).grid(row=3, column=2, padx=10, sticky="w")
    tk.Radiobutton(thongke_frame,
                   text="30 days",
                   font=("Segoe UI", 13),
                   variable=ngay_var,
                   value=30).grid(row=3, column=3, padx=10, sticky="w")
    
    admin_window.mainloop()

show_admin_form()