from django.db import models

from controller.ctrl.database import DB

class UserModel(models.Model):
    __user = ""

    def __init__(self):
        pass

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
        data = dict()
        DB.where({"email": cls.__user})
        user_data = DB.getOneRow('names, country, city, contact, dob, img_url', 'users')
        if len(user_data) != 0:
            for names, country, city, contact, dob, img_ur in user_data:
                data = {
                    "name": names,
                    "country": country,
                    "city": city,
                    "contact": contact,
                    "dob": dob,
                    "image": img_ur
                }
        return data
