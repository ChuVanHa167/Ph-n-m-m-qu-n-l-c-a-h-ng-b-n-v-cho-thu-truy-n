from config.database import Database
from models.customer import Customer


class CustomerRepository:

    def __init__(self):

        self.db = Database()

    # =========================
    # CREATE
    # =========================
    def add(self, customer):

        query = """
            INSERT INTO customers (
                customer_id,
                name,
                phone,
                email,
                address
            )
            VALUES (?, ?, ?, ?, ?)
        """

        self.db.cursor.execute(
            query,
            (
                customer.customer_id,
                customer.name,
                customer.phone,
                customer.email,
                customer.address
            )
        )

        self.db.connection.commit()

    # =========================
    # READ ALL
    # =========================
    def get_all(self):

        query = "SELECT * FROM customers"

        self.db.cursor.execute(query)

        rows = self.db.cursor.fetchall()

        customers = []

        for row in rows:

            customer = Customer(
                row["customer_id"],
                row["name"],
                row["phone"],
                row["email"],
                row["address"]
            )

            customers.append(customer)

        return customers

    # =========================
    # FIND BY ID
    # =========================
    def find_by_id(self, customer_id):

        query = """
            SELECT * FROM customers
            WHERE customer_id = ?
        """

        self.db.cursor.execute(
            query,
            (customer_id,)
        )

        row = self.db.cursor.fetchone()

        if row:

            return Customer(
                row["customer_id"],
                row["name"],
                row["phone"],
                row["email"],
                row["address"]
            )

        return None

    # =========================
    # UPDATE
    # =========================
    def update(self, customer):

        query = """
            UPDATE customers
            SET
                name = ?,
                phone = ?,
                email = ?,
                address = ?
            WHERE customer_id = ?
        """

        self.db.cursor.execute(
            query,
            (
                customer.name,
                customer.phone,
                customer.email,
                customer.address,
                customer.customer_id
            )
        )

        self.db.connection.commit()

    # =========================
    # DELETE
    # =========================
    def delete(self, customer_id):

        query = """
            DELETE FROM customers
            WHERE customer_id = ?
        """

        self.db.cursor.execute(
            query,
            (customer_id,)
        )

        self.db.connection.commit()

    # =========================
    # SEARCH
    # =========================
    def search_by_name(self, keyword):

        query = """
            SELECT * FROM customers
            WHERE name LIKE ?
        """

        self.db.cursor.execute(
            query,
            (f"%{keyword}%",)
        )

        rows = self.db.cursor.fetchall()

        customers = []

        for row in rows:

            customer = Customer(
                row["customer_id"],
                row["name"],
                row["phone"],
                row["email"],
                row["address"]
            )

            customers.append(customer)

        return customers