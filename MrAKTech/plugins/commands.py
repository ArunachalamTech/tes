import asyncio
import time
import os
import requests

from telegraph import upload_file
import logging
from platform import python_version

from pyrogram import filters, enums, __version__
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.enums.parse_mode import ParseMode

from MrAKTech import StreamBot
from MrAKTech.config import Telegram
from MrAKTech.tools.txt import tamilxd, BUTTON
from MrAKTech.database.u_db import u_db
from MrAKTech.tools.utils_bot import temp, readable_time, verify_user, is_check_admin

logger = logging.getLogger(__name__)


@StreamBot.on_message(
    filters.command("stop") & filters.private & filters.user(list(Telegram.OWNER_ID))
)
async def alive(bot: StreamBot, message: Message):  # type: ignore
    print("Stopping...")
    ax = await message.reply("Stopping...")
    try:
        await StreamBot.stop()
    except:  # noqa: E722
        pass
    print("Bot Stopped")
    await ax.edit_text("Bot Stopped")


@StreamBot.on_message(filters.command("alive"))
async def alivex(bot: StreamBot, message: Message):  # type: ignore
    txt = (
        f"**{temp.B_NAME}** ```RUNNING```\n"
        f"-> Current Uptime: `{readable_time((time.time() - temp.START_TIME))}`\n"
        f"-> Python: `{python_version()}`\n"
        f"-> Pyrogram: `{__version__}`"
    )
    await message.reply_text(txt, quote=True)


@StreamBot.on_message(filters.command("start") & filters.private)
async def start(client, message):
    if not await verify_user(client, message):
        return
    chat_id = message.text.split("_")[-1]
    if chat_id == "/start":
        await message.reply_photo(
            photo="https://graph.org/file/8cd764fbdf3ccd34abe22.jpg",
            caption=tamilxd.START_TXT.format(
                message.from_user.first_name, message.from_user.id
            ),
            parse_mode=ParseMode.HTML,
            reply_markup=BUTTON.START_BUTTONS,
            quote=True,
        )
    else:
        if "channel" in message.text:
            tamil = await message.reply_text(
                "Geting your channel data, Please Wait...", quote=True
            )
            chat = await client.get_chat(chat_id)
            if chat.type != enums.ChatType.CHANNEL:
                await tamil.edit_text("This is Invalid command.")
            if not await is_check_admin(client, chat_id, message.from_user.id):
                await tamil.edit_text("You are not an admin in this channel.")
            else:
                username = chat.username
                username = "@" + username if username else "private"
                chatx = await u_db.add_channel(
                    int(message.from_user.id), int(chat_id), chat.title, username
                )
                await tamil.edit_text(
                    (
                        "<b>Channel added successfully.</b>"
                        if chatx
                        else "<b>This channel already added!...</b>"
                    ),
                    reply_markup=InlineKeyboardMarkup(
                        [[InlineKeyboardButton("≺≺ Back", callback_data="channels")]]
                    ),
                )
        else:
            await message.reply_text("**Invalid Command**", quote=True)


@StreamBot.on_message(filters.private & filters.command(["about"]))
async def about(bot, update):
    await update.reply_text(
        text=tamilxd.ABOUT_TXT,
        disable_web_page_preview=True,
        reply_markup=BUTTON.ABOUT_BUTTONS,
        quote=True,
    )


@StreamBot.on_message(filters.command("help") & filters.private)
async def help_handler(bot, message):
    await message.reply_text(
        text=tamilxd.HELP_TXT,
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True,
        reply_markup=BUTTON.HELP_BUTTONS,
        quote=True,
    )


# thiss is for shortner
@StreamBot.on_message(filters.command(["shortner", "shortener"]) & filters.private)
async def shortner(bot, message):
    if not await verify_user(bot, message):
        return
    user_id = message.from_user.id
    userxdb = await u_db.get_user_details(user_id)
    buttons = []
    if userxdb["shortener_url"] and userxdb["shortener_api"] is not None:
        buttons.append(
            [InlineKeyboardButton("Show shortner", callback_data="show_shortner")]
        )
        buttons.append(
            [
                InlineKeyboardButton(
                    "Default shortner", callback_data="delete_shortner"
                ),
                InlineKeyboardButton("Change shortner", callback_data="add_shortner"),
            ]
        )
    else:
        buttons.append(
            [InlineKeyboardButton("Set shortner", callback_data="add_shortner")]
        )
    buttons.append([InlineKeyboardButton("Close", callback_data="close")])
    await message.reply_text(
        text=tamilxd.CUSTOM_SHORTNER_TXT,
        disable_web_page_preview=True,
        quote=True,
        reply_markup=InlineKeyboardMarkup(buttons),
    )


