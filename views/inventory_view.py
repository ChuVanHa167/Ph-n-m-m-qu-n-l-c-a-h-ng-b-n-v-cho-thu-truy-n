import tkinter as tk
from tkinter import ttk, messagebox


class InventoryView:

    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Quản lý kho truyện")
        self.window.geometry("800x500")

        self.build_ui()

    # =========================
    # UI
    # =========================
    def build_ui(self):

        tk.Label(
            self.window,
            text="QUẢN LÝ KHO TRUYỆN",
            font=("Arial", 16, "bold")
        ).pack(pady=10)

        frame = tk.Frame(self.window)
        frame.pack(pady=10)

        tk.Label(frame, text="ID truyện").grid(row=0, column=0)
        self.comic_id_entry = tk.Entry(frame)
        self.comic_id_entry.grid(row=0, column=1)

        tk.Label(frame, text="Số lượng").grid(row=1, column=0)
        self.quantity_entry = tk.Entry(frame)
        self.quantity_entry.grid(row=1, column=1)

        # Buttons
        tk.Button(
            self.window,
            text="Nhập kho",
            width=20,
            command=self.on_import
        ).pack(pady=5)

        tk.Button(
            self.window,
            text="Xuất kho",
            width=20,
            command=self.on_export
        ).pack(pady=5)

        tk.Button(
            self.window,
            text="Chuyển ra kệ",
            width=20,
            command=self.on_move
        ).pack(pady=5)

        # Log table
        self.tree = ttk.Treeview(
            self.window,
            columns=("id", "comic", "action", "qty", "note", "time"),
            show="headings"
        )

        self.tree.heading("id", text="ID")
        self.tree.heading("comic", text="Comic ID")
        self.tree.heading("action", text="Hành động")
        self.tree.heading("qty", text="Số lượng")
        self.tree.heading("note", text="Ghi chú")
        self.tree.heading("time", text="Thời gian")

        self.tree.pack(fill="both", expand=True)

    # =========================
    # INPUT
    # =========================
    def get_input(self):
        return (
            self.comic_id_entry.get(),
            int(self.quantity_entry.get())
        )

    # =========================
    # EVENTS (controller hook)
    # =========================
    def set_import_handler(self, handler):
        self.import_handler = handler

    def set_export_handler(self, handler):
        self.export_handler = handler

    def set_move_handler(self, handler):
        self.move_handler = handler

    def on_import(self):
        self.import_handler(*self.get_input())

    def on_export(self):
        self.export_handler(*self.get_input())

    def on_move(self):
        self.move_handler(*self.get_input())

    # =========================
    # DISPLAY LOGS
    # =========================
    def display_logs(self, logs):

        for item in self.tree.get_children():
            self.tree.delete(item)

        for log in logs:
            self.tree.insert("", "end", values=(
                log["log_id"],
                log["comic_id"],
                log["action_type"],
                log["quantity"],
                log["note"],
                log["created_at"]
            ))

    # =========================
    # MESSAGE
    # =========================
    def show_message(self, message):
        messagebox.showinfo("Thông báo", message)