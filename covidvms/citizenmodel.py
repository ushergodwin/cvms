from django.db import models
from django.db.models.base import Model
from django.db.models.fields import IntegerField
from datetime import date, datetime

from django.utils import timezone

from controller.ctrl.database import DB


class CitizenModel(models.Model):
    __table = "covidvms_citizenmodel"
    __districts = "covidvms_ug"
    __vaccination_table = "covidvms_covid19vaccination"

    nin_number = models.CharField(max_length=15, primary_key=True, default="CM999999999999")
    sur_name = models.CharField(max_length=35)
    given_name = models.CharField(max_length=35)
    nationality = models.CharField(max_length=25)
    gender = models.CharField(max_length=1, default="M")
    date_of_birth = models.DateField()
    card_no = IntegerField()
    expiry_date = models.DateField()
    village = models.CharField(max_length=100)
    parish = models.CharField(max_length=100)
    sub_county = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13)
    email = models.EmailField(max_length=65)

    def __init__(cls, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def save_citizen(self):
        self.save()

    def __str__(self) -> str:
        return super().__str__()

    @classmethod
    def get_districts(cls):
        """Get all available districts in Uganda

        Returns:
            tupple: Available districts in the system
        """
        return DB.getAll("name", cls.__districts)

    @classmethod
    def add_citizen(cls, citizen_data: dict):
        res = False

        DB.insertData(citizen_data, cls.__table)

        res = True if DB.affectedRows() > 0 else res

        return res

    @classmethod
    def create_citizen_account(cls, citizen_data: dict):
        res = False

        DB.insertData(citizen_data, "auth_user")

        res = True if DB.affectedRows() > 0 else res

        return res

    @classmethod
    def prepare_citizen_doze(cls, citizen_data: dict):
        res = False

        DB.insertData(citizen_data, "covidvms_covid19vaccination")

        res = True if DB.affectedRows() > 0 else res

        return res

    @classmethod
    def get_all_citizens(cls):
        columns = "nin_number, sur_name, given_name, nationality, gender, date_of_birth, card_no, expiry_date, village, parish, sub_county, county, district, phone_number, email"

        return DB.getAll(columns, cls.__table)

    @classmethod
    def citizen_exits(cls, where: dict = {}):
        res = False
        try:

            DB.where(where)

            citizen_nin = DB.getOneValue('sur_name', cls.__table)
            res = True if citizen_nin != "" and type(citizen_nin) is not bool else res
        except Exception as e:
            res = e
        return res

    @classmethod
    def get_citizen_for_first_doze(cls):

        where = {'no_of_dozes': 0}

        join_tables = {
            cls.__table: "nin_number",
            cls.__vaccination_table: "citizen_nin_id"
        }

        columns = "nin_number, sur_name, given_name, nationality, gender, date_of_birth, card_no, expiry_date, village, parish, sub_county, county, district, phone_number, email"

        DB.where(where)

        return DB.join(columns, join_tables)

    @classmethod
    def citizen_for_first_doze(cls, citizen):

        where = {'no_of_dozes': 0, 'citizen_nin_id': citizen}

        join_tables = {
            cls.__table: "nin_number",
            cls.__vaccination_table: "citizen_nin_id"
        }

        columns = "nin_number, sur_name, given_name, nationality, gender, date_of_birth, card_no, expiry_date, phone_number, email"

        DB.where(where)

        citizen_data = {}

        data = DB.join(columns, join_tables)

        if DB.not_empty(data):
            for nin_number, sur_name, given_name, nationality, gender, date_of_birth, card_no, expiry_date, phone_number, email in data:
                citizen_data = {
                    "nin": nin_number,
                    "sur_name": sur_name,
                    "given_name": given_name,
                    "nationality": nationality,
                    "sex": gender,
                    "dob": date_of_birth,
                    "card_no": card_no,
                    "expiry_date": expiry_date,
                    "phone": phone_number,
                    "email": email
                }

        return citizen_data


class Covid19Vaccines(models.Model):
    vaccine_id = models.CharField(primary_key=True, max_length=8)
    name = models.CharField(max_length=100)
    dozes = models.IntegerField(default=2)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def save_vaccines(self):
        self.save()

    def __str__(self) -> str:
        return super().__str__()


class Covid19Vaccination(models.Model):
    vaccination_id = models.CharField(max_length=11, primary_key=True)
    citizen_nin = models.ForeignKey(CitizenModel, on_delete=models.SET_NULL, related_name="+", null=True)
    no_of_dozes = models.IntegerField(default=0)
    vaccine_type = models.ForeignKey(Covid19Vaccines, on_delete=models.SET_NULL, related_name="+", null=True)
    taken_at = models.DateTimeField(null=True)
    next_doze_on = models.DateTimeField(null=True)
    doze_status = models.CharField(max_length=20, default="PARTIAL")

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def save_vaccination(self):
        self.save()

    def __str__(self) -> str:
        return super().__str__()


class Ug(models.Model):
    dist_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def __str__(self) -> str:
        return super().__str__()
