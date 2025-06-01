# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox
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
        self.window.geometry("800x800")
        self.window.configure(bg="#f4faff") 
        
        # Tiêu đề
        tk.Label(self.window, text="Tiêu đề:", font=("Arial", 13, "bold"), bg="#f4faff").pack(pady=8)
        self.entry_title = tk.Entry(self.window, width=60, font=("Arial", 13), bg="#ffffff", relief=tk.SOLID)
        self.entry_title.pack(pady=5)

        # Nội dung
        tk.Label(self.window, text="Nội dung:", font=("Arial", 13, "bold"), bg="#f4faff").pack(pady=8)
        self.text_content = tk.Text(self.window, height=20, width=70, font=("Arial", 13), bg="#ffffff", relief=tk.SOLID)
        self.text_content.pack(pady=5)

        # Nút lưu
        tk.Button(self.window, text="💾 Lưu ghi chú", width=25, bg="#28a745", fg="white",
                  font=("Arial", 12, "bold"), command=self.save_note).pack(pady=12)

        # Đường phân cách
        tk.Frame(self.window, height=2, bg="#cccccc").pack(fill="x", pady=8)

        # Nút điều hướng
        tk.Button(self.window, text="📋 Xem danh sách ghi chú", width=35, bg="#007bff", fg="white",
                  font=("Arial", 12), command=self.go_to_list).pack(pady=5)
        tk.Button(self.window, text="🔍 Tìm kiếm ghi chú", width=35, bg="#fd7e14", fg="white",
                  font=("Arial", 12), command=self.go_to_search).pack(pady=5)
        tk.Button(self.window, text="Đăng xuất", width=25, bg="#FF0000", fg="white",
                  font=("Arial", 12), command=self.logout).pack(pady=5)

        # Nếu là guest thì thêm nút đăng nhập / đăng ký
        if self.is_guest:
            tk.Button(self.window, text="🔑 Đăng nhập / Đăng ký", width=25, bg="#17a2b8", fg="white",
                      font=("Arial", 12), command=self.open_login_register).pack(pady=10)

        tk.Button(self.window, text="❌ Đóng", width=15, bg="#dc3545", fg="white",
                  font=("Arial", 12), command=self.window.destroy).pack(pady=12)

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
        from Form_Login import dangNhap
        dangNhap(self.window, self.handle_login_success)
        self.window.withdraw()
    
    def handle_login_success(self, user):
        if user.role == "admin":
            from Form_Admin import Form_Admin
            # Mở giao diện admin
            Form_Admin(user)
        else:
            Form_Note(user)
    
    def logout(self):
        self.user_manager.logout()
        self.window.destroy()
        from Form_Main import show_main_form
        show_main_form()

        
