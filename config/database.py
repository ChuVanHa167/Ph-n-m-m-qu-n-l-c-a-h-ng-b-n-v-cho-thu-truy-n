import sqlite3


class Database:
    """
    Singleton Database Connection
    """

    _instance = None

    def __new__(cls):

        if cls._instance is None:

            cls._instance = super(Database, cls).__new__(cls)

            cls._instance.connection = sqlite3.connect(
                "database/comic_store.db"
            )

            # Cho phép lấy dữ liệu dạng dictionary
            cls._instance.connection.row_factory = (
                sqlite3.Row
            )
            cls._instance.connection.execute("PRAGMA foreign_keys = ON")
            cls._instance.cursor = (
                cls._instance.connection.cursor()
            )

        return cls._instance

    def create_tables(self):
        """
        Tạo toàn bộ bảng cho hệ thống
        """

        # =========================
        # BẢNG TRUYỆN
        # =========================
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS comics (

                comic_id TEXT PRIMARY KEY,

                title TEXT NOT NULL,

                author TEXT,

                genre TEXT,

                price REAL NOT NULL,

                rental_price REAL NOT NULL,

                quantity INTEGER DEFAULT 0,

                stock_quantity INTEGER DEFAULT 0,

                is_rented INTEGER DEFAULT 0,

                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # =========================
        # BẢNG KHÁCH HÀNG
        # =========================
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers (

                customer_id TEXT PRIMARY KEY,

                name TEXT NOT NULL,

                phone TEXT,

                email TEXT,

                address TEXT,

                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # =========================
        # BẢNG THUÊ TRUYỆN
        # =========================
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS rentals (

                rental_id INTEGER PRIMARY KEY AUTOINCREMENT,

                customer_id TEXT NOT NULL,

                comic_id TEXT NOT NULL,

                rental_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

                return_date TIMESTAMP,

                status TEXT DEFAULT 'ĐANG_THUE',

                total_price REAL,

                FOREIGN KEY (customer_id) REFERENCES customers(customer_id),

                FOREIGN KEY (comic_id) REFERENCES comics(comic_id)
            )
        """)

        # =========================
        # BẢNG BÁN TRUYỆN
        # =========================
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS sales (

                sale_id INTEGER PRIMARY KEY AUTOINCREMENT,

                customer_id TEXT,

                comic_id TEXT NOT NULL,

                quantity INTEGER DEFAULT 1,

                total_price REAL NOT NULL,

                sale_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

                FOREIGN KEY (customer_id) REFERENCES customers(customer_id),

                FOREIGN KEY (comic_id) REFERENCES comics(comic_id)
            )
        """)

        # =========================
        # BẢNG LOG KHO
        # =========================
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS inventory_logs (

                log_id INTEGER PRIMARY KEY AUTOINCREMENT,

                comic_id TEXT NOT NULL,

                action_type TEXT NOT NULL,

                quantity INTEGER NOT NULL,

                before_quantity INTEGER,
                            
                after_quantity INTEGER,
                
                note TEXT,

                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

                FOREIGN KEY (comic_id)
                    REFERENCES comics(comic_id)
            )
        """)

        # =========================
        # BẢNG ADMIN
        # =========================
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS admins (

                admin_id TEXT PRIMARY KEY,

                username TEXT UNIQUE NOT NULL,

                password TEXT NOT NULL,

                role TEXT DEFAULT 'staff'
            )
        """)

        self.connection.commit()

    def close_connection(self):
        """
        Đóng kết nối database
        """

        self.connection.close()