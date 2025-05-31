# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import messagebox
from Form_EditNote import show_edit_note_form

class Form_SearchNote:
    def __init__(self, user, parent_window=None):
        self.user = user
        self.parent_window = parent_window
        self.window = tk.Toplevel()
        self.window.title(f"Tìm kiếm ghi chú của {user.username}")
        self.window.geometry("450x400")

        self.window.protocol("WM_DELETE_WINDOW", self.on_close)

        tk.Label(self.window, text="Nhập từ khóa tìm kiếm:", font=("Arial", 12)).pack(pady=5)
        self.entry_search = tk.Entry(self.window, width=40)
        self.entry_search.pack(pady=5)

        tk.Button(self.window, text="Tìm kiếm", command=self.search).pack(pady=5)

        self.listbox = tk.Listbox(self.window, width=60, height=15)
        self.listbox.pack(pady=10)

        tk.Button(self.window, text="Xem / Chỉnh sửa", command=self.edit_note).pack(pady=5)

        self.search_results = []

    def search(self):
        keyword = self.entry_search.get().strip().lower()
        self.listbox.delete(0, tk.END)
        self.search_results = []

        if not keyword:
            messagebox.showwarning("Chú ý", "Vui lòng nhập từ khóa tìm kiếm")
            return

        for note in self.user.notes:
            if keyword in note.title.lower() or keyword in note.content.lower():
                self.search_results.append(note)

        if not self.search_results:
            messagebox.showinfo("Kết quả", "Không tìm thấy ghi chú phù hợp")
            return

        for idx, note in enumerate(self.search_results):
            self.listbox.insert(tk.END, f"{idx + 1}. {note.title}")

    def edit_note(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("Chú ý", "Vui lòng chọn ghi chú để xem/chỉnh sửa")
            return
        index = selected[0]
        note = self.search_results[index]
        
        def on_update():
            self.search()

        show_edit_note_form(self.user, note, on_update)

    def on_close(self):
        self.window.destroy()
        if self.parent_window:
            self.parent_window.deiconify()

def search_note(user, parent_window=None):
    Form_SearchNote(user, parent_window)
