import random
import datetime
import platform
import math
import os
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
import re
from controller.ctrl.database import DB


class System:
    __portal = False

    def __init__(self):
        self.__portal = True

    @classmethod
    def os(cls) -> str:
        """

        :return: The name of the operating system eg Windows
        """
        return platform.system()


class Math:
    PI: float
    """
    :var PI
    :returns The mathematical pi
    """

    def __int__(self):
        self.PI = math.pi

    @classmethod
    def round_up(cls, num: float):
        """
        The method rounds a decimal up eg 2.5 becomes 3
        :param num: The number to round off
        :return: int
        """
        return math.ceil(num)

    @classmethod
    def round_down(cls, num: float):
        """
        The method rounds a decimal down eg 2.5 becomes 2
        :param num: The number to round off
        :return: int
        """
        return math.floor(num)

    @classmethod
    def square_root(cls, num: int):
        """

        :param num: The number to find its square root
        :raises Exception If none digit values are parsed
        :return: int The square root of the supplied number
        """
        if type(num) is not int or type(num) is not float:
            raise Exception("Expected a whole or decimal number")
        return math.sqrt(num)

    @classmethod
    def max_value(cls, sequence):
        """

        :param sequence: A list of numbers eg [1,2,3,4]
        :return: int The maximum number among the list items
        """
        return max(sequence)

    @classmethod
    def min_value(cls, sequence):
        """

        :param sequence: A list of numbers eg [1,2,3,4]
        :return: int The minimum number among the list items
        """
        return min(sequence)

    @classmethod
    def to_number(cls, num):
        """

        :param num:
        :raises Exception If the number supplied is not a float
        :return: int
        """
        if type(num) is not float:
            raise Exception("Expected a float")
        return int(num)

    @classmethod
    def to_float(cls, num: float) -> float:
        """

        :param num: The Integer to convert into a float
        :raises Exception If the number passed is not a whole number
        :return: Float
        """
        if type(num) is not int:
            raise Exception("Expected a whole number")
        return float(num)

    @classmethod
    def random_number(cls, minvalue, maxvalue):
        """

        :param minvalue: The start value when generating the random number
        :param maxvalue: The end value when generating the random number
        :return: int random number
        """
        return random.randrange(minvalue, maxvalue)


class File:
    open = False

    def __int__(self):
        self.open = True

    @classmethod
    def open(cls, filename):
        """

        :param filename: The name of the file to open for reading
        :return: An opened file
        """
        return open(filename, "r")

    @classmethod
    def get_content(cls, opened_file):
        """

        :param opened_file: The file previously opened for reading
        :return: Content from the file
        """
        return opened_file.read()

    @classmethod
    def readline_by_line(cls, opened_file):
        """

        :param opened_file: The file previously opened for reading
        :return: Content from the file, read line by line until the end of the file
        """
        return opened_file.readline()

    @classmethod
    def close(cls, opened_file):
        """

        :param opened_file: The name of the file to close
        :return: Any
        """
        return opened_file.close()

    @classmethod
    def create(cls, filename):
        """

        :param filename: The name of the file to create.
        :return: TextIO
        """
        return open(filename, 'w')

    @classmethod
    def append(cls, filename):
        """

        :param filename: The file to open in the appending mode
        :return: TextIO
        """
        return open(filename, 'a')

    @classmethod
    def put_content(cls, opened_file, content):
        """

        :param opened_file: The file recently opened for writing or appending content to
        :param content: The content to put in the file
        :return: None
        """
        opened_file.write(content)
        cls.close(opened_file)

    @classmethod
    def trash(cls, filename):
        """

        :param filename: The file to delete
        :return: bool True if the File is successfully deleted
        """
        if os.path.exists(filename):
            if os.remove(filename):
                return True
        else:
            print("Oops, File does not exist")


class Password:
    __hash = False

    def __init__(self):
        self.__hash = True

    @classmethod
    def hash_password(cls, password):
        """

        :param password: The plain password to hash
        :return: str
        """
        return make_password(password)

    @classmethod
    def password_verify(cls, password, password_hash):
        """

        :param password: Plain text password
        :param password_hash: The hash stored in the database
        :return: bool True if the password matches the hash and False otherwise
        """
        return check_password(password, password_hash)


