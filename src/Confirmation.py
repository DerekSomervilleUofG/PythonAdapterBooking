from abc import ABC, abstractmethod

class Confirmation(ABC):

    @abstractmethod
    def confirm(self,name):
        pass
