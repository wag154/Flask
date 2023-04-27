from applications import db
from datetime import datetime


class TvShows(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    category = db.Column(db.String(30), nullable=False)
    
    def __str__(self):
        return self.id