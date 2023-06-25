from src.models.plans import SubscribePlan, TopUpPlan
from src.models.base_builder import IBuilder
from src.utils.enums import PlanTypeEnum, StreamCategoryEnum, TopUpDeviceCategoryEnum
from src.utils.constants import PlansDurationsInMonth, PlansCost


class SubscribeablePlanBuilder(IBuilder):
    """Builder class for creating subscribeable plans."""

    def _music_free_plan(self, date_string: str):
        """Create a music free plan and return it.

        Args:
            date_string (str): The start date of the plan in the format 'dd-mm-yyyy'.

        Returns:
            SubscribePlan: The created music free plan.
        """
        return SubscribePlan(
            date_string, StreamCategoryEnum.MUSIC, PlanTypeEnum.FREE,
            PlansDurationsInMonth.FREE, PlansCost.FREE
        )

    def _music_personal_plan(self, date_string: str):
        """Create a music personal plan and return it.

        Args:
            date_string (str): The start date of the plan in the format 'dd-mm-yyyy'.

        Returns:
            SubscribePlan: The created music personal plan.
        """
        return SubscribePlan(
            date_string, StreamCategoryEnum.MUSIC, PlanTypeEnum.PERSONAL,
            PlansDurationsInMonth.PERSONAL, PlansCost.MUSIC_PERSONAL
        )

    def _music_premium_plan(self, date_string: str):
        """Create a music premium plan and return it.

        Args:
            date_string (str): The start date of the plan in the format 'dd-mm-yyyy'.

        Returns:
            SubscribePlan: The created music premium plan.
        """
        return SubscribePlan(
            date_string, StreamCategoryEnum.MUSIC, PlanTypeEnum.PREMIUM,
            PlansDurationsInMonth.PREMIUM, PlansCost.MUSIC_PREMIUM
        )

    def _video_free_plan(self, date_string: str):
        """Create a video free plan and return it.

        Args:
            date_string (str): The start date of the plan in the format 'dd-mm-yyyy'.

        Returns:
            SubscribePlan: The created video free plan.
        """
        return SubscribePlan(
            date_string, StreamCategoryEnum.VIDEO, PlanTypeEnum.FREE,
            PlansDurationsInMonth.FREE, PlansCost.FREE
        )

    def _video_personal_plan(self, date_string: str):
        """Create a video personal plan and return it.

        Args:
            date_string (str): The start date of the plan in the format 'dd-mm-yyyy'.

        Returns:
            SubscribePlan: The created video personal plan.
        """
        return SubscribePlan(
            date_string, StreamCategoryEnum.VIDEO, PlanTypeEnum.PERSONAL,
            PlansDurationsInMonth.PERSONAL, PlansCost.VIDEO_PERSONAL
        )

    def _video_premium_plan(self, date_string: str):
        """Create a video premium plan and return it.

        Args:
            date_string (str): The start date of the plan in the format 'dd-mm-yyyy'.

        Returns:
            SubscribePlan: The created video premium plan.
        """
        return SubscribePlan(
            date_string, StreamCategoryEnum.VIDEO, PlanTypeEnum.PREMIUM,
            PlansDurationsInMonth.PREMIUM, PlansCost.VIDEO_PREMIUM
        )

    def _podcast_free_plan(self, date_string: str):
        """Create a podcast free plan and return it.

        Args:
            date_string (str): The start date of the plan in the format 'dd-mm-yyyy'.

        Returns:
            SubscribePlan: The created podcast free plan.
        """
        return SubscribePlan(
            date_string, StreamCategoryEnum.PODCAST, PlanTypeEnum.FREE,
            PlansDurationsInMonth.FREE, PlansCost.FREE
        )

    def _podcast_personal_plan(self, date_string: str):
        """Create a podcast personal plan and return it.

        Args:
            date_string (str): The start date of the plan in the format 'dd-mm-yyyy'.

        Returns:
            SubscribePlan: The created podcast personal plan.
        """
        return SubscribePlan(
            date_string, StreamCategoryEnum.PODCAST, PlanTypeEnum.PERSONAL,
            PlansDurationsInMonth.PERSONAL, PlansCost.PODCAST_PERSONAL
        )

    def _podcast_premium_plan(self, date_string: str):
        """Create a podcast premium plan and return it.

        Args:
            date_string (str): The start date of the plan in the format 'dd-mm-yyyy'.

        Returns:
            SubscribePlan: The created podcast permium plan.
        """
        return SubscribePlan(
            date_string, StreamCategoryEnum.PODCAST, PlanTypeEnum.PREMIUM,
            PlansDurationsInMonth.PREMIUM, PlansCost.PODCAST_PREMIUM
        )

    def get_instance(self, **kwargs) -> SubscribePlan:
        """Get an instance of a subscribeable plan based on provided arguments.

        Args:
            **kwargs: Additional keyword arguments for building the plan.
                Required arguments:
                    - stream_category (str): The stream category of the plan.
                    - plan_type (str): The plan type.
                    - date_string (str): The start date of the plan in the format 'dd-mm-yyyy'.

        Returns:
            SubscribePlan: An instance of the subscribeable plan.

        Raises:
            ValueError: If the provided arguments are not valid or incomplete.
        """
        stream_category: str = kwargs.get('stream_category').lower()
        plan_type: str = kwargs.get('plan_type').lower()
        date_string: str = kwargs.get('date_string').lower()

        if not stream_category or not plan_type or not date_string:
            raise ValueError(
                "stream_category, plan_type, date_string is not valid or not str object.")

        if hasattr(self, f"_{stream_category}_{plan_type}_plan"):
            func = getattr(
                self, f"_{stream_category}_{plan_type}_plan")
            return func(date_string)
        raise ValueError(f"Can not build a plan with {kwargs} arguments.")