# this is for caption
@StreamBot.on_message(filters.command("caption"))
async def caption(bot, message):
    if not await verify_user(bot, message):
        return
    user_id = message.from_user.id
    caption = await u_db.get_caption(user_id)
    buttons = []
    if caption is not None:
        buttons.append(
            [InlineKeyboardButton("Show caption", callback_data="show_caption")]
        )
        buttons.append(
            [
                InlineKeyboardButton("Default caption", callback_data="delete_caption"),
                InlineKeyboardButton("Change caption", callback_data="add_caption"),
            ]
        )
    else:
        buttons.append(
            [InlineKeyboardButton("Set caption", callback_data="add_caption")]
        )
    buttons.append([InlineKeyboardButton("Close", callback_data="close")])
    await message.reply_text(
        text=tamilxd.CUSTOM_CAPTION_TXT,
        disable_web_page_preview=True,
        quote=True,
        reply_markup=InlineKeyboardMarkup(buttons),
    )


@StreamBot.on_message(filters.command("settings"))
async def settings(client, message):
    await message.reply_text(
        "<b>ᴄʜᴀɴɢᴇ ʏᴏᴜʀ ꜱᴇᴛᴛɪɴɢꜱ ᴀꜱ ʏᴏᴜʀ ᴡɪꜱʜ </b>",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Personal settings", callback_data="settings"),
                ],
                [InlineKeyboardButton("Channels settings", callback_data="channels")],
                [InlineKeyboardButton("≺≺ Close", callback_data="close")],
            ]
        ),
    )


# this is for user settings
@StreamBot.on_message(filters.command(["usetting", "us", "usettings"]))
async def settings(client, message):  # noqa: F811
    userxdb = await u_db.get_user_details(message.from_user.id)
    button = [
        [
            InlineKeyboardButton(
                (
                    "✅ Custom caption"
                    if userxdb["caption"] is not None
                    else "📝 Custom caption"
                ),
                callback_data="custom_caption",
            )
        ],
        [
            InlineKeyboardButton(
                (
                    "✅ Custom shortner"
                    if userxdb["shortener_url"] and userxdb["shortener_api"] is not None
                    else "🖼️ Custom shortner"
                ),
                callback_data="custom_shortner",
            )
        ],
        [
            InlineKeyboardButton("📤 Upload mode", callback_data="toggle_mode"),
            InlineKeyboardButton(
                userxdb["method"] if userxdb["method"] else "Links",
                callback_data="toggle_mode",
            ),
        ],
        [InlineKeyboardButton("Close ✗", callback_data="close")],
    ]
    await message.reply_text(
        text=tamilxd.SETTINGS_TXT.format(
            CAPTION="✅ Exists" if userxdb["caption"] is not None else "❌ Not Exists",
            URLX=(
                userxdb["shortener_url"]
                if userxdb["shortener_url"] is not None
                else "❌ Not Exists"
            ),
            APIX=(
                userxdb["shortener_api"]
                if userxdb["shortener_api"] is not None
                else "❌ Not Exists"
            ),
            STORAGEX=userxdb["storage"],
            METHODX=userxdb["method"],
            AUTO_EXTRACT="✅ Enabled" if userxdb.get("auto_extract", True) else "❌ Disabled",
        ),
        reply_markup=InlineKeyboardMarkup(button),
        disable_web_page_preview=True,
        quote=True,
    )


# this is for channels settings
@StreamBot.on_message(filters.command(["channels", "csetting", "cs", "csettings"]))
async def settings(bot, msg):  # noqa: F811
    buttons = []
    channels = await u_db.get_user_channels(msg.from_user.id)
    for channel in channels:
        buttons.append(
            [
                InlineKeyboardButton(
                    f"{channel['title']}",
                    callback_data=f"editchannels_{channel['chat_id']}",
                )
            ]
        )
    buttons.append(
        [InlineKeyboardButton("✚ Add Channel ✚", callback_data="addchannel")]
    )
    buttons.append([InlineKeyboardButton("≺≺ Back", callback_data="main")])
    await msg.reply_text(
        "<b><u>My Channels</b></u>\n\n<b>you can manage your target chats in here</b>",
        reply_markup=InlineKeyboardMarkup(buttons),
        quote=True,
    )


