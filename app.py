from flask import Flask, render_template

from config import Config
from database.db import db
from routes.api_routes import api_bp
from scheduler import start_scheduler

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()
    start_scheduler()

app.register_blueprint(api_bp)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)