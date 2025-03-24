from abc import ABC, abstractmethod

class Observer(ABC):

    @abstractmethod
    def update(self, monitor_tool) -> None:
        """
        Receive update from monitor tool.
        """
        pass
