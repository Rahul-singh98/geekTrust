from datetime import datetime
from dateutil.relativedelta import relativedelta
from src.utils.constants import (
    DATE_FORMAT,
    RENEWAL_REMINDER_BEFORE_SUBSCRIPTION_EXPIRE_IN_DAYS,
)


def validate_date(date_string: str) -> bool:
    """Validates if a given date string is in the specified date format.

    Args:
        date_string (str): A string representing a date.

    Returns:
        bool: True if the date string is in the specified format, False otherwise.

    Examples:
        >>> validate_date('')
        False

        >>> validate_date('06-24-2023')
        False

        >>> validate_date('24/06/2023')
        False

        >>> validate_date('24-06-2023')
        True
    """
    try:
        datetime.strptime(date_string, DATE_FORMAT)
        return True
    except ValueError:
        return False


def get_renewal_reminder_date(date_string: str, timedelta_in_months: int) -> str:
    """Calculates the renewal reminder date based on the given date string and time delta in months.

    Args:
        date_string (str): A string representing a date.
        timedelta_in_months (int): Number of months to add to the given date.

    Returns:
        str: The renewal reminder date in the specified date format, or an empty string if an error occurs.

    Examples:
        >>> get_renewal_reminder_date('', 0)

        >>> get_renewal_reminder_date('24-06-2023', 3)
        14-09-2023
    """
    try:
        date_obj = datetime.strptime(date_string, DATE_FORMAT).date()
        expiry_date = date_obj \
            + relativedelta(months=timedelta_in_months) \
            - relativedelta(days=RENEWAL_REMINDER_BEFORE_SUBSCRIPTION_EXPIRE_IN_DAYS)

        return expiry_date.strftime(DATE_FORMAT)
    except ValueError:
        return ""
