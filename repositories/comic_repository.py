from config.database import Database
from models.comic import Comic


class ComicRepository:

    def __init__(self):

        self.db = Database()

    # =========================
    # CREATE
    # =========================
    def add(self, comic):

        query = """
            INSERT INTO comics (
                comic_id,
                title,
                author,
                genre,
                price,
                rental_price,
                quantity,
                stock_quantity,
                is_rented
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """

        self.db.cursor.execute(
            query,
            (
                comic.comic_id,
                comic.title,
                comic.author,
                comic.genre,
                comic.price,
                comic.rental_price,
                comic.quantity,
                comic.stock_quantity,
                comic.is_rented
            )
        )

        self.db.connection.commit()

    # =========================
    # READ ALL
    # =========================
    def get_all(self):

        query = "SELECT * FROM comics"

        self.db.cursor.execute(query)

        rows = self.db.cursor.fetchall()

        comics = []

        for row in rows:

            comic = Comic(
                row["comic_id"],
                row["title"],
                row["author"],
                row["genre"],
                row["price"],
                row["rental_price"],
                row["quantity"],
                row["stock_quantity"],
                bool(row["is_rented"])
            )

            comics.append(comic)

        return comics

    # =========================
    # FIND BY ID
    # =========================
    def find_by_id(self, comic_id):

        query = """
            SELECT * FROM comics
            WHERE comic_id = ?
        """

        self.db.cursor.execute(query, (comic_id,))

        row = self.db.cursor.fetchone()

        if row:

            return Comic(
                row["comic_id"],
                row["title"],
                row["author"],
                row["genre"],
                row["price"],
                row["rental_price"],
                row["quantity"],
                row["stock_quantity"],
                bool(row["is_rented"])
            )

        return None

    # =========================
    # UPDATE
    # =========================
    def update(self, comic):

        query = """
            UPDATE comics
            SET
                title = ?,
                author = ?,
                genre = ?,
                price = ?,
                rental_price = ?,
                quantity = ?,
                stock_quantity = ?
            WHERE comic_id = ?
        """

        self.db.cursor.execute(
            query,
            (
                comic.title,
                comic.author,
                comic.genre,
                comic.price,
                comic.rental_price,
                comic.quantity,
                comic.stock_quantity,
                comic.comic_id
            )
        )

        self.db.connection.commit()

    # =========================
    # DELETE
    # =========================
    def delete(self, comic_id):

        query = """
            DELETE FROM comics
            WHERE comic_id = ?
        """

        self.db.cursor.execute(query, (comic_id,))

        self.db.connection.commit()

    # =========================
    # SEARCH
    # =========================
    def search_by_title(self, keyword):

        query = """
            SELECT * FROM comics
            WHERE title LIKE ?
        """

        self.db.cursor.execute(
            query,
            (f"%{keyword}%",)
        )

        rows = self.db.cursor.fetchall()

        comics = []

        for row in rows:

            comic = Comic(
                row["comic_id"],
                row["title"],
                row["author"],
                row["genre"],
                row["price"],
                row["rental_price"],
                row["quantity"],
                row["stock_quantity"],
                bool(row["is_rented"])
            )

            comics.append(comic)

        return comics

    # =========================
    # UPDATE RENTAL STATUS
    # =========================
    def update_rental_status(
        self,
        comic_id,
        status
    ):

        query = """
            UPDATE comics
            SET is_rented = ?
            WHERE comic_id = ?
        """

        self.db.cursor.execute(
            query,
            (status, comic_id)
        )

        self.db.connection.commit()