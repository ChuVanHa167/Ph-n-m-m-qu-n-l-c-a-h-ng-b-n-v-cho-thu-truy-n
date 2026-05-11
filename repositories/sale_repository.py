from config.database import (
    ThreadSafeDatabase
)

from models.sale import Sale


class SaleRepository:

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

        self.cursor.execute(
            query,
            (
                customer_id,
                comic_id,
                quantity,
                total_price
            )
        )

        self.connection.commit()

    # =========================
    # GET ALL SALES
    # =========================
    def get_all(self):

        query = """
            SELECT * FROM sales
            ORDER BY sale_date DESC
        """

        self.cursor.execute(query)

        rows = self.cursor.fetchall()

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

        self.cursor.execute(query)

        row = self.cursor.fetchone()

        if row["revenue"] is None:
            return 0

        return row["revenue"]
    
    def get_monthly_revenue(self):

        query = """
            SELECT 
                strftime('%Y-%m', sale_date) as month,
                SUM(total_price) as revenue
            FROM sales
            GROUP BY month
            ORDER BY month ASC
        """

        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        result = []
        for row in rows:
            result.append({
                "month": row["month"],
                "revenue": row["revenue"]
            })

        return result