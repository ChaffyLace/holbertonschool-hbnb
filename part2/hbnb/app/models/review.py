from app import db
from app.models.base import BaseModel

class Review(BaseModel):
    __tablename__ = 'reviews'

    text = db.Column(db.String(1000), nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def __init__(self, text, rating, **kwargs):
        super().__init__(**kwargs)
        self.validate_review(text, rating)
        self.text = text
        self.rating = rating

    def validate_review(self, text, rating):
        if not text:
            raise ValueError("Review text is required.")
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5.")
