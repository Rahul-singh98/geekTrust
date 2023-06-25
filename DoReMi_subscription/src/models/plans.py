from src.utils.enums import PlanTypeEnum, StreamCategoryEnum
from src.models.base_plan import ASubscribeablePlan, ATopUpPlan
from src.exceptions.common import InvalidDateException
from src.utils.date import validate_date, get_renewal_reminder_date


class SubscribePlan(ASubscribeablePlan):
    """Class representing a subscription plan."""

    def __init__(
        self, start_date: str, stream_category: StreamCategoryEnum,
        plan_type: PlanTypeEnum, duration_in_months: int,
        cost: int
    ):
        """Initialize a SubscribePlan instance.

        Args:
            start_date (str): The start date of the subscription in the format 'dd-mm-yyyy'.
            stream_category (StreamCategoryEnum): The stream category of the plan.
            plan_type (PlanTypeEnum): The plan type.
            duration_in_months (int): The duration of the plan in months.
            cost (int): The cost of the subscription.

        Raises:
            InvalidDateException: If the start date is invalid.
        """
        if not validate_date(start_date):
            raise InvalidDateException()
        super().__init__(start_date, stream_category, plan_type, duration_in_months, cost)

    def get_renewal_reminder_date(self) -> str:
        """Get the renewal reminder date for the subscription.

        The renewal reminder date is calculated based on the start date and duration of the associated plan.

        Returns:
            str: The renewal reminder date in the format 'dd-mm-yyyy'.
        """
        plan_duration_in_months = self._duration_in_months
        date = get_renewal_reminder_date(
            self._start_date, plan_duration_in_months)
        return date

    def get_amount(self) -> int:
        """Get the cost of the subscription.

        Returns:
            int: The cost of the subscription.
        """
        return super().get_amount()


class TopUpPlan(ATopUpPlan):
    """Class representing a top-up plan."""

    def get_amount(self) -> int:
        """Get the cost of the top-up plan.

        Returns:
            int: The cost of the top-up plan.
        """
        return super().get_amount()
