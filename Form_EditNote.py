import tkinter as tk
from tkinter import messagebox
import datetime

class Form_EditNote:
    def __init__(self, user, note, on_update=None):
        # ==== Color palette ====
        BG = "#e3f2fd"
        HEADER = "#1976d2"
        BTN_SAVE = "#43a047"
        BTN_SAVE_TEXT = "white"
        BTN_CANCEL = "#e53935"
        BTN_CANCEL_TEXT = "white"
        ENTRY_BG = "#ffffff"

        self.user = user
        self.note = note
        self.on_update = on_update

        self.window = tk.Toplevel()
        self.window.title("Chỉnh sửa ghi chú")
        self.window.geometry("420x430")
        self.window.configure(bg=BG)

        # ==== Header ====
        tk.Label(
            self.window, text="📝 Chỉnh sửa ghi chú",
            font=("Segoe UI", 15, "bold"),
            fg=HEADER, bg=BG, pady=14
        ).pack()

        # ==== Tiêu đề ====
        frame_title = tk.Frame(self.window, bg=BG)
        frame_title.pack(pady=(10, 0))
        tk.Label(
            frame_title, text="Tiêu đề:",
            font=("Segoe UI", 11, "bold"),
            bg=BG
        ).pack(anchor="w", padx=5)
        self.entry_title = tk.Entry(
            frame_title, width=38, font=("Segoe UI", 11),
            bg=ENTRY_BG, relief=tk.FLAT
        )
        self.entry_title.pack(padx=5, pady=(2, 8))
        self.entry_title.insert(0, self.note.title)

        # ==== Nội dung ====
        frame_content = tk.Frame(self.window, bg=BG)
        frame_content.pack(pady=(0, 0))
        tk.Label(
            frame_content, text="Nội dung:",
            font=("Segoe UI", 11, "bold"),
            bg=BG
        ).pack(anchor="w", padx=5)
        self.text_content = tk.Text(
            frame_content, height=10, width=38,
            font=("Segoe UI", 11), bg=ENTRY_BG, relief=tk.FLAT
        )
        self.text_content.pack(padx=5, pady=(2, 8))
        self.text_content.insert("1.0", self.note.content)

        # ==== Button frame ====
        btn_frame = tk.Frame(self.window, bg=BG)
        btn_frame.pack(pady=15)

        btn_save = tk.Button(
            btn_frame, text="💾 Lưu thay đổi", width=16,
            font=("Segoe UI", 10, "bold"),
            bg=BTN_SAVE, fg=BTN_SAVE_TEXT, relief=tk.FLAT, cursor="hand2",
            command=self.save_changes
        )
        btn_save.grid(row=0, column=0, padx=8, ipadx=2)

        btn_cancel = tk.Button(
            btn_frame, text="Hủy", width=8,
            font=("Segoe UI", 10, "bold"),
            bg=BTN_CANCEL, fg=BTN_CANCEL_TEXT, relief=tk.FLAT, cursor="hand2",
            command=self.window.destroy
        )
        btn_cancel.grid(row=0, column=1, padx=8, ipadx=2)


    def save_changes(self):
        new_title = self.entry_title.get().strip()
        new_content = self.text_content.get("1.0", "end-1c").strip()
        
        if not new_title or not new_content:
            messagebox.showwarning("Lỗi", "Vui lòng nhập đầy đủ tiêu đề và nội dung")
            return

        self.note.title = new_title
        self.note.content = new_content
        self.note.updated_at = datetime.datetime.now().isoformat()
        
        messagebox.showinfo("Thành công", "Ghi chú đã được cập nhật")
        
        # Sau khi note đã được chỉnh sửa, cần thực hiện:
        from Class_UserManage import UserManage
        manager = UserManage()
        notes_dict_list = [n.to_dict() for n in self.user.notes]  # hoặc self.notes nếu bạn dùng biến này
        manager.update_user_notes(self.user.username, notes_dict_list)
        
        self.window.destroy()

        if self.on_update:
            self.on_update()
            
def show_edit_note_form(user, note, on_update=None):
    Form_EditNote(user, note, on_update)