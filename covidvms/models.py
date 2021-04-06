from django.db import models
from controller.ctrl.controller import Password
from controller.ctrl.database import DB


class Auth(models.Model):
    __auth = False
    user_name = ""
    email_error = ""
    is_authenticated = False
    p_hash = ""

    def __init__(self):
        self.__auth = True
        super().__init__()

    @classmethod
    def authenticate(cls, email: str, password: str):
        """

        :param email: The User Email
        :param password: The user password
        :return: bool True if the email exits and the password matches
        """
        DB.where({"email": email})
        user_data = DB.getAll('names, password', 'users')
        if len(user_data) != 0:
            for names, db_hash in user_data:
                cls.user_name = names
                cls.p_hash = db_hash
        else:
            cls.email_error = "Oops, No account matches the provided login details"
        if Password.password_verify(password, cls.p_hash):
            cls.is_authenticated = True
        return cls.is_authenticated

    @classmethod
    def getUser(cls):
        return DB.getAll("username, email", "auth_user")
