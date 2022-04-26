from django.db import models
from django.db.models.fields import IntegerField

from pycsql.db.pycsql import pycsql
from pycsql.core.manager import Math, String, Date

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save_citizen(self):
        self.save()

    def __str__(self):
        return super().__str__()



    @classmethod
    def get_districts(cls):
        """Get all available districts in Uganda

        Returns:
            tuple: Available districts in the system
        """
        pycsql.orderBy('name')
        return pycsql.getAll("name", cls.__districts)



    @classmethod
    def add_citizen(cls, citizen_data: dict):

        pycsql.insertData(citizen_data, cls.__table)

        return pycsql.affectedRows() > 0




    @classmethod
    def create_citizen_account(cls, citizen_data: dict):

        pycsql.insertData(citizen_data, "auth_user")

        return pycsql.affectedRows() > 0



    @classmethod
    def prepare_citizen_doze(cls, citizen_data: dict):

        pycsql.insertData(citizen_data, "covidvms_covid19vaccination")

        return pycsql.affectedRows() > 0



    @classmethod
    def get_all_citizens(cls):
        columns = "nin_number, sur_name, given_name, nationality, gender, date_of_birth," \
                  "district"

        return pycsql.getAll(columns, cls.__table)
    
    
    
    @classmethod
    def get_citizen_by_id(cls, citizen, is_email=False):
        colum_key = "email" if is_email else "nin_number"
        
        columns = "nin_number, sur_name, given_name, nationality, gender, date_of_birth," \
                  "card_no, phone_number, village, parish, county, sub_county, district, email"
        pycsql.where({colum_key: citizen})
        return pycsql.getOneRow(columns, cls.__table)



    @classmethod
    def citizen_exits(cls, where={}):
            pycsql.where(where)
            return len(pycsql.getAll('sur_name', cls.__table)) > 0



    @classmethod
    def get_citizen_for_first_doze(cls):

        where = {'no_of_dozes': 0}

        join_tables = {
            cls.__table: "nin_number",
            cls.__vaccination_table: "citizen_nin_id"
        }

        columns = "nin_number, sur_name, given_name, nationality, gender, date_of_birth, card_no, expiry_date, " \
                  "village, parish, sub_county, county, district, phone_number, email"

        pycsql.where(where)

        return pycsql.join(columns, join_tables)



    @classmethod
    def get_citizen_for_second_doze(cls):

        where = {'no_of_dozes': 1}

        join_tables = {
            cls.__table: "nin_number",
            cls.__vaccination_table: "citizen_nin_id"
        }

        columns = "nin_number, sur_name, given_name, nationality, gender, date_of_birth, card_no, expiry_date, " \
                  "village, parish, sub_county, county, district, phone_number, email "

        pycsql.where(where)

        return pycsql.join(columns, join_tables)



    @classmethod
    def citizen_for_first_doze(cls, citizen):

        where = {'no_of_dozes': 0, 'citizen_nin_id': citizen}

        join_tables = {
            cls.__table: "nin_number",
            cls.__vaccination_table: "citizen_nin_id"
        }

        columns = "nin_number, sur_name, given_name, nationality, gender, date_of_birth, card_no, expiry_date, " \
                  "phone_number, email, district"

        citizen_data = {}
                
        pycsql.where(where)

        data = pycsql.join(columns, join_tables)

        if pycsql.not_empty(tuple(data)):
            for nin_number, sur_name, given_name, nationality, gender, date_of_birth, card_no, expiry_date, phone_number, email, district in data:
                citizen_data = {
                    "nin": nin_number,"sur_name": sur_name,"given_name": given_name,
                    "nationality": nationality,"sex": gender,"dob": date_of_birth,
                    "card_no": card_no,"expiry_date": expiry_date,"phone": phone_number,
                    "email": email,"district_name": district 
                }
                
        pycsql.where({'name': citizen_data.get('district_name')})
        district = pycsql.getOneValue('dist_id', 'covidvms_ug')
        
        if type(district) is not int:
            dist_id = Math.random_number(0, 999)
            pycsql.insertData({'dist_id': dist_id, 'name': citizen_data.get('district_name')}, 'covidvms_ug')
            district = dist_id
            
        citizen_data.update(district_id = district)
        
        return citizen_data



    @classmethod
    def citizen_for_second_doze(cls, citizen):

        columns = (
            "nin_number, sur_name, given_name, nationality, gender, date_of_birth, card_no, expiry_date, "
            "phone_number, email " + ", taken_at, vaccination_center, vaccine_id, name "
        )


        sql = "SELECT " + columns + " FROM " + cls.__table + " INNER JOIN " + cls.__vaccination_table
        sql += " ON " + cls.__table + ".nin_number = " + cls.__vaccination_table + ".citizen_nin_id"
        sql += " INNER JOIN covidvms_covid19vaccines  ON " + cls.__vaccination_table + ".vaccine_type_id"
        sql += " = covidvms_covid19vaccines.vaccine_id"
        sql += " WHERE " + cls.__vaccination_table + ".no_of_dozes = %s"
        sql += " AND " + cls.__vaccination_table + ".citizen_nin_id = %s"

        citizen_data = {}

        data = pycsql.query(sql, [1, citizen])

        if pycsql.not_empty(data):
            for nin_number, sur_name, given_name, nationality, gender, date_of_birth, card_no, expiry_date, phone_number, email, taken_at, vaccination_center, vaccine_id, name in data:
                citizen_data = {
                    "nin": nin_number,"sur_name": sur_name,"given_name": given_name,
                    "nationality": nationality,"sex": gender,"dob": date_of_birth,
                    "card_no": card_no,"expiry_date": expiry_date,"phone": phone_number,
                    "email": email,"vaccination_center": vaccination_center,
                    "vaccine_id": vaccine_id, "vaccine_name": name,"taken_at": taken_at
                }

        return citizen_data
    
    
    
    @classmethod
    def fully_vaccinated_citizen(cls): 
        
        where = {'no_of_dozes': 2}

        join_tables = {
            cls.__table: "nin_number",
            cls.__vaccination_table: "citizen_nin_id"
        }

        columns = "nin_number, sur_name, given_name, nationality, gender, date_of_birth, card_no, expiry_date, " \
                  "village, parish, sub_county, county, district, phone_number, email "

        pycsql.where(where)

        return pycsql.join(columns, join_tables)
    
    
    
    @classmethod 
    def vaccination_card(cls, citizen):
        
        columns = (
            "nin_number, sur_name, given_name, nationality, gender, date_of_birth, district, sub_county, parish, village, phone_number, taken_at, next_doze_on, vaccination_center, dozes, name, card_epi, card_sn, batch_no"
        )

        sql = "SELECT " + columns + " FROM " + cls.__table + " INNER JOIN " + cls.__vaccination_table
        sql += " ON " + cls.__table + ".nin_number = " + cls.__vaccination_table + ".citizen_nin_id"
        sql += " INNER JOIN covidvms_covid19vaccines  ON " + cls.__vaccination_table + ".vaccine_type_id"
        sql += " = covidvms_covid19vaccines.vaccine_id INNER JOIN covidvms_vaccinationcards ON " + cls.__table + ".nin_number = covidvms_vaccinationcards.citizen_nin_id"
        sql += " WHERE " + cls.__vaccination_table + ".no_of_dozes = %s"
        sql += " AND " + cls.__vaccination_table + ".citizen_nin_id = %s"

        citizen_data = {}

        data = pycsql.query(sql, [2, citizen])

        if pycsql.not_empty(data):
            for nin_number, sur_name, given_name, nationality, gender, date_of_birth, district, sub_county, parish, village, phone_number, taken_at, next_doze_on, vaccination_center, dozes, name, card_epi, card_sn, batch_no in data:
                citizen_data = {
                    "nin": nin_number,
                    "sur_name": sur_name,
                    "given_name": given_name,
                    "nationality": nationality,
                    "sex": gender,
                    "year": String.sub_str(date_of_birth, 0, 4),
                    "district": district,
                    "sub_county": sub_county,
                    "parish": parish,
                    "village": village,
                    "phone": phone_number,
                    "taken_at": taken_at,
                    "next_doze_on": next_doze_on,
                    "vaccination_center": vaccination_center,
                    "dozes": dozes,
                    "vaccine_name": name,
                    "card_epi": card_epi,
                    "card_sn": card_sn,
                    "batch_no": batch_no,
                }
        
        return citizen_data


