from pycsql.db.pycsql import pycsql
from django.db import models
from django.utils import timezone
from pycsql.core.manager import Password


class Auth(models.Model):
    user_name = ""
    email_error = ""
    is_authenticated = False
    p_hash = ""
    is_staff = 0
    is_superuser = 0

    email = models.CharField(max_length=65, primary_key=True)
    username = models.CharField(max_length=100, null=True)
    is_active = models.IntegerField(null=True, default=1)
    password = models.CharField(max_length=100, null=True)

    def __init__(self):
        super().__init__()



    def save_auth(self):
        self.save()



    def __str__(self):
        return super().__str__()



    @classmethod
    def authenticate(cls, email: str, row_password: str, column: str = ""):
        """

        Args:
            email: The User Email
            password: The user password
        Returns: 
            bool: True if the email exits and the password matches
            :param email:
            :param column:
            :param row_password:
        """
        pycsql.where({column: email})
        user_data = pycsql.getAll('first_name, last_name, is_staff, is_superuser, password', 'auth_user')
        if len(user_data) == 0:
            cls.email_error = "Oops, No account matches the provided login details "
            return
        for first_name, last_name, is_staff, is_superuser, password in user_data:
            cls.user_name = first_name + " " + last_name
            cls.p_hash = password
            cls.is_staff = is_staff
            cls.is_superuser = is_superuser
        if Password.password_verify(row_password, cls.p_hash):
            cls.is_authenticated = True
        return cls.is_authenticated


class FeedBack(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=65)
    side_effects = models.TextField()
    sent_at = models.DateTimeField(default=timezone.now)

    def create_feedback(self):
        self.save()



    def __str__(self):
        return super().__str__()

class VaccinationCards(models.Model):
    card_id = models.AutoField(primary_key=True)
    card_epi = models.CharField(max_length=11)
    card_sn = models.CharField(max_length=8)
    batch_no = models.CharField(max_length=8)
    citizen_nin_id = models.CharField(max_length=15, default='')
    
    
    def save(self):
        self.save()
        
        
        
    def __str__(self):
        return super().__str__()
    