# this is for features
@StreamBot.on_message(filters.command("features") & filters.private)
async def about_handler(bot, message):
    hs = await message.reply_photo(
        photo="https://graph.org/file/68a0935f0d19ffd647a09.jpg",
        caption=(tamilxd.COMMENTS_TXT.format(message.from_user.mention)),
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("↻ ᴄʟᴏsᴇ ↻", callback_data="close")]]
        ),
    )
    await asyncio.sleep(150)
    await hs.delete()
    await message.delete()


# this is for id get
@StreamBot.on_message(filters.command("id"))
async def get_id(bot: StreamBot, message: Message):  # type: ignore
    file_id = None
    user_id = None

    if message.reply_to_message:
        rep = message.reply_to_message

        if rep.audio:
            file_id = f"**File ID**: `{rep.audio.file_id}`"
            file_id += "**File Type**: `audio`"

        elif rep.document:
            file_id = f"**File ID**: `{rep.document.file_id}`"
            file_id += f"**File Type**: `{rep.document.mime_type}`"

        elif rep.photo:
            file_id = f"**File ID**: `{rep.photo.file_id}`"
            file_id += "**File Type**: `photo`"

        elif rep.sticker:
            file_id = f"**Sicker ID**: `{rep.sticker.file_id}`\n"
            if rep.sticker.set_name and rep.sticker.emoji:
                file_id += f"**Sticker Set**: `{rep.sticker.set_name}`\n"
                file_id += f"**Sticker Emoji**: `{rep.sticker.emoji}`\n"
                if rep.sticker.is_animated:
                    file_id += f"**Animated Sticker**: `{rep.sticker.is_animated}`\n"
                else:
                    file_id += "**Animated Sticker**: `False`\n"
            else:
                file_id += "**Sticker Set**: __None__\n"
                file_id += "**Sticker Emoji**: __None__"

        elif rep.video:
            file_id = f"**File ID**: `{rep.video.file_id}`\n"
            file_id += "**File Type**: `video`"

        elif rep.animation:
            file_id = f"**File ID**: `{rep.animation.file_id}`\n"
            file_id += "**File Type**: `GIF`"

        elif rep.voice:
            file_id = f"**File ID**: `{rep.voice.file_id}`\n"
            file_id += "**File Type**: `Voice Note`"

        elif rep.video_note:
            file_id = f"**File ID**: `{rep.animation.file_id}`\n"
            file_id += "**File Type**: `Video Note`"

        elif rep.location:
            file_id = "**Location**:\n"
            file_id += f"**longitude**: `{rep.location.longitude}`\n"
            file_id += f"**latitude**: `{rep.location.latitude}`"

        elif rep.venue:
            file_id = "**Location**:\n"
            file_id += f"**longitude**: `{rep.venue.location.longitude}`\n"
            file_id += f"**latitude**: `{rep.venue.location.latitude}`\n\n"
            file_id += "**Address**:\n"
            file_id += f"**title**: `{rep.venue.title}`\n"
            file_id += f"**detailed**: `{rep.venue.address}`\n\n"

        elif rep.from_user:
            user_id = rep.from_user.id

    if user_id:
        if rep.forward_from:
            user_detail = (
                f"**Forwarded User ID**: `{message.reply_to_message.forward_from.id}`\n"
            )
        else:
            user_detail = f"**User ID**: `{message.reply_to_message.from_user.id}`\n"
        user_detail += f"**Message ID**: `{message.reply_to_message.id}`"
        await message.reply(user_detail)
    elif file_id:
        if rep.forward_from:
            user_detail = (
                f"**Forwarded User ID**: `{message.reply_to_message.forward_from.id}`\n"
            )
        else:
            user_detail = f"**User ID**: `{message.reply_to_message.from_user.id}`\n"
        user_detail += f"**Message ID**: `{message.reply_to_message.id}`\n\n"
        user_detail += file_id
        await message.reply(user_detail, quote=True)

    else:
        await message.reply(f"**Chat ID**: `{message.chat.id}`", quote=True)


# this is for telegraph
@StreamBot.on_message(filters.command("telegraph"))
async def telegraph_upload(bot, message):
    if not (reply_to_message := message.reply_to_message):
        return await message.reply("Reply to any photo or video.")
    file = reply_to_message.photo or reply_to_message.video or None
    if file is None:
        return await message.reply("Invalid media.")
    if file.file_size >= 5242880:
        await message.reply_text(text="Send less than 5MB")
        return
    text = await message.reply_text(text="Processing....", quote=True)
    media = await reply_to_message.download()
    try:
        response = upload_file(media)
    except Exception as e:
        await text.edit_text(text=f"Error - {e}")
        return
    try:
        os.remove(media)
    except:  # noqa: E722
        pass
    await text.edit_text(
        f"<b>❤️ Your Telegram Link Complete 👇</b>\n\n<code>https://telegra.ph/{response[0]}</code></b>"
    )


