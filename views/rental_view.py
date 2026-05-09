class RentalView:

    # =========================
    # INPUT RENT
    # =========================
    def input_rental(self):

        customer_id = input(
            "ID khách hàng: "
        )

        comic_id = input(
            "ID truyện: "
        )

        return (
            customer_id,
            comic_id
        )

    # =========================
    # INPUT RETURN
    # =========================
    def input_return(self):

        return input(
            "Nhập Rental ID: "
        )

    # =========================
    # DISPLAY
    # =========================
    def display_rentals(
        self,
        rentals
    ):

        if not rentals:

            print(
                "Không có lịch sử thuê."
            )

            return

        for rental in rentals:

            print(rental)

            print("-" * 40)

    # =========================
    # MESSAGE
    # =========================
    def show_message(self, message):

        print(message)