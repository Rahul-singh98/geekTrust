from enum import Enum


class TopUpDeviceCategoryEnum(Enum):
    """Enum class representing top-up device categories in Doremi application.

    The TopUpDeviceCategoryEnum class provides an enumeration of the available device categories
    for top-up options in the Doremi application.

    Enum Values:
        FOUR_DEVICE (int): Represents the category for top-ups with four devices.
        TEN_DEVICE (int): Represents the category for top-ups with ten devices.
    """

    FOUR_DEVICE = 4
    TEN_DEVICE = 10


class PlanTypeEnum(Enum):
    """Enum class representing plan types in Doremi application.

    The PlanTypeEnum class provides an enumeration of the available plan types in the Doremi application.

    Enum Values:
        FREE (int): Represents the free plan type.
        PERSONAL (int): Represents the personal plan type.
        PREMIUM (int): Represents the premium plan type.
    """

    FREE, PERSONAL, PREMIUM = 0, 1, 2


class StreamCategoryEnum(Enum):
    """Enum class representing stream categories in Doremi application.

    The StreamCategoryEnum class provides an enumeration of the available stream categories
    in the Doremi application.

    Enum Values:
        MUSIC (int): Represents the music stream category.
        VIDEO (int): Represents the video stream category.
        PODCAST (int): Represents the podcast stream category.
    """

    MUSIC, VIDEO, PODCAST = 0, 1, 2
