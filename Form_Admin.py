import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from Class_UserManage import UserManage
from Class_Admin import Admin

def show_admin_form(admin_user):
    def chon_dong(event):
        chon = tree.selection()
        if chon:
            username = tree.item(chon[0])['values'][0]
            username_var.set(username)
            notes = users_data.get(username, {}).get('notes', [])
            soluong_var.set(str(len(notes)))
            
            # Xóa bảng note cũ
            for i in notes_tree.get_children():
                notes_tree.delete(i)
            # Thêm note mới
            for note in notes:
                title = note.get('title', '')
                created_goc = note.get('created', note.get('created_at', ''))
                updated_goc = note.get('updated', note.get('updated_at', ''))
                created = date(created_goc)
                updated = date(updated_goc)
                notes_tree.insert("", tk.END, values=(title, created, updated))
                
    def cap_nhat_du_lieu():
        for i in tree.get_children():
            tree.delete(i)
        for username in users_data:
            tree.insert("", tk.END, values=(username,))  
        
    def date(dt_str):
        try:
            # Nếu chuỗi đúng định dạng ISO, cắt lấy ngày
            return datetime.fromisoformat(dt_str).strftime('%Y-%m-%d')
        except Exception:
            # Nếu lỗi (ví dụ chuỗi trống hoặc không hợp lệ), lấy 10 ký tự đầu
            return dt_str[:10] if dt_str else ''
        
    admin = Admin(admin_user.username, admin_user.password)
    user_manager = UserManage()
    users_data = user_manager.load_users()

    # //* Xây giao diện *\\
    admin_window = tk.Tk()
    admin_window.title("Admin")
    admin_window.geometry("840x520")
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
    heading_frame.pack(padx=10, pady=10, fill="x")
    
    heading_frame.grid_columnconfigure(0, weight=1)
    heading_frame.grid_columnconfigure(1, weight=0)
    heading_frame.grid_columnconfigure(2, weight=1)
    
    tk.Label(heading_frame,
             text="Quản lý Note-Taking",
             font=("Segoe UI", 21, "bold"),
             foreground="#1976d2"
             ).grid(row=0, column=1, pady=10)
    
    tk.Button(heading_frame,
              text="Logout",
              font=("Segoe UI", 11, "bold"),
              command=lambda:admin.dang_xuat(user_manager, admin_window),
              bg="#e53935",
              fg="white",
              relief=tk.FLAT,
              borderwidth=0,
              padx=12,
              pady=4
              ).grid(row=0, column=2, padx=10, pady=10)
    
    # ========================== Xây Body ==========================
    body_frame = tk.Frame(admin_window)
    body_frame.pack(padx=10, pady=10, fill="both", expand=True)
    
    # ======== Xây Treeview ========
    ds_user_frame = tk.Frame(body_frame)
    ds_user_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ewsn")
    tree = ttk.Treeview(ds_user_frame, columns=("username"), show="headings")
    tree.heading("username", text="Danh sách User")
    tree.pack()
    for username, info in users_data.items():
        if info.get("role", "user") == "user":
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
    tk.Entry(thongke_frame,
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
    tk.Entry(thongke_frame,
            textvariable=soluong_var,
            font=("Segoe UI", 13),
            state="readonly",
            width=15
            ).grid(row=2, column=1, padx=10, sticky="w", columnspan=2)
    tk.Label(thongke_frame,
             text="Lịch sử tạo note",
             font=("Segoe UI", 13)
             ).grid(row=3, column=0, padx=10, sticky="w")
    
    # Treeview hiển thị note của user
    notes_frame = tk.Frame(thongke_frame)
    notes_frame.grid(row=4, rowspan=2, column=0, columnspan=2, padx=10, pady=10)
    
    notes_tree = ttk.Treeview(
        notes_frame, 
        columns=("title", "created_at", "updated_at"), 
        show="headings",
        height=6
    )
    notes_tree.heading("title", text="Tiêu đề")
    notes_tree.heading("created_at", text="Ngày tạo")
    notes_tree.heading("updated_at", text="Ngày sửa")
    notes_tree.column("title", width=100)
    notes_tree.column("created_at", width=200)
    notes_tree.column("updated_at", width=200)
    notes_tree.pack(expand=True)
    
    
    admin_window.mainloop()



    