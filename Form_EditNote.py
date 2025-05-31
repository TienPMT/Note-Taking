# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import messagebox

class Form_EditNote:
    def __init__(self, user, note, on_update=None):
        self.user = user
        self.note = note
        self.on_update = on_update
        self.window = tk.Toplevel()
        self.window.title("Chỉnh sửa ghi chú")
        self.window.geometry("400x400")

        tk.Label(self.window, text="Tiêu đề:").pack(pady=5)
        self.entry_title = tk.Entry(self.window, width=40)
        self.entry_title.pack(pady=5)
        self.entry_title.insert(0, self.note.title)

        tk.Label(self.window, text="Nội dung:").pack(pady=5)
        self.text_content = tk.Text(self.window, height=10, width=40)
        self.text_content.pack(pady=5)
        self.text_content.insert("1.0", self.note.content)

        tk.Button(self.window, text="Lưu thay đổi", command=self.save_changes).pack(pady=10)


    def save_changes(self):
        new_title = self.entry_title.get().strip()
        new_content = self.text_content.get("1.0", "end-1c").strip()

        if not new_title or not new_content:
            messagebox.showwarning("Lỗi", "Vui lòng nhập đầy đủ tiêu đề và nội dung")
            return

        self.note.title = new_title
        self.note.content = new_content

        messagebox.showinfo("Thành công", "Ghi chú đã được cập nhật")
        self.window.destroy()

        if self.on_update:
            self.on_update()
            
def show_edit_note_form(user, note, on_update=None):
    Form_EditNote(user, note, on_update)