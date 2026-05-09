class Rental:

    def __init__(
        self,
        rental_id,
        customer_id,
        comic_id,
        rental_date,
        return_date,
        status,
        total_price
    ):

        self.rental_id = rental_id

        self.customer_id = customer_id

        self.comic_id = comic_id

        self.rental_date = rental_date

        self.return_date = return_date

        self.status = status

        self.total_price = total_price

    def __str__(self):

        return (
            f"\nRental ID: {self.rental_id}"
            f"\nKhách hàng: {self.customer_id}"
            f"\nTruyện: {self.comic_id}"
            f"\nNgày thuê: {self.rental_date}"
            f"\nNgày trả: {self.return_date}"
            f"\nTrạng thái: {self.status}"
            f"\nTổng tiền: {self.total_price}"
        )