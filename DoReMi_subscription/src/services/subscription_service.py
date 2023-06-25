import logging
from src.utils.date import validate_date
from src.exceptions.common import (
    InvalidDateException, DuplicateTopUpException,
    SubscriptionNotFoundException, DuplicateSubscriptionException)
from src.validators.subscription_validator import SubscriptionValidator

from src.dao.doremi_dao import DoremiDao

# Configure logging settings
logging.basicConfig(level=logging.DEBUG, format="%(message)s")


class SubscriptionsService:
    def __init__(self):
        self.dao = DoremiDao()
        self.__validator = SubscriptionValidator()

    def start_subscription(self, date):
        if not validate_date(date):
            logging.info("INVALID_DATE")
        self.dao.start_subscription = date

    def add_subscription(self, streaming_category, plan_type):
        try:
            self.__validator.validate_duplicate_subscription(
                streaming_category)
            self.__validator.validate_subscription_date()
        except DuplicateSubscriptionException:
            logging.info("ADD_SUBSCRIPTION_FAILED\tDUPLICATE_CATEGORY")
            return
        except InvalidDateException:
            logging.info("ADD_SUBSCRIPTION_FAILED\tINVALID_DATE")
            return

        subscription_plan = self.dao.create_subscription_plan(
            streaming_category, plan_type)
        self.dao.add_subscription(subscription_plan)

    def add_topup(self, devices, duration):
        try:
            self.__validator.validate_subscription_date()
            self.__validator.validate_subscription_exists()
            self.__validator.validate_duplicate_topup()
        except InvalidDateException:
            logging.info("ADD_TOPUP_FAILED\tINVALID_DATE")
            return
        except SubscriptionNotFoundException:
            logging.info("ADD_TOPUP_FAILED\tSUBSCRIPTIONS_NOT_FOUND")
            return
        except DuplicateTopUpException:
            logging.info("ADD_TOPUP_FAILED\tDUPLICATE_TOPUP")
            return

        topup = self.dao.create_topup(devices, int(duration))
        self.dao.top_up = topup

    def print_renewal_details(self):
        try:
            self.__validator.validate_subscription_exists()
        except SubscriptionNotFoundException:
            logging.info("SUBSCRIPTIONS_NOT_FOUND")
            return

        renewal_reminders = []
        renewal_amount = 0
        subs = self.dao.get_subscriptions()

        for sub in subs:
            renewal_amount += sub.get_amount()
            renewal_reminders.append(
                (sub.stream_category, sub.get_renewal_reminder_date()))
        if self.dao.top_up:
            renewal_amount += self.dao.top_up.get_amount()

        for renewal_reminder in renewal_reminders:
            logging.info(
                f"RENEWAL_REMINDER\t{renewal_reminder[0].name}\t{renewal_reminder[1]}")
        logging.info(f"RENEWAL_AMOUNT\t{renewal_amount}")
