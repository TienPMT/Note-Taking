# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import messagebox

class Form_NoteList:
    def __init__(self, user, parent_window=None):
        self.user = user
        self.parent_window = parent_window
        self.window = tk.Toplevel()
        self.window.title(f"Danh sách ghi chú của {user.username}")
        self.window.geometry("540x520")
        self.window.configure(bg="#f0f4fb")
        self.window.resizable(False, False)

        # ====== HEADER ======
        header = tk.Frame(self.window, bg="#f0f4fb")
        header.pack(fill="x", pady=(18, 0))
        tk.Label(header, text="📋 Danh Sách Ghi Chú", font=("Segoe UI", 18, "bold"), bg="#f0f4fb", fg="#1976d2").pack(side="left", padx=(22,0))
        tk.Label(header, text=f"👤 {user.username}", font=("Segoe UI", 11), bg="#f0f4fb", fg="#445").pack(side="right", padx=(0,22), pady=4)

        # ====== LISTBOX + SCROLLBAR ======
        list_frame = tk.Frame(self.window, bg="#f0f4fb")
        list_frame.pack(padx=24, pady=(18,10), fill="both", expand=True)

        self.listbox = tk.Listbox(list_frame, width=56, height=16, font=("Segoe UI", 12), bg="#fff", fg="#223", relief=tk.FLAT, selectbackground="#b3d7ff", activestyle="none")
        self.listbox.pack(side="left", fill="both", expand=True)
        self.listbox.bind("<Double-1>", self.show_note_detail)

        scrollbar = tk.Scrollbar(list_frame, orient="vertical", command=self.listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.listbox.config(yscrollcommand=scrollbar.set)

        self.load_notes()

        # ====== BUTTONS ======
        button_frame = tk.Frame(self.window, bg="#f0f4fb")
        button_frame.pack(pady=(8, 18))

        btn_back = tk.Button(button_frame, text="⬅️ Quay lại", width=15, bg="#6c757d", fg="white", font=("Segoe UI", 11),
                             command=self.go_back, cursor="hand2", relief=tk.FLAT)
        btn_back.grid(row=0, column=0, padx=12, pady=6, ipady=2)
        btn_back.bind("<Enter>", lambda e: btn_back.config(bg="#495057"))
        btn_back.bind("<Leave>", lambda e: btn_back.config(bg="#6c757d"))

        self.btn_delete = tk.Button(button_frame, text="🗑️ Xoá ghi chú", width=15, bg="#e53935", fg="white", font=("Segoe UI", 11, "bold"),
                                   command=self.delete_note, cursor="hand2", relief=tk.FLAT)
        self.btn_delete.grid(row=0, column=1, padx=12, pady=6, ipady=2)
        self.btn_delete.bind("<Enter>", lambda e: self.btn_delete.config(bg="#b71c1c"))
        self.btn_delete.bind("<Leave>", lambda e: self.btn_delete.config(bg="#e53935"))

        self.window.protocol("WM_DELETE_WINDOW", self.go_back)

    def load_notes(self):
        self.listbox.delete(0, tk.END)
        notes = getattr(self.user, 'notes', [])
        if not notes:
            messagebox.showinfo("Thông báo", "Chưa có ghi chú nào.")
            return
        for idx, note in enumerate(notes):
            self.listbox.insert(tk.END, f"{idx + 1}. {note.title}")

    def show_note_detail(self, event):
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            notes = getattr(self.user, 'notes', [])
            if index < len(notes):
                note = notes[index]
                messagebox.showinfo(f"Nội dung: {note.title}", note.content)
    
    def delete_note(self):
        notes = getattr(self.user, 'notes', [])
        idx = self.listbox.curselection()
        if not idx or not notes:
            messagebox.showwarning("Chưa chọn ghi chú", "Vui lòng chọn ghi chú muốn xoá.")
            return
        note = notes[idx[0]]
        title = getattr(note, "title", "Ghi chú") if hasattr(note, "title") else note.get("title", "Ghi chú")
        if messagebox.askyesno("Xác nhận xoá", f"Bạn chắc chắn muốn xoá ghi chú \"{title}\"?"):
            del notes[idx[0]]
            self.load_notes()
            from Class_UserManage import UserManage
            manager = UserManage()
            manager.update_user_notes(self.user.username, notes)
            messagebox.showinfo("Đã xoá", f"Đã xoá ghi chú \"{title}\".")

    def go_back(self):
        self.window.destroy()
        if self.parent_window:
            self.parent_window.deiconify()

def show_note_list(user, parent_window=None):
    Form_NoteList(user, parent_window)