# this is for GPT codes
@StreamBot.on_message(filters.command(["askgpt", "gpt"]))
async def gpt(app, message: Message):
    text = "".join(message.text.split(" ")[1:])
    if len(text) == 0:
        return await message.reply_text(
            "Cannot reply to empty message.", parse_mode=ParseMode.MARKDOWN
        )
    m = await message.reply_text("Getting Request....", parse_mode=ParseMode.MARKDOWN)
    url = "https://api.safone.dev/chatgpt"
    payloads = {
        "message": text,
        # "version": 3,
        "chat_mode": "assistant",
        "dialog_messages": '[{"bot":"","user":""}]',
    }
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.post(url, json=payloads, headers=headers)
        results = response.json()
        res = results["message"]

        await m.edit_text(f"{res}")
    except Exception as e:
        await m.edit_text(f"Error :-\n{e}")


# this is for  donate
@StreamBot.on_message(filters.command(["donate"]))
async def donate(app, message: Message):
    await message.reply_text(
        text=tamilxd.DONATE_TXT,
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True,
        reply_markup=BUTTON.DONATE_BUTTONS,
        quote=True,
    )


# Auto extraction commands
@StreamBot.on_message(filters.command(["extract", "autoextract"]))
async def extract_toggle(bot, message):
    if not await verify_user(bot, message):
        return
    user_id = message.from_user.id
    auto_extract = await u_db.get_auto_extract(user_id)

    buttons = []
    buttons.append([
        InlineKeyboardButton(
            "✅ Enable Auto Extract" if not auto_extract else "❌ Disable Auto Extract",
            callback_data="toggle_extract"
        )
    ])
    buttons.append([InlineKeyboardButton("Close", callback_data="close")])

    status = "Enabled" if auto_extract else "Disabled"
    await message.reply_text(
        f"<b><u>🔍 AUTO EXTRACTION SETTINGS</u></b>\n\n"
        f"<b>Current Status:</b> {status}\n\n"
        f"<b>📝 What it does:</b>\n"
        f"• Automatically extracts quality (1080p, 720p, 4K, etc.)\n"
        f"• Finds season numbers (S01, S02, etc.)\n"
        f"• Detects episode numbers (E01, E02, etc.)\n"
        f"• Replaces placeholders in your custom caption\n\n"
        f"<b>🎯 Supported placeholders:</b>\n"
        f"<code>{{quality}}</code> - Video quality\n"
        f"<code>{{season}}</code> - Season number\n"
        f"<code>{{episode}}</code> - Episode number",
        disable_web_page_preview=True,
        quote=True,
        reply_markup=InlineKeyboardMarkup(buttons),
    )


# Example caption command
@StreamBot.on_message(filters.command(["examples", "example"]))
async def show_examples(bot, message):
    if not await verify_user(bot, message):
        return
    
    example_text = """<b><u>📝 CAPTION EXAMPLES WITH AUTO EXTRACTION</u></b>

<b>🎬 Example 1:</b>
<code>🎥 {file_name}

📺 Quality: {quality}
🎞️ Season: {season} | Episode: {episode}
📦 Size: {file_size}

📥 Download: {download_link}
🖥️ Stream: {stream_link}</code>

<b>🎬 Example 2:</b>
<code>📁 File: {file_name}
🔍 [{quality}] S{season}E{episode}
📊 Size: {file_size}

⬇️ {download_link}</code>

<b>🎬 Example 3:</b>
<code>🎦 **{file_name}**

🌟 Quality: **{quality}**
📺 Season {season} - Episode {episode}
💾 {file_size}

📱 Watch Online: {stream_link}
💿 Download: {download_link}</code>

<b>💡 Note:</b> These placeholders will be automatically replaced with extracted information from your file names!"""
    
    await message.reply_text(
        example_text,
        disable_web_page_preview=True,
        quote=True,
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("🔍 Configure Auto Extract", callback_data="toggle_extract"),
            InlineKeyboardButton("Close", callback_data="close")
        ]])
    )


