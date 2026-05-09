from config.database import Database
from views.main_view import MainView


def main():

    db = Database()
    db.create_tables()

    MainView()


if __name__ == "__main__":
    main()