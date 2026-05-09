import tkinter as tk
from tkinter import messagebox

from controllers.sale_controller import SaleController


class SaleView:

    def __init__(self):

        self.controller = SaleController(self)

        self.window = tk.Toplevel()
        self.window.title("💰 BÁN TRUYỆN")
        self.window.geometry("400x300")

        tk.Label(self.window, text="BÁN TRUYỆN",
                 font=("Arial", 14, "bold")).pack(pady=10)

        tk.Label(self.window, text="ID khách").pack()
        self.customer = tk.Entry(self.window)
        self.customer.pack()

        tk.Label(self.window, text="ID truyện").pack()
        self.comic = tk.Entry(self.window)
        self.comic.pack()

        tk.Label(self.window, text="Số lượng").pack()
        self.qty = tk.Entry(self.window)
        self.qty.pack()

        tk.Button(
            self.window,
            text="Bán",
            width=20,
            command=self.controller.sell_comic
        ).pack(pady=10)

    def input_sale(self):

        return (
            self.customer.get(),
            self.comic.get(),
            int(self.qty.get())
        )

    def show_message(self, msg):
        messagebox.showinfo("OK", msg)