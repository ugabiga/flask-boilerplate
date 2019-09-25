from flask import Blueprint, jsonify

root = Blueprint("main", __name__)


@root.route("/")
def index():
    return jsonify({"status": True})
