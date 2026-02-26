from app.models.base import BaseModel
from app.models.place import Place
from app.models.user import User

class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()
        self.text = text
        self.rating = rating
        self.place = place
        self.user = user

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        if not value:
            raise ValueError("Review text is required.")
        self._text = value

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if value is None or not (1 <= value <= 5):
            raise ValueError("Rating must be an integer between 1 and 5.")
        self._rating = value

    @property
    def place(self):
        return self._place
        
    @place.setter
    def place(self, value):
        if not isinstance(value, Place):
             raise ValueError("Place must be a valid Place instance.")
        self._place = value

    @property
    def user(self):
        return self._user
        
    @user.setter
    def user(self, value):
        if not isinstance(value, User):
             raise ValueError("User must be a valid User instance.")
        self._user = value