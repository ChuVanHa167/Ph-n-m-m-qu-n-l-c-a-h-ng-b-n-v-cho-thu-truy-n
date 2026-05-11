from flask import Flask
from flask import render_template

from config.database import Database

from views.routes.comic_routes import (
    comic_routes
)

from views.routes.customer_routes import (
    customer_bp
)

from views.routes.inventory_routes import (
    inventory_bp
)

from views.routes.rental_routes import (
    rental_bp
)

from views.routes.sale_routes import (
    sale_bp
)

app = Flask(
    __name__,
    template_folder="views/templates",
    static_folder="views/static"
)

db = Database()
db.create_tables()

app.register_blueprint(comic_routes)
app.register_blueprint(customer_bp)
app.register_blueprint(inventory_bp)
app.register_blueprint(rental_bp)
app.register_blueprint(sale_bp)


@app.route("/")
def dashboard():
    return render_template(
        "dashboard.html"
    )


if __name__ == "__main__":
    app.run(debug=True)