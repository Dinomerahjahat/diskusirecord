#(©)Codexbotz

import pyromod.listen
from pyrogram import Client
import sys

from config import API_HASH, APP_ID, LOGGER, TG_BOT_TOKEN, TG_BOT_WORKERS, FORCE_SUB_CHANNEL, CHANNEL_ID

class Bot(Client):
    def __init__(self):
        super().__init__(
            "Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "plugins"
            },
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()

        if FORCE_SUB_CHANNEL:
            try:
                link = (await self.get_chat(FORCE_SUB_CHANNEL)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_CHANNEL)
                    link = (await self.get_chat(FORCE_SUB_CHANNEL)).invite_link
                self.invitelink = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bot tidak dapat Mengekspor tautan Undangan dari Force Sub Channel!")
                self.LOGGER(__name__).warning(f"Silakan periksa kembali FORCE_SUB_CHANNEL dan Pastikan Bot adalah Admin di saluran dengan Undang Pengguna melalui Izin Tautan, Nilai Angkatan Sub Channel Saat Ini: {FORCE_SUB_CHANNEL}")
                self.LOGGER(__name__).info("\nBot Stopped. Join https://t.me/rexaprivateroom")
                sys.exit()
        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id = db_channel.id, text = "Test Message")
            await test.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(f"Pastikan bot adalah Admin di Saluran DB, dan Periksa kembali CHANNEL_ID, Channel Saat Ini {CHANNEL_ID}")
            self.LOGGER(__name__).info("\nBot Berhenti. Bergabunglah dengan https://t.me/rexaprivateroom")
            sys.exit()

        self.set_parse_mode("html")
        self.LOGGER(__name__).info(f"Menjalankan Bot..!\n\nDibuat oleh Rexashh\nhttps://t.me/JustRex")
        self.username = usr_bot_me.username

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped.")
