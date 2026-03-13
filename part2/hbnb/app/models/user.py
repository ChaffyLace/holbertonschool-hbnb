import re
from app.models.base import BaseModel
from app import bcrypt

class User(BaseModel):
    def __init__(self, first_name, last_name, email, password, is_admin=False):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.password = self.hash_password(password)
        self.places = []
        self.reviews = []

    @staticmethod
    def hash_password(password):
        return bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not value or len(value) > 50:
            raise ValueError("First name is required and must be max 50 characters.")
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not value or len(value) > 50:
            raise ValueError("Last name is required and must be max 50 characters.")
        self._last_name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+$'
        if not value or not re.match(email_regex, value):
            raise ValueError("Invalid email format.")
        self._email = value