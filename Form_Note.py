import tkinter as tk

def show_note():
    # Xây dựng form
    note_form = tk.Tk()
    note_form.title("<Name>")
    note_form.geometry("360x480")
    note_form.resizable(False, False)

    # Cấu hình lưới cột
    note_form.columnconfigure(0, weight=1)  # Cột đầu tiên chứa nút New
    note_form.columnconfigure(1, weight=1)  # Cột giữa để giãn
    note_form.columnconfigure(2, weight=1)  # Cột cuối cùng chứa nút Login


    # Tên note
    note_title = tk.Label(note_form,
                          text="Title",
                          font=("Times New Roman", 16, "bold")
                          )
    note_title.grid(row=0, column=0, padx=10, pady=10)

    note_title_entry = tk.Entry(note_form,
                                font=("Times New Roman", 14)
                                )
    note_title_entry.grid(row=0, column=1, columnspan=2, padx=10, sticky="ew")


    # Nội dung
    note_body = tk.Text(note_form,
                         font=("Times New Roman", 14),
                         height=15,
                         width=50
                         )
    note_body.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    # Nút Save
    save_button = tk.Button(note_form,
                            text="Save",
                            font=("Times New Roman", 16, "bold"),
                            relief="solid",
                            bd=2
                            )
    save_button.grid(row=2, column=2, padx=10, pady=10)


    # Chạy giao diện
    note_form.mainloop()