from django.db import models

from pycsql.db.pycsql import pycsql

from django.core.exceptions import ValidationError

from django.core.validators import validate_email


class UserModel(models.Model):
    __user = ""

    email = models.CharField(max_length=65, primary_key=True)
    names = models.CharField(max_length=65)
    password = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255)
    account_type = models.IntegerField(default=0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save_user(self):
        self.save()

    def __str__(self):
        return super().__str__()

    @classmethod
    def set_current_user(cls, user):
        cls.__user = user

    @classmethod
    def get_current_user(cls):
        """
        Call set_current_user() method first
        :return: The email of the logged in user
        """
        return cls.__user

    @classmethod
    def userdata(cls):
        """
        Call set_current_user() method first and pass the session email
        :return: dict A dictionary of data for the current user
        """
        data = {}
        column_key = "email"

        try:
            validate_email(cls.__user)
        except ValidationError as e:
            column_key = "username"

        pycsql.where({column_key: cls.__user})
        user_data = pycsql.getOneRow('first_name, last_name', 'auth_user')
        if len(user_data) != 0:
            for first_name, last_name in user_data:
                data = {
                    "fname": first_name,
                    "lname": last_name
                }
        return data
