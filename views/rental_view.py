import tkinter as tk
from tkinter import messagebox

from controllers.rental_controller import RentalController


class RentalView:

    def __init__(self):

        self.controller = RentalController(self)

        self.window = tk.Toplevel()
        self.window.title("📖 THUÊ TRUYỆN")
        self.window.geometry("400x250")

        tk.Label(self.window, text="THUÊ TRUYỆN",
                 font=("Arial", 14, "bold")).pack(pady=10)

        tk.Label(self.window, text="ID khách").pack()
        self.customer = tk.Entry(self.window)
        self.customer.pack()

        tk.Label(self.window, text="ID truyện").pack()
        self.comic = tk.Entry(self.window)
        self.comic.pack()

        tk.Button(
            self.window,
            text="Thuê",
            width=20,
            command=self.controller.rent_comic
        ).pack(pady=10)

    def input_rental(self):
        return (
            self.customer.get(),
            self.comic.get()
        )

    def show_message(self, msg):
        messagebox.showinfo("Thông báo", msg)