# Test extraction command
@StreamBot.on_message(filters.command(["test", "testextract"]))
async def test_extraction(bot, message):
    if not await verify_user(bot, message):
        return
    
    if len(message.command) < 2:
        await message.reply_text(
            "<b>📋 Test Extraction</b>\n\n"
            "<b>Usage:</b> <code>/test filename</code>\n\n"
            "<b>Example:</b> <code>/test Game.of.Thrones.S08E06.1080p.WEB-DL.x264.mkv</code>\n\n"
            "This will show you what quality, season, and episode information can be extracted from the filename.",
            quote=True
        )
        return
    
    # Get filename from command
    filename = " ".join(message.command[1:])
    
    # Import extraction functions
    from MrAKTech.tools.extract_info import extract_quality, extract_season_number, extract_episode_number, extract_combined_info
    
    # Test individual extractions
    quality = extract_quality(filename)
    season = extract_season_number(filename)
    episode = extract_episode_number(filename)
    
    # Test combined extraction (filename only in this case)
    combined_info = extract_combined_info(filename)
    
    result_text = f"""<b><u>🔍 EXTRACTION TEST RESULT</u></b>

<b>📁 Filename:</b> <code>{filename}</code>

<b>📊 Extracted Information:</b>
🎞️ <b>Quality:</b> <code>{quality or 'Not detected'}</code>
📺 <b>Season:</b> <code>{season or 'Not detected'}</code>
🎬 <b>Episode:</b> <code>{episode or 'Not detected'}</code>

<b>🧠 Smart Extraction (Best Result):</b>
🎞️ <b>Final Quality:</b> <code>{combined_info['quality'] or 'Not detected'}</code>
📺 <b>Final Season:</b> <code>{combined_info['season'] or 'Not detected'}</code>
🎬 <b>Final Episode:</b> <code>{combined_info['episode'] or 'Not detected'}</code>

<b>💡 The bot now checks both filename AND original caption to get the most complete information!</b>"""
    
    await message.reply_text(
        result_text,
        disable_web_page_preview=True,
        quote=True,
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("📝 See Examples", callback_data="show_examples"),
            InlineKeyboardButton("Close", callback_data="close")
        ]])
    )


# Linkmode commands
@StreamBot.on_message(filters.command(["linkmode"]))
async def linkmode_toggle(bot, message):
    if not await verify_user(bot, message):
        return
    
    user_id = message.from_user.id
    
    if len(message.command) < 2:
        # Show current status
        linkmode = await u_db.get_linkmode(user_id)
        status = "✅ Enabled" if linkmode else "❌ Disabled"
        
        await message.reply_text(
            f"<b><u>🔗 LINKMODE SETTINGS</u></b>\n\n"
            f"<b>Current Status:</b> {status}\n\n"
            f"<b>📝 Usage:</b>\n"
            f"• <code>/linkmode on</code> - Enable linkmode\n"
            f"• <code>/linkmode off</code> - Disable linkmode\n\n"
            f"<b>🎯 What is Linkmode?</b>\n"
            f"Linkmode allows you to use multiple shortener links and custom captions with advanced placeholders for batch file processing.",
            quote=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("⚙️ Linkmode Settings", callback_data="linkmode_settings"),
                InlineKeyboardButton("Close", callback_data="close")
            ]])
        )
        return
    
    command = message.command[1].lower()
    
    if command == "on":
        await u_db.set_linkmode(user_id, True)
        await u_db.start_file_batch(user_id)  # Start batch mode
        await message.reply_text(
            "🔗 **Linkmode Enabled!**\n\n"
            "You can now:\n"
            "• Send multiple files\n"
            "• Use `/complete` to finish batch\n"
            "• Configure shortlinks and captions\n\n"
            "Use `/linkmode_help` for more information.",
            quote=True
        )
    elif command == "off":
        await u_db.set_linkmode(user_id, False)
        await u_db.clear_file_batch(user_id)  # Clear batch mode
        await message.reply_text(
            "❌ **Linkmode Disabled!**\n\n"
            "Switched back to normal mode.",
            quote=True
        )
    else:
        await message.reply_text(
            "❌ Invalid command. Use:\n"
            "• `/linkmode on` - Enable\n"
            "• `/linkmode off` - Disable",
            quote=True
        )


@StreamBot.on_message(filters.command(["complete"]))
async def complete_batch(bot, message):
    if not await verify_user(bot, message):
        return
    
    user_id = message.from_user.id
    linkmode = await u_db.get_linkmode(user_id)
    
    if not linkmode:
        await message.reply_text(
            "❌ Linkmode is not enabled. Use `/linkmode on` first.",
            quote=True
        )
        return
    
    file_batch = await u_db.get_file_batch(user_id)
    
    if not file_batch:
        await message.reply_text(
            "❌ No files in batch. Send some files first!",
            quote=True
        )
        return
    
    # Process the batch with linkmode caption and shortlinks
    await process_linkmode_batch(bot, message, file_batch)
    
    # Clear the batch
    await u_db.clear_file_batch(user_id)
    await u_db.start_file_batch(user_id)  # Restart for next batch


