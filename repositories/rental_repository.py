from config.database import Database

from models.rental import Rental


class RentalRepository:

    def __init__(self):

        self.db = Database()

    # =========================
    # CREATE RENTAL
    # =========================
    def create_rental(
        self,
        customer_id,
        comic_id,
        total_price
    ):

        query = """
            INSERT INTO rentals (
                customer_id,
                comic_id,
                total_price
            )
            VALUES (?, ?, ?)
        """

        self.db.cursor.execute(
            query,
            (
                customer_id,
                comic_id,
                total_price
            )
        )

        self.db.connection.commit()

    # =========================
    # RETURN COMIC
    # =========================
    def return_comic(
        self,
        rental_id
    ):

        query = """
            UPDATE rentals
            SET
                status = 'Đã trả',

                return_date =
                    CURRENT_TIMESTAMP

            WHERE rental_id = ?
        """

        self.db.cursor.execute(
            query,
            (rental_id,)
        )

        self.db.connection.commit()

    # =========================
    # GET ALL RENTALS
    # =========================
    def get_all(self):

        query = """
            SELECT * FROM rentals
            ORDER BY rental_date DESC
        """

        self.db.cursor.execute(query)

        rows = self.db.cursor.fetchall()

        rentals = []

        for row in rows:

            rental = Rental(
                row["rental_id"],
                row["customer_id"],
                row["comic_id"],
                row["rental_date"],
                row["return_date"],
                row["status"],
                row["total_price"]
            )

            rentals.append(rental)

        return rentals

    # =========================
    # FIND RENTAL
    # =========================
    def find_by_id(
        self,
        rental_id
    ):

        query = """
            SELECT * FROM rentals
            WHERE rental_id = ?
        """

        self.db.cursor.execute(
            query,
            (rental_id,)
        )

        row = self.db.cursor.fetchone()

        if row:

            return Rental(
                row["rental_id"],
                row["customer_id"],
                row["comic_id"],
                row["rental_date"],
                row["return_date"],
                row["status"],
                row["total_price"]
            )

        return None