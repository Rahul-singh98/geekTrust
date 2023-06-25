from src.dao.doremi_dao import DoremiDao
from src.exceptions.common import (
    DuplicateSubscriptionException, DuplicateTopUpException,
    SubscriptionNotFoundException, InvalidDateException
)
from src.utils.date import validate_date


class SubscriptionValidator:
    """Class responsible for validating subscriptions and top-ups."""

    def __init__(self):
        """Initialize the SubscriptionValidator instance."""
        self.dao = DoremiDao()

    def validate_duplicate_subscription(self, streaming_category):
        """Validate if a duplicate subscription exists for the given streaming category.

        Args:
            streaming_category (str): The streaming category.

        Raises:
            DuplicateSubscriptionException: If a duplicate subscription is found.
        """
        subs = self.dao.get_subscriptions()
        for sub in subs:
            if sub.stream_category.name == streaming_category:
                raise DuplicateSubscriptionException()

    def validate_duplicate_topup(self):
        """Validate if a duplicate top-up exists.

        Raises:
            DuplicateTopUpException: If a duplicate top-up is found.
        """
        if self.dao.top_up:
            raise DuplicateTopUpException()

    def validate_subscription_exists(self):
        """Validate if any subscriptions exist.

        Raises:
            SubscriptionNotFoundException: If no subscriptions are found.
        """
        if len(self.dao.get_subscriptions()) == 0:
            raise SubscriptionNotFoundException()

    def validate_subscription_date(self):
        """Validate the start subscription date.

        Raises:
            InvalidDateException: If the start subscription date is invalid.
        """
        if not validate_date(self.dao.start_subscription):
            raise InvalidDateException
