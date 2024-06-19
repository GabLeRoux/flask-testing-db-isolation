from flask import Blueprint, jsonify

from .models import User

# Utilisation de Blueprint pour mieux organiser les routes
bp = Blueprint("main", __name__)


@bp.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([user.username for user in users])


def init_app(app):
    app.register_blueprint(bp)
