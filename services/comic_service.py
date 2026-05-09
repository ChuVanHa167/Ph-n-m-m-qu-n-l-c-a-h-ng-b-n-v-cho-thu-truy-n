from repositories.comic_repository import ComicRepository
from factories.comic_factory import ComicFactory


class ComicService:

    def __init__(self):

        self.repository = ComicRepository()

    # CREATE
    def add_comic(
        self,
        comic_id,
        title,
        author,
        genre,
        price,
        rental_price,
        quantity,
        stock_quantity
    ):

        comic = ComicFactory.create_comic(
            comic_id,
            title,
            author,
            genre,
            price,
            rental_price,
            quantity,
            stock_quantity
        )

        self.repository.add(comic)

    # READ
    def get_all_comics(self):
        return self.repository.get_all()

    # UPDATE
    def update_comic(
        self,
        comic_id,
        title,
        author,
        genre,
        price,
        rental_price,
        quantity,
        stock_quantity
    ):

        comic = ComicFactory.create_comic(
            comic_id,
            title,
            author,
            genre,
            price,
            rental_price,
            quantity,
            stock_quantity
        )

        self.repository.update(comic)

    # DELETE
    def delete_comic(self, comic_id):
        self.repository.delete(comic_id)

    # SEARCH
    def search_comic(self, keyword):
        return self.repository.search_by_title(
            keyword
        )