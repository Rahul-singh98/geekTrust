class InvalidDateException(Exception):
    """Exception raised when an invalid date is encountered.

    This exception is raised when a date is found to be in an invalid format or does not comply with the expected criteria.
    """


class SubscriptionNotFoundException(Exception):
    """Exception raised when a subscription is not found.

    This exception is raised when a subscription is expected to exist but cannot be found.
    """


class DuplicateSubscriptionException(Exception):
    """Exception raised when a duplicate subscription is detected.

    This exception is raised when an attempt is made to create a duplicate subscription that already exists.
    """


class DuplicateTopUpException(Exception):
    """Exception raised when a duplicate top-up transaction is detected.

    This exception is raised when an attempt is made to create a duplicate top-up transaction that has already been processed.
    """
