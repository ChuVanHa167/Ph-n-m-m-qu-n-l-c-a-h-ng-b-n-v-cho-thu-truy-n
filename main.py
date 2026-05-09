from controllers.comic_controller import (
    ComicController
)

from controllers.customer_controller import (
    CustomerController
)

from views.comic_view import ComicView

from views.customer_view import (
    CustomerView
)

from controllers.inventory_controller import (
    InventoryController
)

from views.inventory_view import (
    InventoryView
)

from controllers.rental_controller import (
    RentalController
)

from views.rental_view import (
    RentalView
)

from controllers.sale_controller import (
    SaleController
)

from views.sale_view import (
    SaleView
)
from config.database import Database


def main():

    db = Database()

    db.create_tables()

    comic_view = ComicView()

    comic_controller = (
        ComicController(comic_view)
    )

    customer_view = CustomerView()

    customer_controller = (
        CustomerController(customer_view)
    )

    inventory_view = InventoryView()

    inventory_controller = (
        InventoryController(
            inventory_view
        )
    )

    rental_view = RentalView()

    rental_controller = (
        RentalController(rental_view)
    )

    sale_view = SaleView()

    sale_controller = (
        SaleController(sale_view)
    )

    while True:

        print("\n===== HỆ THỐNG =====")

        print("\n--- QUẢN LÝ TRUYỆN ---")

        print("1. Thêm truyện")
        print("2. Hiển thị truyện")
        print("3. Cập nhật truyện")
        print("4. Xóa truyện")
        print("5. Tìm kiếm truyện")
        print("6. Thuê truyện")

        print("\n--- QUẢN LÝ KHÁCH HÀNG ---")

        print("7. Thêm khách hàng")
        print("8. Hiển thị khách hàng")
        print("9. Cập nhật khách hàng")
        print("10. Xóa khách hàng")
        print("11. Tìm kiếm khách hàng")

        print("\n--- QUẢN LÝ KHO ---")

        print("12. Nhập kho")
        print("13. Xuất kho")
        print("14. Chuyển truyện ra kệ")
        print("15. Xem log kho")

        print("\n--- QUẢN LÝ THUÊ ---")

        print("16. Thuê truyện")
        print("17. Trả truyện")
        print("18. Lịch sử thuê")

        print("\n--- QUẢN LÝ BÁN ---")

        print("19. Bán truyện")
        print("20. Lịch sử bán")
        print("21. Xem doanh thu")

        print("\n0. Thoát")

        choice = input("\nChọn: ")

        # ======================
        # COMICS
        # ======================

        if choice == "1":
            comic_controller.add_comic()

        elif choice == "2":
            comic_controller.show_comics()

        elif choice == "3":
            comic_controller.update_comic()

        elif choice == "4":
            comic_controller.delete_comic()

        elif choice == "5":
            comic_controller.search_comic()

        elif choice == "6":
            comic_controller.rent_comic()

        # ======================
        # CUSTOMERS
        # ======================

        elif choice == "7":
            customer_controller.add_customer()

        elif choice == "8":
            customer_controller.show_customers()

        elif choice == "9":
            customer_controller.update_customer()

        elif choice == "10":
            customer_controller.delete_customer()

        elif choice == "11":
            customer_controller.search_customer()

        # ======================
        # INVENTORY
        # ======================
        elif choice == "12":

            inventory_controller.import_stock()

        elif choice == "13":

            inventory_controller.export_stock()

        elif choice == "14":

            inventory_controller.move_to_display()

        elif choice == "15":

            inventory_controller.show_logs()

        # ======================
        # RENTAL
        # ======================
        elif choice == "16":

            rental_controller.rent_comic()

        elif choice == "17":

            rental_controller.return_comic()

        elif choice == "18":

            rental_controller.show_rentals()

        # ======================
        # SALE
        # ======================

        elif choice == "19":

            sale_controller.sell_comic()

        elif choice == "20":

            sale_controller.show_sales()

        elif choice == "21":

            sale_controller.show_revenue()
        # ======================
        # EXIT
        # ======================

        elif choice == "0":

            print("Thoát chương trình.")

            db.close_connection()

            break

        else:

            print(
                "Lựa chọn không hợp lệ."
            )


if __name__ == "__main__":
    main()