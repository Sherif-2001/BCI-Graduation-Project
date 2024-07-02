import uasyncio as asyncio
from tasks import *

async def schedule():
    sensor_task = asyncio.create_task(read_sensors())
    espnow_task = asyncio.create_task(send_espnow())
    tcp_task = asyncio.create_task(send_tcp())
    await asyncio.gather(sensor_task, tcp_task, espnow_task)