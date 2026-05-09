import tkinter as tk
from tkinter import ttk, messagebox

from controllers.customer_controller import CustomerController


class CustomerView:

    def __init__(self):

        self.controller = CustomerController(self)

        self.window = tk.Toplevel()
        self.window.title("👤 KHÁCH HÀNG")
        self.window.geometry("900x500")

        self.build_ui()
        self.controller.show_customers()

    def build_ui(self):

        tk.Label(self.window, text="QUẢN LÝ KHÁCH HÀNG",
                 font=("Arial", 16, "bold")).pack(pady=10)

        form = tk.Frame(self.window)
        form.pack()

        labels = ["Tên", "SĐT"]
        self.entries = []

        for i, text in enumerate(labels):
            tk.Label(form, text=text).grid(row=0, column=i)
            e = tk.Entry(form)
            e.grid(row=1, column=i, padx=5)
            self.entries.append(e)

        tk.Button(
            self.window,
            text="➕ Thêm khách",
            command=self.controller.add_customer
        ).pack(pady=5)

        self.table = ttk.Treeview(
            self.window,
            columns=("id", "name", "phone"),
            show="headings"
        )

        self.table.heading("id", text="ID")
        self.table.heading("name", text="Tên")
        self.table.heading("phone", text="SĐT")

        self.table.pack(fill="both", expand=True)

    def input_customer(self):

        return (
            "CUST_" + self.entries[0].get(),
            self.entries[0].get(),
            self.entries[1].get(),
            "",
            ""
        )

    def display_customers(self, customers):

        self.table.delete(*self.table.get_children())

        for c in customers:
            self.table.insert("", "end", values=(
                c.customer_id,
                c.name,
                c.phone
            ))

    def show_message(self, msg):
        messagebox.showinfo("OK", msg)
        self.controller.show_customers()