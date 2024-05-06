from abc import ABC,abstractmethod
from model_mqtt.mqtt import MqttSender
from model_mqtt.response import Response
from typing import Tuple
import asyncio

class MqttSend(ABC):
    @abstractmethod
    async def MqttMsg(self,msg:str)->Response:
        pass