import random
from datetime import datetime, date
import platform
import math
import os
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
import re


class System:

    def __init__(self):
        pass

    @classmethod
    def os(cls):
        """
        Get the current operating system

        Returns:
            str: The name of the operating system eg Windows
        """
        return platform.system()


class Math:
    PI: float

    def __init__(self):
        self.PI = math.pi

    @classmethod
    def round_up(cls, num: float):
        """
        The method rounds a decimal up eg 2.5 becomes 3

        Args:
            num (float): The number to round off
        Returns:
            int
        """
        return math.ceil(num)

    @classmethod
    def round_down(cls, num: float):
        """
        The method rounds a decimal down eg 2.5 becomes 2

        Args:
            num (float): The number to round off
        Return:
            int
        """
        return math.floor(num)

    @classmethod
    def square_root(cls, num):
        """
        Get the squarer root of a number

        Args:
            num (int, float, decimal): The number to find its square root
        Returns:
            The square root of the supplied number
        """
        return math.sqrt(num)

    @classmethod
    def max_value(cls, sequence):
        """
        Get the maximum value from a sequence

        Args:
            sequence (list): A list of numbers eg [1,2,3,4]
        :Returns:
            int: The maximum number among the list items
        """
        return max(sequence)

    @classmethod
    def min_value(cls, sequence):
        """
        Get the minimum value from a sequence

        Args:
            sequence (list): A list of numbers eg [1,2,3,4]
        :Returns:
            int: The minimum number among the list items
        """
        return min(sequence)

    @classmethod
    def to_number(cls, num):
        """
        Convert to integer

        Args:
            num (float, decimal):
        Raises:
            Exception: If the number supplied is not a float
        Returns:
            int
        """
        if type(num) is not float:
            raise Exception("Expected a float")
        return int(num)

    @classmethod
    def to_float(cls, num: float):
        """
        Convert an integer to a float

        Args:
            num (int): The Integer to convert into a float
        Raises:
            Exception: If the number passed is not a whole number
        Returns:
            Float
        """
        if type(num) is not int:
            raise Exception("Expected a whole number")
        return float(num)

    @classmethod
    def random_number(cls, minvalue, maxvalue):
        """
        Get a random number between the min and max values supplied

        Args:
            minvalue (int): The start value when generating the random number
            maxvalue (int): The end value when generating the random number
        Returns:
            int: random number
        """
        return random.randrange(minvalue, maxvalue)


class File:

    def __init__(self):
        pass

    @classmethod
    def open(cls, filename):
        """
        Open a file for reading

        Args:
            filename (str): The name of the file to open for reading
        Returns:
            An opened file
        """
        return open(filename, "r")

    @classmethod
    def get_content(cls, opened_file):
        """
        Read content from a file

        Args:
            opened_file: The file previously opened for reading (with open())
        Return:
            str: Content from the file
        """
        return opened_file.read()

    @classmethod
    def readline_by_line(cls, opened_file):
        """
        Get content from a file, line by line

        Args:
            opened_file: The file previously opened for reading
        Returns:
            Content from the file, read line by line until the end of the file
        """
        return opened_file.readline()

    @classmethod
    def close(cls, opened_file):
        """
        Close the opened file

        Args:
            opened_file: The name of the file to close
        Returns:
            None
        """
        return opened_file.close()

    @classmethod
    def create(cls, filename):
        """
        Create a file for writing

        Args:
            filename: The name of the file to create.
        Returns:
            TextIO
        """
        return open(filename, 'w')

    @classmethod
    def append(cls, filename):
        """
        Open a file for appending content at the end

        Arg: 
            filename: The file to open in the appending mode
        Return:
            TextIO
        """
        return open(filename, 'a')

    @classmethod
    def put_content(cls, opened_file, content):
        """
        Write content in a file

        Args:
            opened_file: The file recently opened for writing or appending content to
            content: The content to put in the file
        Returns:
            None
        """
        opened_file.write(content)
        cls.close(opened_file)

    @classmethod
    def trash(cls, filename):
        """
        Move the file to trash bin

        Args:
            filename: The file to delete
        Returns:
            bool: True if the File is successfully deleted

        Does not delete permanently
        """
        if os.path.exists(filename):
            if os.remove(filename):
                return True
        else:
            print("Oops, File does not exist")


