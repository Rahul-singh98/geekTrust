from abc import ABC, abstractmethod


class IBuilder(ABC):
    """Interface for builder classes."""

    @abstractmethod
    def get_instance(self, **kwargs) -> object:
        """Get an instance based on the provided arguments.

        Implementing classes should override this method to provide the logic for creating instances.

        Args:
            **kwargs: Additional keyword arguments for building the instance.

        Returns:
            object: An instance of the desired object.

        Raises:
            NotImplementedError: If the method is not implemented by the subclass.
        """
        pass