class Ug(models.Model):
    dist_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'covidvms_ug'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save_ug(self):
        self.save()

    def __str__(self):
        return super().__str__()


class Covid19Vaccines(models.Model):
    vaccine_id = models.CharField(primary_key=True, max_length=8)
    name = models.CharField(max_length=100)
    dozes = models.IntegerField(default=2)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save_vaccines(self):
        self.save()

    def __str__(self):
        return super().__str__()


class Covid19Vaccination(models.Model):
    __districts = "covidvms_ug"
    __vaccination_table = "covidvms_covid19vaccination"

    vaccination_id = models.CharField(max_length=11, primary_key=True)
    citizen_nin = models.ForeignKey(CitizenModel, on_delete=models.SET_NULL, related_name="+", null=True)
    no_of_dozes = models.IntegerField(default=0)
    vaccine_type = models.ForeignKey(Covid19Vaccines, on_delete=models.SET_NULL, related_name="+", null=True)
    taken_at = models.DateTimeField(null=True)
    next_doze_on = models.DateTimeField(null=True)
    doze_status = models.CharField(max_length=20, default="PARTIAL")
    vaccination_center = models.CharField(max_length=50, default="Mulago")
    vaccination_district = models.ForeignKey(Ug, on_delete=models.SET_NULL, related_name="district_id", null=True,
                                             default=50)

    class Meta:
        managed = True
        db_table = 'covidvms_covid19vaccination'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save_vaccination(self):
        self.save()

    def __str__(self):
        return super().__str__()



    @classmethod
    def vaccinate_citizen(cls, data: dict, nin_id):
        pycsql.where({'citizen_nin_id': nin_id})

        pycsql.update(data, "covidvms_covid19vaccination")

        return pycsql.affectedRows() > 0

    
    
    @classmethod
    def  create_vaccination_card(cls, data:dict):
        pycsql.insertData(data, 'covidvms_vaccinationcards');
        return pycsql.affectedRows() > 0
        
        
        
    @classmethod
    def district_partial_graph(cls):
        where = {'no_of_dozes': 1}

        join_tables = {
            cls.__districts: "dist_id",
            cls.__vaccination_table: "vaccination_district_id"
        }

        columns = "vaccination_id, no_of_dozes, doze_status, citizen_nin_id, vaccination_center, " \
                  "vaccination_district_id, dist_id, name "
        pycsql.where(where)

        return pycsql.join(columns, join_tables)


class Vaccination_centers(models.Model):
    center_id = models.AutoField(primary_key=True)
    center_name = models.CharField(max_length=100)

    def __init_(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return super().__str__()

    class Meta:
        ordering = ('center_name',)

