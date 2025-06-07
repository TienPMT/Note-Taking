# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import messagebox
from Form_EditNote import show_edit_note_form

class Form_SearchNote:
    def __init__(self, user, parent_window=None):
        # ==== Màu sắc chủ đạo ====
        BG = "#e3f2fd"
        HEADER = "#1976d2"
        BTN_SEARCH = "#1976d2"
        BTN_ACTION = "#43a047"
        BTN_BACK = "#e53935"
        TEXT_COLOR = "white"

        self.user = user
        self.parent_window = parent_window
        self.window = tk.Toplevel()
        self.window.title(f"Tìm kiếm ghi chú của {user.username}")
        self.window.geometry("500x500")
        self.window.configure(bg=BG)
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)

        # ==== Tiêu đề ====
        label_title = tk.Label(
            self.window,
            text=f"🔎 Tìm kiếm ghi chú của {user.username}",
            font=("Segoe UI", 15, "bold"),
            fg=HEADER,
            bg=BG,
            pady=10
        )
        label_title.pack()

        # ==== Nhập từ khóa ====
        search_frame = tk.Frame(self.window, bg=BG)
        search_frame.pack(pady=8)

        tk.Label(search_frame, text="Nhập từ khóa tìm kiếm:", font=("Segoe UI", 11), bg=BG).grid(row=0, column=0, sticky="w", pady=2)
        self.entry_search = tk.Entry(search_frame, width=32, font=("Segoe UI", 11))
        self.entry_search.grid(row=1, column=0, sticky="w", padx=2, pady=3)

        # ==== Nút tìm kiếm ====
        btn_search = tk.Button(
            search_frame, text="Tìm kiếm", width=10, font=("Segoe UI", 10, "bold"),
            bg=BTN_SEARCH, fg=TEXT_COLOR, relief=tk.FLAT, cursor="hand2",
            command=self.search
        )
        btn_search.grid(row=1, column=1, padx=(12,0), pady=3)

        # ==== Kết quả ====
        list_frame = tk.Frame(self.window, bg=BG)
        list_frame.pack(pady=10)
        self.listbox = tk.Listbox(list_frame, width=62, height=15, font=("Segoe UI", 10))
        self.listbox.pack()

        # ==== Footer button ====
        self.button_footer = tk.Frame(self.window, bg=BG)
        self.button_footer.pack(pady=12)
        btn_edit = tk.Button(
            self.button_footer, text="✏ Xem / Chỉnh sửa", width=17, font=("Segoe UI", 10, "bold"),
            bg=BTN_ACTION, fg=TEXT_COLOR, relief=tk.FLAT, cursor="hand2",
            command=self.edit_note
        )
        btn_edit.grid(row=0, column=0, padx=8, pady=5)

        btn_back = tk.Button(
            self.button_footer, text="⏪ Quay lại", width=10, font=("Segoe UI", 10, "bold"),
            bg=BTN_BACK, fg=TEXT_COLOR, relief=tk.FLAT, cursor="hand2",
            command=self.on_close
        )
        btn_back.grid(row=0, column=1, padx=8, pady=5)

        # ==== Biến lưu kết quả ====
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
