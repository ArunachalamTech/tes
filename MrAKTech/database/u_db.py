# Copyright 2021 To 2024-present, Author: MrAKTech

import datetime
import motor.motor_asyncio
from MrAKTech.config import Telegram
from MrAKTech.tools.txt import tamilxd


class Database:
    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.col = self.db.users
        self.su = self.db.StorageUsers
        self.black = self.db.blacklist
        self.chl = self.db.ChannelsList
        self.warn = self.db.WarnsList
        self.bot = self.db.bots
        self.Inactive = self.db.InActiveUsers

    def new_user(self, id):
        return dict(
            id=id,
            join_date=datetime.date.today().isoformat(),
            shortener_api=None,
            shortener_url=None,
            method="links",
            caption=tamilxd.STREAM_MSG_TXT,
            settings=None,
            storage="Off",
            auto_extract=True,  # Enable auto extraction by default
            linkmode=False,  # Linkmode disabled by default
            shortlink1_url=None,
            shortlink1_api=None,
            shortlink2_url=None,
            shortlink2_api=None,
            shortlink3_url=None,
            shortlink3_api=None,
            linkmode_caption1=None,
            linkmode_caption2=None,
            linkmode_caption3=None,
            active_linkmode_caption=1,
            file_batch=[],
            batch_mode=False,
        )

    async def add_user(self, id):
        user = self.new_user(id)
        await self.col.insert_one(user)

    async def get_user(self, id):
        return await self.col.find_one({"id": id})

    async def is_user_exist(self, id):
        user = await self.col.find_one({"id": int(id)})
        return bool(user)

    async def total_users_count(self):
        return await self.col.count_documents({})

    async def get_all_users(self):
        return self.col.find({})

    async def delete_user(self, user_id):
        await self.col.delete_many({"id": int(user_id)})

    # testing start

    async def get_user_details(self, user_id: int):
        return await self.col.find_one({"id": int(user_id)})

    async def set_caption(self, id, caption):
        await self.col.update_one({"id": id}, {"$set": {"caption": caption}})

    async def get_caption(self, id):
        user = await self.col.find_one({"id": int(id)})
        return user.get("caption", None)

    async def set_shortner_url(self, id, caption):
        await self.col.update_one({"id": id}, {"$set": {"shortener_url": caption}})

    async def get_shortner_url(self, id):
        user = await self.col.find_one({"id": int(id)})
        return user.get("shortener_url", None)

    async def set_shortner_api(self, id, caption):
        await self.col.update_one({"id": id}, {"$set": {"shortener_api": caption}})

    async def get_shortner_api(self, id):
        user = await self.col.find_one({"id": int(id)})
        return user.get("shortener_api", None)

    async def change_uploadmode(self, id, mode):
        await self.col.update_one({"id": id}, {"$set": {"method": mode}})

    async def get_uploadmode(self, id):
        user = await self.col.find_one({"id": int(id)})
        return user.get("method", None)

    async def change_storagemode(self, id, mode):
        await self.col.update_one({"id": id}, {"$set": {"storage": mode}})

    async def get_storagemode(self, id):
        user = await self.col.find_one({"id": int(id)})
        return user.get("storage", None)

    async def update_user_info(self, user_id, value: dict, tag="$set"):
        user_id = int(user_id)
        myquery = {"id": user_id}
        newvalues = {tag: value}
        await self.col.update_one(myquery, newvalues)

    async def reset_settings(self, id):
        await self.col.update_one(
            {"id": id},
            {
                "$set": {
                    "shortener_api": None,
                    "shortener_url": None,
                    "method": "links",
                    "caption": tamilxd.STREAM_MSG_TXT,
                    "linkmode": False,
                    "linkmode_shortlinks": {},
                    "linkmode_batch": [],
                    "linkmode_captions": []
                }
            },
        )

    async def is_settings(self, id):
        user = await self.col.find_one({"id": int(id)})
        return bool(user.get("caption") or user.get("shortener_url") or user.get("shortener_api"))

    # Channel Database Codes

    default_setgs = {
        "api": None,
        "url": None,
        "shortlink": False,
        "method": "Button",
        "caption": tamilxd.STREAM_MSG_TXT,
        "replace": None,
    }

    async def in_channel(self, user_id: int, chat_id : int) -> bool:
        channel = await self.chl.find_one({"user_id": int(user_id), "chat_id": int(chat_id)})
        return bool(channel)

    async def add_channel(self, user_id: int, chat_id : int, title, username):
        channel = await self.in_channel(int(user_id), int(chat_id))
        if channel:
            return False
        return await self.chl.insert_one(
            {
                "user_id": int(user_id),
                "chat_id": int(chat_id),
                "title": title,
                "username": username,
                "settings": self.default_setgs,
            }
        )

    async def remove_channel(self, user_id: int, chat_id : int):
        channel = await self.in_channel(int(user_id), int(chat_id))
        if not channel:
            return False
        return await self.chl.delete_many({"user_id": int(user_id), "chat_id": int(chat_id)})

    async def is_channel_exist(self, chat_id):
        channel = await self.chl.find_one({"chat_id": int(chat_id)})
        return bool(channel)

    async def get_channel_details(self, user_id: int, chat_id : int):
        return await self.chl.find_one({"user_id": int(user_id), "chat_id": int(chat_id)})

    async def get_user_channels(self, user_id: int):
        channels = self.chl.find({"user_id": int(user_id)})
        return [channel async for channel in channels]

    async def get_chl_settings(self, chat_id : int):
        chat = await self.chl.find_one({"chat_id": int(chat_id)})
        return chat.get("settings", self.default_setgs) if chat else self.default_setgs

    async def update_chl_settings(self, chat_id : int, type, value):
        await self.chl.update_one(
            {"chat_id": int(chat_id)}, {"$set": {f"settings.{type}": value}}
        )

    async def get_channel_detail(self, chat_id : int):
        return await self.chl.find_one({"chat_id": int(chat_id)})

    async def total_channels_count(self):
        return await self.chl.count_documents({})

    async def reset_chl_settings(self, chat_id : int):
        await self.chl.update_one(
            {"chat_id": int(chat_id)}, {"$set": {"settings": self.default_setgs}}
        )

    async def is_chl_settings(self, chat_id):
        chat = await self.get_chl_settings(chat_id)
        if chat["url"] is None and chat["api"] is None:
            if chat["caption"] == tamilxd.STREAM_MSG_TXT and chat["method"] == "Button":
                return False
        return True

    async def get_all_chat(self):
        return self.chl.find({})

    async def update_chat(self, id, chat_id):
        await self.col.update_one({"_id": id}, {"$set": {"chat_id": int(chat_id)}})

    # bot testing end

    async def get_bot(self, user_id: int):
        bot = await self.bot.find_one({"user_id": user_id})
        return bot if bot else None

    async def total_users_bots_count(self):
        count = await self.bot.count_documents({})
        return count

    # ----------------------ban, check banned or unban user----------------------

    def black_user(self, id):
        return dict(id=id, ban_date=datetime.date.today().isoformat())

    async def ban_user(self, id):
        user = self.black_user(id)
        await self.black.insert_one(user)

    async def unban_user(self, id):
        await self.black.delete_one({"id": int(id)})

    async def is_user_banned(self, id):
        user = await self.black.find_one({"id": int(id)})
        return True if user else False

    async def total_banned_users_count(self):
        count = await self.black.count_documents({})
        return count

    # --------------------------- Storage Bot Users ----------------------------

    def snew_user(self, id):
        return dict(
            id=id,
            join_date=datetime.date.today().isoformat(),
        )

    async def sadd_user(self, id):
        user = self.snew_user(id)
        await self.su.insert_one(user)

    async def sget_user(self, id):
        return await self.su.find_one({"id": id})

    async def sis_user_exist(self, id):
        user = await self.su.find_one({"id": int(id)})
        return bool(user)

    async def stotal_users_count(self):
        return await self.su.count_documents({})

    async def sget_all_users(self):
        return self.su.find({})

    async def sdelete_user(self, user_id):
        await self.su.delete_many({"id": int(user_id)})


    # --------------------------- Warn Bot Users ----------------------------

    def wnew_user(self, id : int, msg : str =None):
        return dict(
            id=int(id),
            warn_count= 1,
            warn_msg=str(msg),
            warn_date=datetime.date.today().isoformat(),
        )
    
    async def wadd_user(self, id : int, msg : str):
        user = self.wnew_user(id, msg)
        await self.warn.insert_one(user)

    async def wget_user(self, id : int):
        return await self.warn.find_one({"id": id})
    
    async def is_wuser_exist(self, id : int):
        user = await self.warn.find_one({"id": int(id)})
        return bool(user)
    
    async def wupdate_user(self, id : int, msg : str, count : int):
        await self.warn.update_one({"id": id}, {"$set": {"warn_msg": msg, "warn_count": count}})
    
    async def wtotal_users_count(self):
        return await self.warn.count_documents({})
    
    async def wget_all_users(self):
        return self.warn.find({})
    
    async def wdelete_user(self, user_id):
        await self.warn.delete_many({"id": int(user_id)})

    # --------------------------- Inactive Bot Users ----------------------------

    def inew_user(self, id):
        return dict(
            id=id,
            join_date=datetime.date.today().isoformat(),
        )
    
    async def iadd_user(self, id):
        user = self.inew_user(id)
        await self.Inactive.insert_one(user)

    async def iget_user(self, id):
        return await self.Inactive.find_one({"id": id})
    
    async def iis_user_exist(self, id):
        user = await self.Inactive.find_one({"id": int(id)})
        return bool(user)
    
    async def itotal_users_count(self):
        return await self.Inactive.count_documents({})

    # Auto extraction methods
    async def set_auto_extract(self, id, enabled):
        await self.col.update_one({"id": id}, {"$set": {"auto_extract": enabled}})

    async def get_auto_extract(self, id):
        user = await self.col.find_one({"id": int(id)})
        return user.get("auto_extract", True)

    # Linkmode methods
    async def set_linkmode(self, id, enabled):
        await self.col.update_one({"id": id}, {"$set": {"linkmode": enabled}})

    async def get_linkmode(self, id):
        user = await self.col.find_one({"id": int(id)})
        return user.get("linkmode", False)

    # Shortlink methods for linkmode
    async def set_shortlink1(self, id, url, api):
        await self.col.update_one({"id": id}, {"$set": {"shortlink1_url": url, "shortlink1_api": api}})

    async def set_shortlink2(self, id, url, api):
        await self.col.update_one({"id": id}, {"$set": {"shortlink2_url": url, "shortlink2_api": api}})

    async def set_shortlink3(self, id, url, api):
        await self.col.update_one({"id": id}, {"$set": {"shortlink3_url": url, "shortlink3_api": api}})

    async def get_shortlink1(self, id):
        user = await self.col.find_one({"id": int(id)})
        return user.get("shortlink1_url"), user.get("shortlink1_api")

    async def get_shortlink2(self, id):
        user = await self.col.find_one({"id": int(id)})
        return user.get("shortlink2_url"), user.get("shortlink2_api")

    async def get_shortlink3(self, id):
        user = await self.col.find_one({"id": int(id)})
        return user.get("shortlink3_url"), user.get("shortlink3_api")

    async def delete_shortlink1(self, id):
        await self.col.update_one({"id": id}, {"$unset": {"shortlink1_url": "", "shortlink1_api": ""}})

    async def delete_shortlink2(self, id):
        await self.col.update_one({"id": id}, {"$unset": {"shortlink2_url": "", "shortlink2_api": ""}})

    async def delete_shortlink3(self, id):
        await self.col.update_one({"id": id}, {"$unset": {"shortlink3_url": "", "shortlink3_api": ""}})

    # Linkmode caption methods
    async def set_linkmode_caption1(self, id, caption):
        await self.col.update_one({"id": id}, {"$set": {"linkmode_caption1": caption}})

    async def set_linkmode_caption2(self, id, caption):
        await self.col.update_one({"id": id}, {"$set": {"linkmode_caption2": caption}})

    async def set_linkmode_caption3(self, id, caption):
        await self.col.update_one({"id": id}, {"$set": {"linkmode_caption3": caption}})

    async def get_linkmode_caption1(self, id):
        user = await self.col.find_one({"id": int(id)})
        return user.get("linkmode_caption1")

    async def get_linkmode_caption2(self, id):
        user = await self.col.find_one({"id": int(id)})
        return user.get("linkmode_caption2")

    async def get_linkmode_caption3(self, id):
        user = await self.col.find_one({"id": int(id)})
        return user.get("linkmode_caption3")

    async def delete_linkmode_caption1(self, id):
        await self.col.update_one({"id": id}, {"$unset": {"linkmode_caption1": ""}})

    async def delete_linkmode_caption2(self, id):
        await self.col.update_one({"id": id}, {"$unset": {"linkmode_caption2": ""}})

    async def delete_linkmode_caption3(self, id):
        await self.col.update_one({"id": id}, {"$unset": {"linkmode_caption3": ""}})

    async def set_active_linkmode_caption(self, id, caption_number):
        await self.col.update_one({"id": id}, {"$set": {"active_linkmode_caption": caption_number}})

    async def get_active_linkmode_caption(self, id):
        user = await self.col.find_one({"id": int(id)})
        return user.get("active_linkmode_caption", 1)

    # File batch tracking for linkmode
    async def start_file_batch(self, id):
        await self.col.update_one({"id": id}, {"$set": {"file_batch": [], "batch_mode": True}})

    async def add_file_to_batch(self, id, file_info):
        await self.col.update_one({"id": id}, {"$push": {"file_batch": file_info}})

    async def get_file_batch(self, id):
        user = await self.col.find_one({"id": int(id)})
        return user.get("file_batch", [])

    async def clear_file_batch(self, id):
        await self.col.update_one({"id": id}, {"$unset": {"file_batch": "", "batch_mode": ""}})

    async def is_batch_mode(self, id):
        user = await self.col.find_one({"id": int(id)})
        return user.get("batch_mode", False)

    async def is_settings(self, id):
        user = await self.col.find_one({"id": int(id)})
        return bool(user.get("caption") or user.get("shortener_url") or user.get("shortener_api"))


# Create the database instance
u_db = Database(Telegram.DATABASE_URL, "MrAKTech")