class Password:

    def __init__(self):
        pass

    @classmethod
    def hash_password(cls, password):
        """
        Encrypt a row password using pbkdf_256
        Args:
            password (str): The plain password to hash
        Returns:
            str: hashed password
        """
        return make_password(password)

    @classmethod
    def password_verify(cls, password, password_hash):
        """
        Verify a password

        Args:
            password (str): Plain text password
            password_hash: The hash of the password (commonly stored in the database)
        Returns:
            bool: True if the password matches the hash and False otherwise
        """
        return check_password(password, password_hash)


class String:

    def __init__(self):
        pass

    @classmethod
    def sub_str(cls, string: str,
                pos1: int,
                pos2: int):
        """
        Get a sub copy of a string

        Args:
            string (str): The string to slice
            pos1 (int): The index where to start from when slicing the supplied string
            pos2 (int): The index where to end from when slicing the supplied string
        Returns:
            str: An extracted/sliced string
        """
        return "{}".format(string)[pos1:pos2]

    @classmethod
    def to_upper(cls, string: str):
        """
        Return a converted string to uppercase

        Args:
            string (str): A string to convert to lowercase
        Returns:
            str: Uppercase string
        """
        return "{}".format(string).upper()

    @classmethod
    def to_lower(cls, string):
        """
        Return a converted string to lowercase

        Args:
            string (str): A string to convert to lowercase
        Returns:
            str: Lowercase string
        """
        return "{}".format(string).lower()

    @classmethod
    def trim(cls, string: str):
        """
        Return a copy of the string with leading and trailing whitespace removed

        Args:
            string (str): A string to remove empty strings
        Returns:
            str: A trimmed string
        """
        return "{}".format(string).strip()

    @classmethod
    def str_exist(cls, hook, string):
        """

        :param hook: Part of the word in a string to search for
        :param string: The string to check from
        :return: bool True if the part exists and False otherwise
        """
        return hook in string

    @classmethod
    def validate_email(cls, email: str):
        """
        Validate an email address

        Args:
            email (str): The email address to check
        Returns:
            str: Email if True and bool False if the email is invalid
        """
        reg = r"^([a-z0-9_.])+@([a-z]){2,}([.])([a-z]){2,}$"
        return re.match(reg, email)

    @classmethod
    def to_string(cls, num):
        """
        Convert to a string object

        Args:
            num (any): An Integer to convert to a string
        Returns:
            str
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

    @classmethod
    def replace(cls, oldvalue: str, newvalue: str, subject: str):
        """Replace an occurrence in a string

        Args:
            oldvalue (str): The value to be replace
            newvalue (str): The new value to replace the old value
            subject (str): The full string to act upon

        Returns:
            str: A new string with the new values
        """
        return "{}".format(subject).replace(oldvalue, newvalue)

    @classmethod
    def is_not_empty(cls, values: list):
        """Check empty values.

        Args:
            values (list): A list of variables to check

        Returns:
            bool: True if the values are not empty and False otherwise
        """
        return "" not in values


class Date:

    def __init__(self):
        pass

    @classmethod
    def __c_date(cls) -> datetime:
        return datetime.now()

    @classmethod
    def year(cls):
        """
        The Current year eg 2021
        Returns:
            int
        """
        return cls.__c_date().year

    @classmethod
    def datetime(cls, clock: int = 24):
        """Get the current date and time

        Args:
            clock (int, optional): Clock, either 12 or 24 hour clock. Defaults to 24.

        Returns:
            string: Date and time
        """
        date_format = '%Y-%m-%d %H:%M:%S'
        date_format = '%Y-%m-%d %i:%M:%S%p' if clock == 24 else date_format
        return datetime.today().strftime(date_format)

    @classmethod
    def dbdate(cls, clock: int = 24, hours: bool = True):
        """Get the current date and time

        Args:
            clock (int, optional): Clock, either 12 or 24 hour clock. Defaults to 24.
            :param hours:
            :param clock:
        Returns:
            string: Date and time

        """
        date_format = '%Y-%m-%d %H:%M:%S'
        date_format = '%Y-%m-%d %i:%M:%S%p' if clock == 24 else date_format

        if not hours:
            date_format = '%Y-%m-%d'
        return datetime.today().strftime(date_format)

    @classmethod
    def month(cls):
        """
        The current month in number eg 3
        Returns:
            int
        """
        return cls.__c_date().month

    @classmethod
    def today(cls):
        """
        The current date in number eg 14
        day (1-31)
        Returns:
            int
        """
        return cls.__c_date().day

    @classmethod
    def week_day(cls):
        """
        The Current day of the week in number eg 6
        Mon == 0 and Sun == 6
        """
        return cls.__c_date().weekday()

    @classmethod
    def str_month(cls, uppercase=False, full_form=False):
        """
        Get the month in words

        Args:
            uppercase (bool): Set it to True if you want a month to be returned in uppercase
            full_form (bool): Set it to True if you want a month to be returned in full form eg december
        Returns:
            str: String Month
        """
        m_in_full = ("January", "February", "March", "April", "May", "June", "July",
                     "August", "September", "November", "December")
        m_in_short = ("Jan", "Feb", "March", "April", "May", "June", "July",
                      "Aug", "Sep", "Nov", "Dec",)
        text = m_in_short[cls.month()]
        if uppercase and not full_form:
            text = String.to_upper(m_in_short[cls.month()])
        if full_form:
            text = m_in_full[cls.month()]
        if uppercase and full_form:
            text = String.to_upper(m_in_full[cls.month()])
        return text

    @classmethod
    def str_day(cls, uppercase=False, full_form=False):
        """
        Get the day of the week

        Args:
            uppercase (bool): Set it to True if you want the day of the week to be returned in uppercase
            full_form (bool): Set it to True if you want the day of the week to be returned in full form eg Monday
        Returns:
            str: String day
        """
        d_in_full = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
        d_in_short = ("Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun")

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

    @classmethod
    def date(cls):
        """Get the current date without time

        Returns:
            str: Date string
        """
        return datetime.now().date()

    @classmethod
    def strtotime(cls, period_in_number=1, period_in_words="days", only_date=False, iso: bool = False):
        """Convert a string to date.

        Args:
            period_in_number (int, optional): The period in numbers. Defaults to 1.
            period_in_words (str, optional): The period in words. Defaults to "days".

            Allowed values (day/days, week/weeks, month/months, year/years)
            only_date (bool, optional): Returns only the date without time. Defaults to False.
            iso (bool, optional): Returns the date in a format of YY-mm-dd/ Y-m-d. Defaults to False.

        Returns:
            date: The formulated date

        Get the date of the next week on today (1 week)
        """
        import datetime
        date_format = datetime.datetime.now()
        if only_date:
            date_format = datetime.datetime.now().date()
        if period_in_words in ["month", "months"]:
            weeks = period_in_number * 4
            period_in_number = weeks * 7

        if period_in_words in ["week", "weeks"]:
            period_in_number = period_in_number * 7

        if period_in_words in ["year", "years"]:
            period_in_number = period_in_number * 365

        extract = date_format + datetime.timedelta(days=period_in_number)
        if iso:
            extract = extract.strftime('%Y-%m-%d')
        return extract


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
        sh_str = String.sub_str(string, 3, 7)
        return "CM" + String.to_string(num) + sh_str

    @classmethod
    def validate(cls, nin: str):
        """

        Args:
            nin: The NIN to check if it has a correct format
        Returns: 
            bool: True if the number is in a correct format and False otherwise
        """
        reg = r"(/^(([C])([M])([0-9A-Z]){12})$/"
        return bool(re.match(reg, nin))


class Notify:
    """Access All Notification alerts
    """

    def __init__(self) -> None:
        pass

    @classmethod
    def success(cls, message: str):
        """Success Notification

        Args:
            message (str): The message to send as a notification

        Returns:
            str: success notification
        """
        return "<div class='alert alert-success'><strong><i class='fas fa-check-circle " \
               "text-success'></i></strong> {} <button type='button' class='close' " \
               "data-dismiss='alert'>&times;</button></div>".format(message)

    @classmethod
    def failure(cls, message: str):
        """Failure | Warning Notification

        Args:
            message (str): The message to send as a notification

        Returns:
            str: Failure notification
        """
        return "<div class='alert alert-warning'><strong><i class='fas fa-exclamation-triangle " \
               "text-warning'></i></strong> {} <button type='button' class='close' " \
               "data-dismiss='alert'>&times;</button></div>".format(message)

    @classmethod
    def info(cls, message: str):
        """Info Notification

        Args:
            message (str): The message to send as a notification

        Returns:
            str: Info notification 
        """
        return "<div class='alert alert-info'><strong><i class='fas fa-info-circle text-info'></i></strong> {} " \
               "<button type='button' class='close' data-dismiss='alert'>&times;</button></div>".format(message)

    @classmethod
    def danger(cls, message: str):
        """ Error Notification

        Args:
            message (str): The message to send as an error notification

        Returns:
            str: Error notification
        """
        return "<div class='alert alert-danger'><strong><i class='fas fa-exclamation-triangle " \
               "text-danger'></i></strong> {} <button type='button' class='close' " \
               "data-dismiss='alert'>&times;</button></div>".format(message)
