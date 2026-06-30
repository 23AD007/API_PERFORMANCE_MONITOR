from flask import Blueprint, request, jsonify
from database.db import db
from database.models import API

api_bp = Blueprint("api_bp", __name__)


@api_bp.route("/apis", methods=["GET"])
def get_apis():
    apis = API.query.all()

    data = []

    for api in apis:
        data.append({
            "id": api.id,
            "name": api.name,
            "url": api.url,
            "method": api.method,
            "interval": api.interval,
            "created_at": api.created_at.strftime("%Y-%m-%d %H:%M:%S")
        })

    return jsonify(data), 200


@api_bp.route("/apis", methods=["POST"])
def add_api():

    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    if "name" not in data or "url" not in data:
        return jsonify({"error": "Name and URL are required"}), 400

    api = API(
        name=data["name"],
        url=data["url"],
        method=data.get("method", "GET"),
        interval=data.get("interval", 30)
    )

    db.session.add(api)
    db.session.commit()

    return jsonify({
        "message": "API added successfully",
        "id": api.id
    }), 201


@api_bp.route("/apis/<int:api_id>", methods=["PUT"])
def update_api(api_id):

    api = API.query.get(api_id)

    if not api:
        return jsonify({"error": "API not found"}), 404

    data = request.get_json()

    api.name = data.get("name", api.name)
    api.url = data.get("url", api.url)
    api.method = data.get("method", api.method)
    api.interval = data.get("interval", api.interval)

    db.session.commit()

    return jsonify({
        "message": "API updated successfully"
    })


@api_bp.route("/apis/<int:api_id>", methods=["DELETE"])
def delete_api(api_id):

    api = API.query.get(api_id)

    if not api:
        return jsonify({"error": "API not found"}), 404

    db.session.delete(api)
    db.session.commit()

    return jsonify({
        "message": "API deleted successfully"
    })