class String:
    __slice = False

    def __init__(self):
        self.__slice = True

    @classmethod
    def slice_str(cls, string: str,
                  pos1: int,
                  pos2: int) -> str:
        """

        :param string: The string to slice
        :param pos1: The index where to start from when slicing the supplied string
        :param pos2: The index where to end from when slicing the supplied string
        :return: str An extracted/sliced string
        """
        return string[pos1:pos2]

    @classmethod
    def to_upper(cls, string: str) -> str:
        """

        :param string: A string to convert to lowercase
        :raises Exception when the string supplied is not lowercase
        :return:
        """
        reg = r"[a-z0-9]"
        if not re.match(reg, string):
            raise Exception('Expected an uppercase string')
        else:
            return string.upper()

    @classmethod
    def to_lower(cls, string):
        """

        :param string: A string to convert to lowercase
        :raises Exception when the string supplied is not uppercase
        :return:
        """
        reg = r"[A-Z0-9]"
        if not re.match(reg, string):
            raise Exception('Expected an uppercase string')
        else:
            return string.lower()

    @classmethod
    def trim(cls, string: str) -> str:
        """

        :param string: A string to remove empty strings
        :return: str A trimed string
        """
        return string.strip()

    @classmethod
    def str_exist(cls, hook, string):
        """

        :param hook: Part of the word in a string to search for
        :param string: The string to check from
        :return: bool True if the part exists and False otherwise
        """
        if hook in string:
            return True
        else:
            return False

    @classmethod
    def validate_email(cls, email: str):
        """

        :param email: The email address to check
        :return: str Email if True and bool False if the email is invalid
        """
        reg = r"^([a-z0-9_.])+@([a-z]){2,}([.])([a-z]){2,}$"
        match = re.match(reg, email)
        if match:
            return email
        else:
            return None

    @classmethod
    def to_string(cls, num) -> str:
        """

        :param num: An Integer to convert to a string
        :return: str
        """
        return str(num)

    @classmethod
    def shuffle(cls, string: str):
        """

        :param string: A string to shuffle
        :return: str A shuffled string
        """
        shuffle = list(string)
        shuffled_str = random.sample(shuffle, len(shuffle))
        return ''.join(shuffled_str)


class Date:
    __construct = False

    def __init__(self):
        self.__construct = True

    @classmethod
    def __c_date(cls) -> datetime:
        return datetime.datetime.now()

    @classmethod
    def year(cls) -> int:
        """
        The Current year eg 2021
        :return: int
        """
        return cls.__c_date().year

    @classmethod
    def date_time(cls) -> datetime:
        """
        The current date and time of the day
        :return: Date and Time
        """
        return cls.__c_date().now()

    @classmethod
    def month(cls) -> int:
        """
        The current month in number eg 3
        :return: int
        """
        return cls.__c_date().month

    @classmethod
    def today(cls) -> int:
        """
        The current date in number eg 14
        day (1-31)
        :return: int
        """
        return cls.__c_date().day

    @classmethod
    def week_day(cls):
        """
        The Current day of the week in number eg 6
        Mon == 0 and Sun == 6
        :return:
        """
        return cls.__c_date().weekday()

    @classmethod
    def str_month(cls, uppercase=False, full_form=False) -> str:
        """

        :param uppercase: Set it to True if you want a month to be returned in uppercase
        :param full_form: Set it to True if you want a month to be returned in full form eg december
        :return: str
        """
        m_in_full = ("January", "February", "March", "April", "May", "June", "July",
                     "August", "September", "November", "December")
        m_in_short = ("Jan", "Feb", "March", "April", "May", "June", "July",
                      "Aug", "Sep", "Nov", "Dec",)
        text = ""
        text = m_in_short[cls.month()]
        if uppercase and not full_form:
            text = String.to_upper(m_in_short[cls.month()])
        if full_form:
            text = m_in_full[cls.month()]
        if uppercase and full_form:
            text = String.to_upper(m_in_full[cls.month()])
        return text

    @classmethod
    def str_day(cls, uppercase=False, full_form=False) -> str:
        """

        :param uppercase: Set it to True if you want the day of the week to be returned in uppercase
        :param full_form: Set it to True if you want the day of the week to be returned in full form eg Monday
        :return: str
        """
        d_in_full = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
        d_in_short = ("Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun")
        text = ""
        text = d_in_short[cls.week_day()]
        if uppercase and not full_form:
            get_txt = d_in_short[cls.week_day()]
            txt = get_txt.lower()
            text = String.to_upper(txt)
        if full_form:
            text = d_in_full[cls.week_day()]
        if uppercase and full_form:
            get_txt = d_in_full[cls.week_day()]
            txt = get_txt.lower()
            text = String.to_upper(txt)
        return text


class NIN:
    __is_unique = False

    def __init__(self):
        self.__is_unique = True

    @staticmethod
    def generate():
        """
        Generates a Ugandan NIN (National Identification Number)
        :return: str NIN
        """
        num = Math.random_number(0, 10000000)
        string = String.shuffle("ABCDEFGHIJKLMNOPQRSTVWXYZ")
        sh_str = String.slice_str(string, 3, 7)
        return "CM" + String.to_string(num) + sh_str

    @classmethod
    def validate(cls, nin: str):
        """

        :param nin: The NIN to check if it has a correct format
        :return: bool True if the number is in a correct format and False otherwise
        """
        reg = r"([A-Z]){2}([0-9]){8}([A-Z]){4}"
        if re.match(reg, nin):
            return True
        else:
            return False
