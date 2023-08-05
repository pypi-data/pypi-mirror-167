from flask import Blueprint, request

from colocarte_api import db, validation

blueprint = Blueprint("coloc", __name__, url_prefix="/coloc")


class Coloc(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    address = db.Column(db.String(255), nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lon = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Coloc {self.name}>"


def validate(json):
    try:
        name, address, lat, lon = validation.dict(
            json, keys=["name", "address", "lat", "lon"]
        )
        return Coloc(
            name=validation.str(name),
            address=validation.str(address),
            lat=validation.float(lat),
            lon=validation.float(lon),
        )
    except validation.Error as exn:
        return exn


@blueprint.route("/create", methods=("POST",))
def create_view():
    coloc = validate(request.json)
    if isinstance(coloc, validation.Error):
        return f"Error: {coloc.explain()}", 400
    else:
        db.session.add(coloc)
        db.session.commit()
        return "", 204  # No Content (all went well)


@blueprint.route("/list", methods=("GET",))
def list_view():
    return [
        {"name": coloc.name, "address": coloc.address, "coords": [coloc.lat, coloc.lon]}
        for coloc in Coloc.query.all()
    ]
