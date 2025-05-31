# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import messagebox

class Form_NoteList:
    def __init__(self, user, parent_window=None):
        self.user = user
        self.parent_window = parent_window
        self.window = tk.Toplevel()
        self.window.title(f"Danh sách ghi chú của {user.username}")
        self.window.geometry("400x400")

        self.listbox = tk.Listbox(self.window, width=50, height=20)
        self.listbox.pack(padx=10, pady=10)
        self.listbox.bind("<Double-1>", self.show_note_detail)

        self.load_notes()

        tk.Button(self.window, text="Quay lại", command=self.go_back).pack(pady=5)

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

    def go_back(self):
        self.window.destroy()
        if self.parent_window:
            self.parent_window.deiconify()

def show_note_list(user, parent_window=None):
    Form_NoteList(user, parent_window)
