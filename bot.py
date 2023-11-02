import os
import logging
import asyncio
from colorama import init, Fore as F, Back as B, Style as S
from aiogram.utils import executor
from create_bot import dp
from handlers.client import event_reminder
from aiogram.contrib.fsm_storage.memory import MemoryStorage

init(autoreset=True)

async def on_startup(_):
    print(F.GREEN + "[+] Bot is online and working!")
    try:
        asyncio.create_task(event_reminder())
    except (ValueError, TypeError, sqlite3.Error) as error:
        print(F.RED + "[-]: Error currupted while starting event reminder! > " + F.WHITE + error)
    finally:
        print(F.GREEN + "[+] Event Reminder started!")


from handlers import client
from buttons import buttons_main
from cist_libs import *
from CIST import cist


client.reg_handlers_client(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
