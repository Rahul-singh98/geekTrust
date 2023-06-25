RENEWAL_REMINDER_BEFORE_SUBSCRIPTION_EXPIRE_IN_DAYS = 10
DATE_FORMAT = "%d-%m-%Y"


class PlansDurationsInMonth:
    """Constants representing the durations of different plans in months."""

    FREE: int = 1
    PERSONAL: int = 1
    PREMIUM: int = 3

    TOPUP: int = 1


class PlansCost:
    """Constants representing the costs of different plans."""

    FREE: int = 0

    MUSIC_PERSONAL: int = 100
    MUSIC_PREMIUM: int = 250

    VIDEO_PERSONAL: int = 200
    VIDEO_PREMIUM: int = 500

    PODCAST_PERSONAL: int = 100
    PODCAST_PREMIUM: int = 300

    FOUR_DEVICE: int = 50
    TEN_DEVICE: int = 100
