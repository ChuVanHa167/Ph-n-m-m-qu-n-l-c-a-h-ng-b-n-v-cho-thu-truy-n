import tkinter as tk
from tkinter import ttk, messagebox

from controllers.comic_controller import ComicController


class ComicView:

    def __init__(self):

        self.controller = ComicController(self)

        self.window = tk.Toplevel()
        self.window.title("📚 QUẢN LÝ TRUYỆN")
        self.window.geometry("1000x600")

        self.selected_comic_id = None

        self.build_ui()
        self.controller.show_comics()

    # =========================
    # UI
    # =========================
    def build_ui(self):

        # ===== TITLE =====
        title = tk.Label(
            self.window,
            text="QUẢN LÝ TRUYỆN",
            font=("Arial", 18, "bold")
        )
        title.pack(pady=10)

        # =========================
        # SEARCH BAR
        # =========================
        search_frame = tk.Frame(self.window)
        search_frame.pack(pady=5)

        tk.Label(search_frame, text="🔍 Tìm tên:").pack(side=tk.LEFT)

        self.search_entry = tk.Entry(search_frame, width=30)
        self.search_entry.pack(side=tk.LEFT, padx=5)

        tk.Button(
            search_frame,
            text="Tìm",
            command=self.controller.search_comic
        ).pack(side=tk.LEFT)

        tk.Button(
            search_frame,
            text="Reset",
            command=self.controller.show_comics
        ).pack(side=tk.LEFT, padx=5)

        # =========================
        # FORM
        # =========================
        form = tk.Frame(self.window)
        form.pack(pady=10)

        labels = ["ID", "Tên", "Giá"]
        self.entries = []

        for i, text in enumerate(labels):
            tk.Label(form, text=text).grid(row=0, column=i)
            e = tk.Entry(form, width=20)
            e.grid(row=1, column=i, padx=5)
            self.entries.append(e)

        self.id_entry = self.entries[0]
        self.name_entry = self.entries[1]
        self.price_entry = self.entries[2]

        # ID chỉ đọc khi chọn dòng
        self.id_entry.config(state="readonly")

        # =========================
        # BUTTONS
        # =========================
        btn_frame = tk.Frame(self.window)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="➕ Thêm", width=12,
                  command=self.controller.add_comic).grid(row=0, column=0, padx=5)

        tk.Button(btn_frame, text="✏️ Sửa", width=12,
                  command=self.controller.update_comic).grid(row=0, column=1, padx=5)

        tk.Button(btn_frame, text="🗑 Xóa", width=12,
                  command=self.controller.delete_comic).grid(row=0, column=2, padx=5)

        # =========================
        # TABLE
        # =========================
        self.table = ttk.Treeview(
            self.window,
            columns=("id", "name", "price"),
            show="headings",
            selectmode="browse"
        )

        self.table.heading("id", text="ID")
        self.table.heading("name", text="Tên truyện")
        self.table.heading("price", text="Giá")

        self.table.pack(fill="both", expand=True, pady=10)

        # click row
        self.table.bind("<<TreeviewSelect>>", self.on_row_select)

    # =========================
    # CLICK ROW -> AUTO FILL
    # =========================
    def on_row_select(self, event):

        selected = self.table.focus()
        data = self.table.item(selected, "values")

        if not data:
            return

        self.selected_comic_id = data[0]

        # unlock id for insert
        self.id_entry.config(state="normal")

        self.id_entry.delete(0, tk.END)
        self.id_entry.insert(0, data[0])

        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, data[1])

        self.price_entry.delete(0, tk.END)
        self.price_entry.insert(0, data[2])

        self.id_entry.config(state="readonly")

    # =========================
    # INPUT
    # =========================
    def input_comic(self):

        return (
            self.selected_comic_id,   # update theo row chọn
            self.name_entry.get(),
            "",
            "",
            float(self.price_entry.get()),
            float(self.price_entry.get()),
            0,
            0
        )

    # =========================
    # DELETE INPUT
    # =========================
    def input_delete_id(self):
        return self.selected_comic_id

    # =========================
    # SEARCH INPUT
    # =========================
    def input_search_keyword(self):
        return self.search_entry.get()

    # =========================
    # DISPLAY
    # =========================
    def display_comics(self, comics):

        self.table.delete(*self.table.get_children())

        for c in comics:
            self.table.insert("", "end", values=(
                c.comic_id,
                c.title,
                c.price
            ))

    # =========================
    # MESSAGE
    # =========================
    def show_message(self, msg):

        messagebox.showinfo("Thông báo", msg)
        self.controller.show_comics()