class TopUpPlanBuilder(IBuilder):
    """Builder class for creating top-up plans."""

    def _four_device_topup(self, subscription_period: int):
        """Create a top-up plan for four devices and return it.

        Args:
            subscription_period (int): The duration of the top-up plan in months.

        Returns:
            TopUpPlan: The created top-up plan for four devices.
        """
        return TopUpPlan(
            TopUpDeviceCategoryEnum.FOUR_DEVICE,
            PlansDurationsInMonth.TOPUP,
            PlansCost.FOUR_DEVICE,
            subscription_period
        )

    def _ten_device_topup(self, subscription_period: int):
        """Create a top-up plan for ten devices and return it.

        Args:
            subscription_period (int): The duration of the top-up plan in months.

        Returns:
            TopUpPlan: The created top-up plan for ten devices.
        """
        return TopUpPlan(
            TopUpDeviceCategoryEnum.TEN_DEVICE,
            PlansDurationsInMonth.TOPUP,
            PlansCost.TEN_DEVICE,
            subscription_period
        )

    def get_instance(self, **kwargs) -> TopUpPlan:
        """Get an instance of a top-up plan based on provided arguments.

        Args:
            **kwargs: Additional keyword arguments for building the plan.
                Required arguments:
                    - top_category (str): The top-up device category.
                    - subscription_period (int): The duration of the top-up plan in months.

        Returns:
            TopUpPlan: An instance of the top-up plan.

        Raises:
            ValueError: If the provided arguments are not valid or incomplete.
        """
        device_category: str = kwargs.get('device_category').lower()
        subscription_period: int = int(kwargs.get('subscription_period'))

        if not device_category or not subscription_period:
            raise ValueError(
                "device_category, subscription_period is not valid.")

        if hasattr(self, f'_{device_category}_topup'):
            func = getattr(
                self, f'_{device_category}_topup'
            )
            return func(subscription_period)
        raise ValueError(f"Can not build a plan with {kwargs} arguments.")
