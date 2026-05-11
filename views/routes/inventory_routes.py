from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for
)

from services.inventory_service import (
    InventoryService
)

inventory_bp = Blueprint(
    "inventory",
    __name__
)

inventory_service = InventoryService()


# =========================
# PAGE
# =========================
@inventory_bp.route("/inventory")
def inventory():

    logs = (
        inventory_service.get_inventory_logs()
    )

    return render_template(
        "inventory.html",
        logs=logs
    )


# =========================
# IMPORT
# =========================
@inventory_bp.route(
    "/inventory/import",
    methods=["POST"]
)
def import_inventory():

    inventory_service.import_comic_stock(
        request.form["comic_id"],
        int(request.form["quantity"])
    )

    return redirect(
        url_for("inventory.inventory")
    )


# =========================
# EXPORT
# =========================
@inventory_bp.route(
    "/inventory/export",
    methods=["POST"]
)
def export_inventory():

    inventory_service.export_comic_stock(
        request.form["comic_id"],
        int(request.form["quantity"])
    )

    return redirect(
        url_for("inventory.inventory")
    )


# =========================
# MOVE TO SHELF
# =========================
@inventory_bp.route(
    "/inventory/move",
    methods=["POST"]
)
def move_inventory():

    inventory_service.move_comic_to_display(
        request.form["comic_id"],
        int(request.form["quantity"])
    )

    return redirect(
        url_for("inventory.inventory")
    )