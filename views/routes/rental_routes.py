from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for
)

from services.rental_service import (
    RentalService
)

rental_bp = Blueprint(
    "rental",
    __name__
)

rental_service = RentalService()


# =========================
# PAGE
# =========================
@rental_bp.route("/rentals")
def rentals():

    rentals = (
        rental_service.get_all_rentals()
    )

    return render_template(
        "rentals.html",
        rentals=rentals
    )


# =========================
# RENT
# =========================
@rental_bp.route(
    "/rentals/add",
    methods=["POST"]
)
def add_rental():

    rental_service.rent_comic(
        request.form["customer_id"],
        request.form["comic_id"]
    )

    return redirect(
        url_for("rental.rentals")
    )


# =========================
# RETURN
# =========================
@rental_bp.route(
    "/rentals/return/<rental_id>"
)
def return_rental(rental_id):

    rental_service.return_comic(
        int(rental_id)
    )

    return redirect(
        url_for("rental.rentals")
    )