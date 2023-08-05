from flask import Blueprint, request

from colocarte_api import db, validation

blueprint = Blueprint("bon_plan", __name__, url_prefix="/bonplan")


class BonPlan(db.Model):
    osm_id = db.Column(db.BigInteger, primary_key=True)
    comment = db.Column(db.Text, nullable=False)

    def __init__(self, osm_id, comment):
        self.osm_id = osm_id
        self.comment = comment


def validate(json):
    try:
        (comment,) = validation.dict(json, keys=["comment"])
        return validation.str(comment)
    except validation.Error as exn:
        return exn


@blueprint.route("/create_or_update/<int:osm_id>", methods=("PUT",))
def create_or_update_view(osm_id):
    comment = validate(request.json)
    if isinstance(comment, validation.Error):
        return f"Error: {comment.explain()}", 400

    bon_plan = BonPlan.query.get(osm_id)
    if bon_plan is None:
        db.session.add(BonPlan(osm_id, comment))
        db.session.commit()
        return "", 201  # Created
    else:
        bon_plan.comment = comment
        db.session.commit()
        return "", 204  # No Content (all went well)


@blueprint.route("/delete/<int:osm_id>", methods=("DELETE",))
def delete_view(osm_id):
    bp = BonPlan.query.get_or_404(osm_id)
    db.session.delete(bp)
    db.session.commit()
    return "", 204  # No Content (all went well)


@blueprint.route("/list", methods=("GET",))
def dispatch_request():
    return [{"osm_id": bp.osm_id, "comment": bp.comment} for bp in BonPlan.query.all()]
