from abc import ABC, abstractmethod
from src.utils.enums import StreamCategoryEnum, PlanTypeEnum, TopUpDeviceCategoryEnum


class IPlan(ABC):
    """Interface for a plan."""

    @property
    @abstractmethod
    def duration_in_months(self) -> int:
        """Get the duration of the plan in months."""
        pass

    @duration_in_months.setter
    @abstractmethod
    def duration_in_months(self, n_duration_in_months: int):
        """Set the duration of the plan in months."""
        pass

    @property
    @abstractmethod
    def cost(self) -> int:
        """Get the cost of the plan in currency."""
        pass

    @cost.setter
    @abstractmethod
    def cost(self, n_cost: int) -> int:
        """Set the cost of the plan in currency."""
        pass

    @abstractmethod
    def get_amount(self) -> int:
        """Calculate and return the total amount for the plan."""
        pass


class ASubscribeablePlan(IPlan, ABC):
    """Abstract class for a subscribeable plan."""

    def __init__(
        self, start_date: str, stream_category: StreamCategoryEnum,
        plan_type: PlanTypeEnum, duration_in_months: int,
        cost: int
    ):
        self._start_date = start_date
        self._stream_category = stream_category
        self._plan_type = plan_type
        self._duration_in_months = duration_in_months
        self._cost = cost

    @property
    def start_date(self) -> str:
        """Get the start date of the subscription.

        Returns:
            str: The start date of the subscription in the format 'dd-mm-yyyy'.
        """
        return self._start_date

    @property
    def stream_category(self) -> StreamCategoryEnum:
        """Get the stream category of the plan."""
        return self._stream_category

    @property
    def plan_type(self) -> PlanTypeEnum:
        """Get the plan type."""
        return self._plan_type

    @property
    def duration_in_months(self) -> int:
        """Get the duration of the plan in months."""
        return self._duration_in_months

    @duration_in_months.setter
    def duration_in_months(self, n_duration_in_months: int):
        """Set the duration of the plan in months."""
        self._duration_in_months = n_duration_in_months

    @property
    def cost(self) -> int:
        """Get the cost of the plan in currency."""
        return self._cost

    @cost.setter
    def cost(self, n_cost: int):
        """Set the cost of the plan in currency."""
        self._cost = n_cost

    @abstractmethod
    def get_amount(self) -> int:
        """Calculate and return the total amount for the plan."""
        return self.cost

    @abstractmethod
    def get_renewal_reminder_date(self) -> str:
        pass


class ATopUpPlan(IPlan, ABC):
    """Abstract class for a top-up plan."""

    def __init__(
        self, device_category: TopUpDeviceCategoryEnum,
        duration_in_months: int, cost: int, period: int
    ):
        self._device_category = device_category
        self._duration_in_months = duration_in_months
        self._cost = cost
        self._period = period

    @property
    def device_category(self) -> TopUpDeviceCategoryEnum:
        """Get the top-up device category of the plan."""
        return self._device_category

    @property
    def duration_in_months(self) -> int:
        """Get the duration of the plan in months."""
        return self._duration_in_months

    @duration_in_months.setter
    def duration_in_months(self, n_duration_in_months: int):
        """Set the duration of the plan in months."""
        self._duration_in_months = n_duration_in_months

    @property
    def cost(self) -> int:
        """Get the cost of the plan in currency."""
        return self._cost

    @cost.setter
    def cost(self, n_cost: int):
        """Set the cost of the plan in currency."""
        self._cost = n_cost

    @abstractmethod
    def get_amount(self) -> int:
        """Calculate and return the total amount for the plan."""
        return self._period * self.cost
