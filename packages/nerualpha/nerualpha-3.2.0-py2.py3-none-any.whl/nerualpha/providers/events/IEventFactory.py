from dataclasses import dataclass, field
from typing import Dict, List, Generic, TypeVar
from abc import ABC, abstractmethod

from nerualpha.providers.events.INeruEvent import INeruEvent


#interface
class IEventFactory(ABC):
    @abstractmethod
    def createEvent(self,eventName,details):
        pass
