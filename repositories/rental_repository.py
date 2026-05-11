from config.database import (
    ThreadSafeDatabase
)

from models.rental import Rental


class RentalRepository:

    def __init__(self):

        # self.db = Database()
        self.connection = (
            ThreadSafeDatabase
            .get_thread_connection()
        )

        self.cursor = (
            ThreadSafeDatabase
            .get_thread_cursor()
        )

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

        self.cursor.execute(
            query,
            (
                customer_id,
                comic_id,
                total_price
            )
        )

        self.connection.commit()

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
                status = 'DA_TRA',

                return_date =
                    CURRENT_TIMESTAMP

            WHERE rental_id = ?
        """

        self.cursor.execute(
            query,
            (rental_id,)
        )

        self.connection.commit()

    # =========================
    # GET ALL RENTALS
    # =========================
    def get_all(self):

        query = """
            SELECT * FROM rentals
            ORDER BY rental_date DESC
        """

        self.cursor.execute(query)

        rows = self.cursor.fetchall()

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

        self.cursor.execute(
            query,
            (rental_id,)
        )

        row = self.cursor.fetchone()

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