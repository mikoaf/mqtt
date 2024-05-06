from abc import ABC,abstractmethod
from model.mqtt import MqttSender
from model.response import Response
from typing import Tuple
import asyncio

class MqttSend(ABC):
    @abstractmethod
    async def MqttMsg(self,msg:str)->Response:
        pass