# Shortlink commands
@StreamBot.on_message(filters.command(["shortlink1", "shortlink2", "shortlink3"]))
async def set_shortlink(bot, message):
    if not await verify_user(bot, message):
        return
    
    user_id = message.from_user.id
    command = message.command[0]
    shortlink_num = command[-1]  # Get the number (1, 2, or 3)
    
    if len(message.command) < 2:
        # Show current shortlink
        if shortlink_num == "1":
            url, api = await u_db.get_shortlink1(user_id)
        elif shortlink_num == "2":
            url, api = await u_db.get_shortlink2(user_id)
        else:
            url, api = await u_db.get_shortlink3(user_id)
        
        status = f"URL: {url or 'Not set'}\nAPI: {api or 'Not set'}"
        
        await message.reply_text(
            f"<b>🔗 Shortlink {shortlink_num} Settings</b>\n\n"
            f"{status}\n\n"
            f"<b>Usage:</b>\n"
            f"<code>/{command} {{url}} {{api}}</code>\n"
            f"<code>/{command} off</code> - Disable",
            quote=True
        )
        return
    
    if message.command[1].lower() == "off":
        # Disable shortlink
        if shortlink_num == "1":
            await u_db.delete_shortlink1(user_id)
        elif shortlink_num == "2":
            await u_db.delete_shortlink2(user_id)
        else:
            await u_db.delete_shortlink3(user_id)
        
        await message.reply_text(
            f"✅ Shortlink {shortlink_num} disabled!",
            quote=True
        )
        return
    
    if len(message.command) < 3:
        await message.reply_text(
            f"❌ Invalid format. Use:\n"
            f"<code>/{command} {{url}} {{api}}</code>\n"
            f"Example: <code>/{command} short.com your_api_key</code>",
            quote=True
        )
        return
    
    url = message.command[1]
    api = message.command[2]
    
    # Set the shortlink
    if shortlink_num == "1":
        await u_db.set_shortlink1(user_id, url, api)
    elif shortlink_num == "2":
        await u_db.set_shortlink2(user_id, url, api)
    else:
        await u_db.set_shortlink3(user_id, url, api)
    
    await message.reply_text(
        f"✅ Shortlink {shortlink_num} set successfully!\n"
        f"URL: {url}\nAPI: {api}",
        quote=True
    )


@StreamBot.on_message(filters.command(["list_shortlinks"]))
async def list_shortlinks(bot, message):
    if not await verify_user(bot, message):
        return
    
    user_id = message.from_user.id
    
    url1, api1 = await u_db.get_shortlink1(user_id)
    url2, api2 = await u_db.get_shortlink2(user_id)
    url3, api3 = await u_db.get_shortlink3(user_id)
    
    text = "<b><u>🔗 YOUR SHORTLINKS</u></b>\n\n"
    
    # Shortlink 1
    if url1 and api1:
        text += f"<b>🔗 Shortlink 1:</b> ✅ Active\n"
        text += f"URL: <code>{url1}</code>\n"
        text += f"API: <code>{api1}</code>\n\n"
    else:
        text += f"<b>🔗 Shortlink 1:</b> ❌ Not set\n\n"
    
    # Shortlink 2
    if url2 and api2:
        text += f"<b>🔗 Shortlink 2:</b> ✅ Active\n"
        text += f"URL: <code>{url2}</code>\n"
        text += f"API: <code>{api2}</code>\n\n"
    else:
        text += f"<b>🔗 Shortlink 2:</b> ❌ Not set\n\n"
    
    # Shortlink 3
    if url3 and api3:
        text += f"<b>🔗 Shortlink 3:</b> ✅ Active\n"
        text += f"URL: <code>{url3}</code>\n"
        text += f"API: <code>{api3}</code>\n\n"
    else:
        text += f"<b>🔗 Shortlink 3:</b> ❌ Not set\n\n"
    
    text += "<b>💡 Commands:</b>\n"
    text += "• <code>/shortlink1 {url} {api}</code>\n"
    text += "• <code>/shortlink2 {url} {api}</code>\n"
    text += "• <code>/shortlink3 {url} {api}</code>\n"
    text += "• <code>/delete_shortlink1</code>\n"
    text += "• <code>/delete_shortlink2</code>\n"
    text += "• <code>/delete_shortlink3</code>"
    
    await message.reply_text(text, quote=True)


