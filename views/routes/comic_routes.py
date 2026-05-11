from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for
)

from services.comic_service import (
    ComicService
)

comic_routes = Blueprint(
    "comic_routes",
    __name__
)

comic_bp = comic_routes

comic_service = ComicService()


# =========================
# AUTO ID
# =========================
def generate_next_id():

    comics = comic_service.get_all_comics()

    if not comics:
        return "1"

    max_id = max(
        int(c.comic_id)
        for c in comics
        if str(c.comic_id).isdigit()
    )

    return str(max_id + 1)


# =========================
# HIỂN THỊ
# =========================
@comic_routes.route("/comics")
def comics():

    keyword = request.args.get(
        "keyword",
        ""
    )

    if keyword:

        comics = (
            comic_service.search_comic(
                keyword
            )
        )

    else:

        comics = (
            comic_service.get_all_comics()
        )

    next_id = generate_next_id()

    return render_template(
        "comics.html",
        comics=comics,
        next_id=next_id
    )


# =========================
# THÊM
# =========================
@comic_routes.route(
    "/comics/add",
    methods=["POST"]
)
def add_comic():

    comic_service.add_comic(
        request.form["comic_id"],
        request.form["title"],
        request.form["author"],
        request.form["genre"],
        float(request.form["price"]),
        float(request.form["rental_price"]),
        int(request.form["quantity"]),
        int(request.form["stock_quantity"])
    )

    return redirect(
        url_for("comic_routes.comics")
    )


# =========================
# UPDATE
# =========================
@comic_routes.route(
    "/comics/update",
    methods=["POST"]
)
def update_comic():

    comic_service.update_comic(
        request.form["comic_id"],
        request.form["title"],
        request.form["author"],
        request.form["genre"],
        float(request.form["price"]),
        float(request.form["rental_price"]),
        int(request.form["quantity"]),
        int(request.form["stock_quantity"])
    )

    return redirect(
        url_for("comic_routes.comics")
    )


# =========================
# DELETE
# =========================
@comic_routes.route(
    "/comics/delete/<comic_id>"
)
def delete_comic(comic_id):

    comic_service.delete_comic(
        comic_id
    )

    return redirect(
        url_for("comic_routes.comics")
    )