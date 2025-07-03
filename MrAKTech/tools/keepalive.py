# Copyright 2021 To 2024-present, Author: MrAKTech

import asyncio
import logging
import aiohttp
import traceback
from MrAKTech.config import Server


async def ping_server():
    sleep_time = Server.PING_INTERVAL
    while True:
        await asyncio.sleep(sleep_time)
        try:
            async with aiohttp.ClientSession(
                timeout=aiohttp.ClientTimeout(total=10)
            ) as session:
                async with session.get(Server.URL) as resp:
                    logging.info("Pinged server with response: {}".format(resp.status))
        except TimeoutError:
            logging.warning("Couldn't connect to the site URL..!")
        except Exception:
            traceback.print_exc()