@StreamBot.on_message(filters.command(["delete_shortlink1", "delete_shortlink2", "delete_shortlink3"]))
async def delete_shortlink(bot, message):
    if not await verify_user(bot, message):
        return
    
    user_id = message.from_user.id
    command = message.command[0]
    shortlink_num = command[-1]  # Get the number (1, 2, or 3)
    
    if shortlink_num == "1":
        await u_db.delete_shortlink1(user_id)
    elif shortlink_num == "2":
        await u_db.delete_shortlink2(user_id)
    else:
        await u_db.delete_shortlink3(user_id)
    
    await message.reply_text(
        f"✅ Shortlink {shortlink_num} deleted successfully!",
        quote=True
    )


@StreamBot.on_message(filters.command(["setlinkmodecaption"]))
async def set_linkmode_caption_menu(bot, message):
    if not await verify_user(bot, message):
        return
    
    buttons = [
        [
            InlineKeyboardButton("📝 Caption 1", callback_data="set_linkmode_caption_1"),
            InlineKeyboardButton("📝 Caption 2", callback_data="set_linkmode_caption_2"),
            InlineKeyboardButton("📝 Caption 3", callback_data="set_linkmode_caption_3")
        ],
        [
            InlineKeyboardButton("📋 View Captions", callback_data="view_linkmode_captions"),
            InlineKeyboardButton("🗑️ Delete Captions", callback_data="delete_linkmode_captions_menu")
        ],
        [
            InlineKeyboardButton("📝 Example 1", callback_data="set_example_caption_1"),
            InlineKeyboardButton("📝 Example 2", callback_data="set_example_caption_2"),
            InlineKeyboardButton("📝 Example 3", callback_data="set_example_caption_3")
        ],
        [
            InlineKeyboardButton("Close", callback_data="close")
        ]
    ]
    
    await message.reply_text(
        "<b><u>📝 LINKMODE CAPTION SETTINGS</u></b>\n\n"
        "Choose an option to manage your linkmode captions:\n\n"
        "<b>💡 Examples:</b> Pre-made caption templates you can use",
        quote=True,
        reply_markup=InlineKeyboardMarkup(buttons)
    )


@StreamBot.on_message(filters.command(["linkmode_help"]))
async def linkmode_help(bot, message):
    if not await verify_user(bot, message):
        return
    
    await message.reply_text(tamilxd.LINKMODE_HELP_TXT, quote=True)


# Helper function to process linkmode batch
async def process_linkmode_batch(bot, message, file_batch):
    user_id = message.from_user.id
    user = await u_db.get_user(user_id)
    
    # Get active linkmode caption
    active_caption_num = await u_db.get_active_linkmode_caption(user_id)
    
    if active_caption_num == 1:
        caption_template = await u_db.get_linkmode_caption1(user_id)
    elif active_caption_num == 2:
        caption_template = await u_db.get_linkmode_caption2(user_id)
    else:
        caption_template = await u_db.get_linkmode_caption3(user_id)
    
    if not caption_template:
        caption_template = user["caption"]  # Fallback to regular caption
    
    # Get first and last file info
    first_file = file_batch[0] if file_batch else {}
    last_file = file_batch[-1] if file_batch else {}
    
    filenamefirst = first_file.get("file_name", "")
    filenamelast = last_file.get("file_name", "")
    filecaptionfirst = first_file.get("caption", "")
    filecaptionlast = last_file.get("caption", "")
    
    # Process each file in the batch
    for file_info in file_batch:
        await process_single_file_linkmode(
            bot, message, file_info, caption_template, user,
            filenamefirst, filenamelast, filecaptionfirst, filecaptionlast
        )
    
    await message.reply_text(
        f"✅ **Batch Complete!**\n\n"
        f"Processed {len(file_batch)} files with linkmode.",
        quote=True
    )


