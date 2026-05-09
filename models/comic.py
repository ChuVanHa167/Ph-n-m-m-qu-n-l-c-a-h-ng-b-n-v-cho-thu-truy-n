class Comic:

    def __init__(
        self,
        comic_id,
        title,
        author,
        genre,
        price,
        rental_price,
        quantity,
        stock_quantity,
        is_rented=False
    ):

        self.comic_id = comic_id
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price
        self.rental_price = rental_price
        self.quantity = quantity
        self.stock_quantity = stock_quantity
        self.is_rented = is_rented

    def __str__(self):

        status = (
            "Đang thuê"
            if self.is_rented
            else "Có sẵn"
        )

        return (
            f"\nID: {self.comic_id}"
            f"\nTên: {self.title}"
            f"\nTác giả: {self.author}"
            f"\nThể loại: {self.genre}"
            f"\nGiá bán: {self.price}"
            f"\nGiá thuê: {self.rental_price}"
            f"\nTrưng bày: {self.quantity}"
            f"\nTrong kho: {self.stock_quantity}"
            f"\nTrạng thái: {status}"
        )