from flask import current_app as app, jsonify

from .models import User


@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.username for user in users])
