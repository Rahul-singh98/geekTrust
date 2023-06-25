from src.models.plan_builder import TopUpPlanBuilder, SubscribeablePlanBuilder
from src.models.base_plan import ATopUpPlan, ASubscribeablePlan
from typing import Optional, List
import copy


def singleton(cls):
    """Decorator function that implements the Singleton pattern.

    The singleton decorator ensures that only one instance of a class is created and provides a global
    point of access to that instance.

    Args:
        cls (class): The class to be decorated as a singleton.

    Returns:
        function: The wrapper function that implements the Singleton behavior.

    Example:
        @singleton
        class SingletonClass:
            def __init__(self, name):
                self.name = name

        instance1 = SingletonClass("Instance 1")
        instance2 = SingletonClass("Instance 2")

        print(instance1.name)  # Output: Instance 1
        print(instance2.name)  # Output: Instance 1 (same instance as instance1)

    Note:
        The Singleton pattern implemented using this decorator is not strictly enforced in Python.
        It's still possible to create additional instances by manipulating the class or using other techniques.
        However, this implementation discourages the creation of multiple instances by convention and provides
        a straightforward way to access the singleton instance.
    """
    instance = None

    def wrapper(*args, **kwargs):
        nonlocal instance
        if not instance:
            instance = cls(*args, **kwargs)
        return instance

    return wrapper


@singleton
class DoremiDao:
    """Singleton class representing the Doremi data access object."""

    def __init__(self):
        """Initialize the DoremiDao instance."""
        self.__start_subscription = ""
        self.__top_up: Optional[ATopUpPlan] = None
        self.__subscription_builder = SubscribeablePlanBuilder()
        self.__topup_builder = TopUpPlanBuilder()
        self.__subscriptions: List[ASubscribeablePlan] = []

    @property
    def start_subscription(self) -> str:
        """Get the start subscription date.

        Returns:
            str: The start subscription date in the format 'dd-mm-yyyy'.
        """
        return self.__start_subscription

    @start_subscription.setter
    def start_subscription(self, date_string: str):
        """Set the start subscription date.

        Args:
            date_string (str): The start subscription date in the format 'dd-mm-yyyy'.
        """
        self.__start_subscription = date_string

    @property
    def top_up(self) -> ATopUpPlan:
        """Get the top-up plan.

        Returns:
            ATopUpPlan: The top-up plan instance.
        """
        return self.__top_up

    @top_up.setter
    def top_up(self, top_up: ATopUpPlan):
        """Set the top-up plan.

        Args:
            top_up (ATopUpPlan): The top-up plan instance.
        """
        self.__top_up = top_up

    def add_subscription(self, subscription: ASubscribeablePlan):
        """Add a subscription to the list of subscriptions.

        Args:
            subscription (ASubscribeablePlan): The subscription to be added.
        """
        self.__subscriptions.append(subscription)

    def create_subscription_plan(self, stream_category: str, plan_type: str):
        """Create a subscription plan instance based on the stream category and plan type.

        Args:
            stream_category (str): The stream category of the plan.
            plan_type (str): The plan type.

        Returns:
            object: An instance of the desired subscription plan.

        Raises:
            ValueError: If the plan cannot be built with the provided arguments.
        """
        return self.__subscription_builder.get_instance(
            date_string=self.start_subscription,
            stream_category=stream_category,
            plan_type=plan_type
        )

    def get_subscriptions(self) -> List[ASubscribeablePlan]:
        """Get a deep copy of the list of subscriptions.

        Returns:
            List[ASubscribeablePlan]: A list of subscription instances.
        """
        return copy.deepcopy(self.__subscriptions)

    def create_topup(self, device_category: str, duration_in_months: int) -> ATopUpPlan:
        """Create a top-up plan instance based on the device category.

        Args:
            device_category (str): The device category.
            duration_in_months (int): Topup duration in months.

        Returns:
            ATopUpPlan: An instance of the desired top-up plan.

        Raises:
            ValueError: If the plan cannot be built with the provided arguments.
        """
        return self.__topup_builder.get_instance(
            device_category=device_category, subscription_period=duration_in_months
        )
