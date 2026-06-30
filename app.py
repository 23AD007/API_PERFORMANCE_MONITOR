from flask import Flask

from config import Config
from database.db import db
from database.models import API, Metric
from routes.api_routes import api_bp

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)


with app.app_context():
    db.create_all()


app.register_blueprint(api_bp)


@app.route("/")
def home():
    return {
        "project": "API Performance Monitor",
        "status": "Running",
        "version": "1.0"
    }


if __name__ == "__main__":
    app.run(debug=True)