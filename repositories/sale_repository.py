from config.database import Database

from models.sale import Sale


class SaleRepository:

    def __init__(self):

        self.db = Database()

    # =========================
    # CREATE SALE
    # =========================
    def create_sale(
        self,
        customer_id,
        comic_id,
        quantity,
        total_price
    ):

        query = """
            INSERT INTO sales (
                customer_id,
                comic_id,
                quantity,
                total_price
            )
            VALUES (?, ?, ?, ?)
        """

        self.db.cursor.execute(
            query,
            (
                customer_id,
                comic_id,
                quantity,
                total_price
            )
        )

        self.db.connection.commit()

    # =========================
    # GET ALL SALES
    # =========================
    def get_all(self):

        query = """
            SELECT * FROM sales
            ORDER BY sale_date DESC
        """

        self.db.cursor.execute(query)

        rows = self.db.cursor.fetchall()

        sales = []

        for row in rows:

            sale = Sale(
                row["sale_id"],
                row["customer_id"],
                row["comic_id"],
                row["quantity"],
                row["total_price"],
                row["sale_date"]
            )

            sales.append(sale)

        return sales

    # =========================
    # TOTAL REVENUE
    # =========================
    def get_total_revenue(self):

        query = """
            SELECT SUM(total_price)
            AS revenue
            FROM sales
        """

        self.db.cursor.execute(query)

        row = self.db.cursor.fetchone()

        if row["revenue"] is None:
            return 0

        return row["revenue"]