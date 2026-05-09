class SaleView:

    # =========================
    # INPUT SALE
    # =========================
    def input_sale(self):

        customer_id = input(
            "ID khách hàng: "
        )

        comic_id = input(
            "ID truyện: "
        )

        quantity = int(
            input("Số lượng mua: ")
        )

        return (
            customer_id,
            comic_id,
            quantity
        )

    # =========================
    # DISPLAY SALES
    # =========================
    def display_sales(self, sales):

        if not sales:

            print(
                "Không có lịch sử bán."
            )

            return

        for sale in sales:

            print(sale)

            print("-" * 40)

    # =========================
    # DISPLAY REVENUE
    # =========================
    def display_revenue(self, revenue):

        print(
            f"\nTỔNG DOANH THU: "
            f"{revenue}"
        )

    # =========================
    # MESSAGE
    # =========================
    def show_message(self, message):

        print(message)