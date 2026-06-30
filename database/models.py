from datetime import datetime
from database.db import db


class API(db.Model):

    __tablename__ = "apis"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    url = db.Column(db.String(500), nullable=False)

    method = db.Column(db.String(10), default="GET")

    interval = db.Column(db.Integer, default=30)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    metrics = db.relationship(
        "Metric",
        backref="api",
        lazy=True,
        cascade="all, delete"
    )


class Metric(db.Model):

    __tablename__ = "metrics"

    id = db.Column(db.Integer, primary_key=True)

    api_id = db.Column(
        db.Integer,
        db.ForeignKey("apis.id"),
        nullable=False
    )

    status_code = db.Column(db.Integer)

    response_time = db.Column(db.Float)

    success = db.Column(db.Boolean)

    error_message = db.Column(db.Text)

    checked_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )