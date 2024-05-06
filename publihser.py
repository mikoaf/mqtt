from mqtt.mqtt import mqqts
from model.response import Response,StatusResponse
import asyncio

Send = mqqts()

async def main():
    while True:
        mqqtmessage = "run"
        mqttpub = await Send.MqttMsg(mqqtmessage)
        print (mqttpub)
        await asyncio.sleep(5)

            

asyncio.run(main())