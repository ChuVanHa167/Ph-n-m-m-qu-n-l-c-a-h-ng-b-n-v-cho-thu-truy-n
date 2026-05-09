from models.comic import Comic

class ComicFactory:

    @staticmethod
    def create_comic(
        comic_id,
        title,
        author,
        genre,
        price,
        rental_price,
        quantity,
        stock_quantity
    ):

        return Comic(
            comic_id,
            title,
            author,
            genre,
            price,
            rental_price,
            quantity,
            stock_quantity
        )