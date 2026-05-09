from services.rental_service import (
    RentalService
)


class RentalController:

    def __init__(self, view):

        self.view = view

        self.rental_service = (
            RentalService()
        )

    # =========================
    # RENT
    # =========================
    def rent_comic(self):

        customer_id, comic_id = (
            self.view.input_rental()
        )

        result = (
            self.rental_service.rent_comic(
                customer_id,
                comic_id
            )
        )

        self.view.show_message(result)

    # =========================
    # RETURN
    # =========================
    def return_comic(self):

        rental_id = (
            self.view.input_return()
        )

        result = (
            self.rental_service.return_comic(
                rental_id
            )
        )

        self.view.show_message(result)

    # =========================
    # HISTORY
    # =========================
    def show_rentals(self):

        rentals = (
            self.rental_service
            .get_all_rentals()
        )

        self.view.display_rentals(
            rentals
        )