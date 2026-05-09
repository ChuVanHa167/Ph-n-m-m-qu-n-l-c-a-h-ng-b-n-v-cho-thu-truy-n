import tkinter as tk

from views.comic_view import ComicView
from views.customer_view import CustomerView
from views.rental_view import RentalView
from views.sale_view import SaleView
from views.inventory_view import InventoryView


class MainView:

    def __init__(self):

        self.root = tk.Tk()
        self.root.title("📚 QUẢN LÝ CỬA HÀNG TRUYỆN")
        self.root.geometry("1000x700")

        self.build_ui()
        self.root.mainloop()

    def build_ui(self):

        tk.Label(
            self.root,
            text="HỆ THỐNG QUẢN LÝ CỬA HÀNG TRUYỆN",
            font=("Arial", 18, "bold")
        ).pack(pady=10)

        # =========================
        # FRAME CHỨC NĂNG
        # =========================
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        # =========================
        # TRUYỆN (1-6)
        # =========================
        tk.Label(frame, text="QUẢN LÝ TRUYỆN",
                 font=("Arial", 12, "bold")).grid(row=0, column=0, pady=5)

        tk.Button(frame, text="Thêm / Sửa / Xóa / Tìm",
                  width=25, command=self.open_comic).grid(row=1, column=0)

        # =========================
        # KHÁCH HÀNG (7-11)
        # =========================
        tk.Label(frame, text="QUẢN LÝ KHÁCH HÀNG",
                 font=("Arial", 12, "bold")).grid(row=0, column=1)

        tk.Button(frame, text="CRUD Khách hàng",
                  width=25, command=self.open_customer).grid(row=1, column=1)

        # =========================
        # KHO (12-15)
        # =========================
        tk.Label(frame, text="QUẢN LÝ KHO",
                 font=("Arial", 12, "bold")).grid(row=2, column=0)

        tk.Button(frame, text="Nhập / Xuất / Chuyển / Log",
                  width=25, command=self.open_inventory).grid(row=3, column=0)

        # =========================
        # THUÊ (16-18)
        # =========================
        tk.Label(frame, text="THUÊ TRUYỆN",
                 font=("Arial", 12, "bold")).grid(row=2, column=1)

        tk.Button(frame, text="Thuê / Trả / Lịch sử",
                  width=25, command=self.open_rental).grid(row=3, column=1)

        # =========================
        # BÁN (19-21)
        # =========================
        tk.Label(frame, text="BÁN TRUYỆN",
                 font=("Arial", 12, "bold")).grid(row=4, column=0)

        tk.Button(frame, text="Bán / Doanh thu",
                  width=25, command=self.open_sale).grid(row=5, column=0)

    # =========================
    # OPEN MODULES
    # =========================
    def open_comic(self):
        ComicView()

    def open_customer(self):
        CustomerView()

    def open_rental(self):
        RentalView()

    def open_sale(self):
        SaleView()

    def open_inventory(self):
        InventoryView()