async def process_single_file_linkmode(bot, message, file_info, caption_template, user, 
                                     filenamefirst, filenamelast, filecaptionfirst, filecaptionlast):
    from MrAKTech.tools.utils_bot import short_link
    from MrAKTech.tools.human_readable import humanbytes
    from MrAKTech.tools.extract_info import smart_replace_placeholders_in_caption, create_safe_format_dict
    import random
    from MrAKTech.config import Domain
    from shortzy import Shortzy
    
    user_id = message.from_user.id
    
    # Get shortlink configurations
    url1, api1 = await u_db.get_shortlink1(user_id)
    url2, api2 = await u_db.get_shortlink2(user_id)
    url3, api3 = await u_db.get_shortlink3(user_id)
    
    # Create base links
    log_msg_id = file_info["log_msg_id"]
    file_hash = file_info["file_hash"]
    
    storage_link = f"https://telegram.me/{Telegram.FILE_STORE_BOT_USERNAME}?start=download_{log_msg_id}"
    stream_link = f"{random.choice(Domain.CLOUDFLARE_URLS)}watch/{str(log_msg_id)}?hash={file_hash}"
    download_link = f"{random.choice(Domain.CLOUDFLARE_URLS)}dl/{str(log_msg_id)}?hash={file_hash}"
    
    # Create shortened links for each shortener
    stream_link_1 = download_link_1 = storage_link_1 = ""
    stream_link_2 = download_link_2 = storage_link_2 = ""
    stream_link_3 = download_link_3 = storage_link_3 = ""
    
    if url1 and api1:
        try:
            shortzy1 = Shortzy(api_key=api1, base_site=url1)
            stream_link_1 = await shortzy1.convert(stream_link)
            download_link_1 = await shortzy1.convert(download_link)
            storage_link_1 = await shortzy1.convert(storage_link)
        except:
            pass
    
    if url2 and api2:
        try:
            shortzy2 = Shortzy(api_key=api2, base_site=url2)
            stream_link_2 = await shortzy2.convert(stream_link)
            download_link_2 = await shortzy2.convert(download_link)
            storage_link_2 = await shortzy2.convert(storage_link)
        except:
            pass
    
    if url3 and api3:
        try:
            shortzy3 = Shortzy(api_key=api3, base_site=url3)
            stream_link_3 = await shortzy3.convert(stream_link)
            download_link_3 = await shortzy3.convert(download_link)
            storage_link_3 = await shortzy3.convert(storage_link)
        except:
            pass
    
    # Regular shortened links (using user's main shortener)
    stream_link_short = await short_link(stream_link, user)
    download_link_short = await short_link(download_link, user)
    storage_link_short = await short_link(storage_link, user)
    
    # Create format dictionary with all placeholders
    format_dict = {
        "file_name": file_info.get("file_name", ""),
        "caption": file_info.get("caption", ""),
        "file_size": file_info.get("file_size", ""),
        "download_link": download_link_short,
        "stream_link": stream_link_short,
        "storage_link": storage_link_short,
        "stream_link_1": stream_link_1,
        "download_link_1": download_link_1,
        "storage_link_1": storage_link_1,
        "stream_link_2": stream_link_2,
        "download_link_2": download_link_2,
        "storage_link_2": storage_link_2,
        "stream_link_3": stream_link_3,
        "download_link_3": download_link_3,
        "storage_link_3": storage_link_3,
        "filenamefirst": filenamefirst,
        "filenamelast": filenamelast,
        "filecaptionfirst": filecaptionfirst,
        "filecaptionlast": filecaptionlast,
    }
    
    # Apply smart replacement for auto-extraction
    auto_extract = user.get("auto_extract", True)
    if auto_extract:
        caption_template = smart_replace_placeholders_in_caption(
            caption_template, 
            file_info.get("file_name", ""), 
            file_info.get("caption", "")
        )
    
    # Create safe format dictionary
    safe_format_dict = create_safe_format_dict(format_dict, 
                                               file_info.get("file_name", ""), 
                                               file_info.get("caption", ""))
    
    # Update with linkmode specific placeholders
    safe_format_dict.update({
        "stream_link_1": stream_link_1,
        "download_link_1": download_link_1,
        "storage_link_1": storage_link_1,
        "stream_link_2": stream_link_2,
        "download_link_2": download_link_2,
        "storage_link_2": storage_link_2,
        "stream_link_3": stream_link_3,
        "download_link_3": download_link_3,
        "storage_link_3": storage_link_3,
        "filenamefirst": filenamefirst,
        "filenamelast": filenamelast,
        "filecaptionfirst": filecaptionfirst,
        "filecaptionlast": filecaptionlast,
    })
    
    try:
        final_caption = caption_template.format(**safe_format_dict)
        
        await message.reply_text(
            text=final_caption,
            quote=False,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Dᴏᴡɴʟᴏᴀᴅ ɴᴏᴡ 📥", url=stream_link_short)]]
            ),
        )
    except Exception as e:
        await message.reply_text(
            f"❌ Error formatting caption: {str(e)}\n\n"
            f"File: {file_info.get('file_name', 'Unknown')}\n"
            f"Download: {download_link_short}",
            quote=False
        )
