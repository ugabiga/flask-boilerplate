from flask import Blueprint, jsonify

root = Blueprint("root", __name__)


@root.route("/")
def index():
    return jsonify({"status": True})
