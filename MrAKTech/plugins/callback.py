import asyncio
import time
import datetime
import shutil
import psutil
from shortzy import Shortzy
from validators import domain

from pyrogram import enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from MrAKTech import StreamBot, work_loads, multi_clients, cdn_count
from MrAKTech.config import Telegram
from MrAKTech.database.u_db import u_db
from MrAKTech.tools.txt import tamilxd, BUTTON
from MrAKTech.tools.utils_bot import readable_time, get_readable_file_size, temp, is_check_admin

@StreamBot.on_callback_query()
async def cb_handler(bot, query: CallbackQuery):
    data = query.data
    user_id = query.from_user.id
    userxdb = await u_db.get_user_details(user_id)
    # Callback started
    if data == "start":
        await query.message.edit_text(
            text=(tamilxd.START_TXT.format(query.from_user.mention)),
            disable_web_page_preview=True,
            reply_markup=BUTTON.START_BUTTONS
        )

    elif data == "help":
        await query.message.edit_text(
            text=tamilxd.HELP_TXT,
            disable_web_page_preview=True,
            reply_markup=BUTTON.HELP_BUTTONS
        )

    elif data == "owner":
        await query.message.edit_text(
            text=tamilxd.OWNER_INFO,
            disable_web_page_preview=True,
            reply_markup=BUTTON.OWNER_BUTTONS
        )
    elif data == "about":
        await query.message.edit_text(
            text=tamilxd.ABOUT_TXT,
            disable_web_page_preview=True,
            reply_markup=BUTTON.ABOUT_BUTTONS
        )

    elif data == "dev":
        m=await query.message.reply_sticker("CAACAgIAAxkBAAEJ8bxk0L2LAm0P4AABCIUXG6g7V03RTTQAAoAOAALUdQlKzIMOAcx1iKkwBA")
        await asyncio.sleep(3)
        await m.delete()
        caption = tamilxd.DEV_TXT
        tamil=await query.message.reply_photo(
            photo="https://telegra.ph/file/4e48e88fe9811add5fb22.jpg",
            caption=caption,
            reply_markup=InlineKeyboardMarkup([[
               #InlineKeyboardButton("♙ ʜᴏᴍᴇ", callback_data = "start"),
               InlineKeyboardButton("✗ Close", callback_data = "close")
               ]]
            )
        )
        await asyncio.sleep(1600)
        await tamil.delete()
        await query.message.delete()

    elif data == "source":
        m=await query.message.reply_sticker("CAACAgUAAxkBAAEBlVBkoEL0LKGBhqNxTtVM_Ti0QHnO_AAC5wQAAo6i-VUZIF0fRfvjmx4E")
        await asyncio.sleep(2)
        await m.delete()
        tamil=await query.message.reply_photo(
            photo="https://graph.org/file/306e4f62551e994ee6792.jpg",
            caption=tamilxd.SOURCE_TXT,
            reply_markup=BUTTON.SOURCE_BUTTONS
        )
        await asyncio.sleep(10)
        await tamil.delete()
        await query.message.delete()

    elif data == "don":
        m=await query.message.reply_sticker("CAACAgUAAxkBAAEBlVBkoEL0LKGBhqNxTtVM_Ti0QHnO_AAC5wQAAo6i-VUZIF0fRfvjmx4E")
        await asyncio.sleep(3)
        await m.delete()
        tamil=await query.message.reply_photo(
            photo="https://telegra.ph/file/d6e78fb5f4288e91be748.jpg",
            caption=(tamilxd.DONATE_TXT),
            reply_markup=BUTTON.DONATE_BUTTONS,
        )
        await asyncio.sleep(1800)
        await tamil.delete()
        await query.message.delete()

    ########## USERS MAIN BOT DETAILS START ########

    elif data in ['settings', 'toggle_mode', 'storage_mode']:
        mode = await u_db.get_uploadmode(user_id)
        # modex = await u_db.get_storagemode(user_id)
        if data == "toggle_mode":
            if not mode:
                mode = "links"
            elif mode == "links":
                mode = "files"
            else:
                # mode = None
                mode = "links"
            await u_db.change_uploadmode(user_id, mode)
        # if data == "storage_mode":
        #     if not modex:
        #         modex = "Off"
        #     elif modex == "Off":
        #         modex = "On"
        #     else:
        #      #mode = None
        #         modex = "Off"
        #     await u_db.change_storagemode(user_id, modex)

        # button = [[
        #     InlineKeyboardButton(
        #         "✅ Custom caption" if userxdb['caption'] is not None else "📝 Custom caption",
        #         callback_data="custom_caption"
        #     )
        #     ],[
        #     InlineKeyboardButton(
        #         "✅ Custom shortner" if userxdb['shortener_url'] and userxdb['shortener_api'] is not None else "🖼️ Custom shortner",
        #         callback_data="custom_shortner"
        #     )
        #     ],[
        #     InlineKeyboardButton('📤 Upload mode', callback_data="toggle_mode"),
        #     InlineKeyboardButton(mode if mode else "Links", callback_data="toggle_mode")
        #     ],[
        #     InlineKeyboardButton('🛠️ Reset settings', callback_data="reset_setting"),
        #     ], [
        #     InlineKeyboardButton('Close ✗', callback_data="close")
        #     ]]

        #
        buttons = []
        buttons.append([InlineKeyboardButton(
            "✅ Custom Caption" if userxdb['caption'] != tamilxd.STREAM_MSG_TXT else "📝 Custom Caption",
            callback_data="custom_caption"
        )])
        buttons.append([InlineKeyboardButton(
            "✅ Custom Shortner" if userxdb['shortener_url'] and userxdb[
                'shortener_api'] is not None else "🖼️ Custom Shortner",
            callback_data="custom_shortner"
        )])
        auto_extract = userxdb.get('auto_extract', True)
        buttons.append([InlineKeyboardButton(
            "✅ Auto Extract" if auto_extract else "❌ Auto Extract",
            callback_data="toggle_extract"
        )])
        linkmode = userxdb.get('linkmode', False)
        buttons.append([InlineKeyboardButton(
            "✅ Linkmode" if linkmode else "❌ Linkmode",
            callback_data="linkmode_settings"
        )])
        buttons.append([InlineKeyboardButton('📤 Upload Mode', callback_data="toggle_mode"),
                        InlineKeyboardButton(mode if mode else "Links", callback_data="toggle_mode")])
        if await u_db.is_settings(user_id):
            buttons.append([InlineKeyboardButton('🛠️ Reset Settings', callback_data="reset_setting")])
        buttons.append([InlineKeyboardButton('Close', callback_data="close")])
        await query.message.edit_text(
            text=tamilxd.SETTINGS_TXT.format(CAPTION="✅ Exists" if userxdb["caption"] is not None else "❌ Not Exists",
                                             URLX=userxdb["shortener_url"] if userxdb["shortener_url"] is not None else "❌ Not Exists",
                                             APIX=userxdb["shortener_api"] if userxdb["shortener_api"] is not None else "❌ Not Exists",
                                             STORAGEX=userxdb["storage"],
                                             METHODX=userxdb["method"],
                                             AUTO_EXTRACT="✅ Enabled" if userxdb.get("auto_extract", True) else "❌ Disabled"),
            reply_markup=InlineKeyboardMarkup(buttons),
            disable_web_page_preview=True)

    elif data == "reset_setting":
        await query.message.edit_text(
            text=tamilxd.RESET_SETTINGS,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton('Yes', callback_data="reset_settings"),
                InlineKeyboardButton('No', callback_data="settings"),
            ]]))

    elif data == "reset_settings":
        await u_db.reset_settings(user_id)
        await query.answer("Successfully settings resetted.", show_alert=True)
        buttons = []
        buttons.append([InlineKeyboardButton("📝 Custom caption", callback_data="custom_caption")])
        buttons.append([InlineKeyboardButton("🖼️ Custom shortner", callback_data="custom_shortner")])
        buttons.append([InlineKeyboardButton("✅ Auto Extract", callback_data="toggle_extract")])
        buttons.append([InlineKeyboardButton("❌ Linkmode", callback_data="linkmode_settings")])
        buttons.append([InlineKeyboardButton('📤 Upload mode', callback_data="toggle_mode"),
                        InlineKeyboardButton("Links", callback_data="toggle_mode")])
        buttons.append([InlineKeyboardButton('Close', callback_data="close")])
        await query.message.edit_text(
            text=tamilxd.SETTINGS_TXT.format(CAPTION="❌ Not Exists",
                                             URLX="❌ Not Exists",
                                             APIX="❌ Not Exists",
                                             METHODX="Links",
                                             AUTO_EXTRACT="✅ Enabled"),
            reply_markup=InlineKeyboardMarkup(buttons),
            disable_web_page_preview=True)

    elif data == "custom_caption":
        buttons = []
        if userxdb['caption'] is not None:
            buttons.append([InlineKeyboardButton('Show caption', callback_data="show_caption")])
            buttons.append([InlineKeyboardButton('Default caption', callback_data="delete_caption"),
                            InlineKeyboardButton('Change caption', callback_data="add_caption")])
        else:
            buttons.append([InlineKeyboardButton('Set caption', callback_data="add_caption")])
        buttons.append([InlineKeyboardButton('≺≺ Back', callback_data="settings"),
                        InlineKeyboardButton('Close', callback_data="close")])
        await query.message.edit_text(
            text=tamilxd.CUSTOM_CAPTION_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons))

    elif data == "custom_shortner":
        buttons = []
        if userxdb['shortener_url'] and userxdb['shortener_api'] is not None:
            buttons.append([InlineKeyboardButton('Show shortner', callback_data="show_shortner")])
            buttons.append([InlineKeyboardButton('Delete shortner', callback_data="delete_shortner"),
                            InlineKeyboardButton('Change shortner', callback_data="add_shortner")])
        else:
            buttons.append([InlineKeyboardButton('Set shortner', callback_data="add_shortner")])
        buttons.append([InlineKeyboardButton('≺≺ Back', callback_data="settings"),
                        InlineKeyboardButton('Close', callback_data="close")])
        await query.message.edit_text(
            text=tamilxd.CUSTOM_SHORTNER_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons))

    elif data == "add_caption":
        await query.message.delete()
        try:
            tamil = await bot.send_message(query.message.chat.id, "Send your custom caption\n/cancel - <code>Cancel this process</code>")
            caption = await bot.listen(chat_id=user_id, timeout=300)
            if caption.text == "/cancel":
                await caption.delete()
                return await tamil.edit_text("<b>Your process is canceled!</b>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('≺≺ Back', callback_data="custom_caption")]]))
            try:
                caption.text.format(file_name='', file_size='', caption='', download_link='', stream_link='', storage_link='', quality='', season='', episode='')
            except KeyError as e:
                await caption.delete()
                return await tamil.edit_text(f"<b><u>Wrong filling</u> \n\n<code>{e}</code> \n\n Used in your caption. change it.</b>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('≺≺ Back', callback_data="custom_caption")]]))
            await u_db.set_caption(user_id, caption.text)
            await caption.delete()
            await tamil.edit_text("<b>Successfully added your custon caption!...</b>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('≺≺ Back', callback_data="custom_caption")]]))
        except asyncio.exceptions.TimeoutError:
            await tamil.edit_text('Process has been automatically cancelled.', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('≺≺ Back', callback_data="custom_caption")]]))

    elif data == "add_shortner":
        await query.message.delete()
        try:
            tamil = await bot.send_message(query.message.chat.id, "<b>Please provide your custom shortener URL\nEg: <code>dalink.in</code>\n/cancel - <code>Cancel this process</code></b>")
            url_input = await bot.listen(chat_id=user_id, timeout=300)
            if url_input.text == "/cancel":
                await url_input.delete()
                return await tamil.edit_text("<b>Your process is canceled!</b>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('≺≺ Back', callback_data="custom_shortner")]]))
            elif not domain(url_input.text):
                await url_input.delete()
                return await tamil.edit_text("<b>Invalid domain format. please provide a valid domain.</b>", disable_web_page_preview=True, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('≺≺ Back', callback_data="custom_shortner")]]))
            try:
                # await u_db.set_shortner_url(user_id, url_input.text)
                await url_input.delete()
                await tamil.delete()
                tamil1 = await bot.send_message(query.message.chat.id, f"<b> https://{url_input.text}/member/tools/quick \n\nPlease provide your custom shortener API \n Eg: <code>88f4e0fc522facab5fef40d69f4114c260facc9b</code></b>")
                api = await bot.listen(chat_id=user_id)
                try:
                    shortzy = Shortzy(api_key=api.text, base_site=url_input.text)
                    link = Telegram.MAIN
                    await shortzy.convert(link)
                except Exception as e:
                    return await tamil1.edit_text(f"Your shortener API or URL is invalid, please check again! {e}", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('≺≺ Back', callback_data="custom_shortner")]]))
                await u_db.set_shortner_url(user_id, url_input.text)
                await u_db.set_shortner_api(user_id, api.text)
                await api.delete()
                await tamil1.edit_text("<b>Successfully added your custon shortener!...</b>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('≺≺ Back', callback_data="custom_shortner")]]))
            except Exception as e:
                print(f"Error fetching user: {e}")
            return
        except asyncio.exceptions.TimeoutError:
            await tamil.edit_text('Process has been automatically cancelled.', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('≺≺ Back', callback_data="custom_shortner")]]))

    elif data =="show_caption":
        if len(userxdb['caption']) > 170:
            await query.message.edit_text(
                text=userxdb['caption'],
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('≺≺ Back', callback_data="custom_caption")]])
            )
        else:
            await query.answer(f"Your custom caption:\n\n{userxdb['caption']}", show_alert=True)

    elif data == "delete_caption":
        if not userxdb['caption']:
            return await query.answer("Nothing will found to delete.", show_alert=True)
        await u_db.set_caption(query.from_user.id, tamilxd.STREAM_MSG_TXT)
        return await query.answer("Caption removed suppessfully!", show_alert=True)

    elif data == "toggle_extract":
        user_id = query.from_user.id
        auto_extract = await u_db.get_auto_extract(user_id)
        new_status = not auto_extract
        await u_db.set_auto_extract(user_id, new_status)
        
        status_text = "✅ Enabled" if new_status else "❌ Disabled"
        await query.answer(f"Auto Extract {status_text}!", show_alert=True)
        
        buttons = []
        buttons.append([
            InlineKeyboardButton(
                "❌ Disable Auto Extract" if new_status else "✅ Enable Auto Extract",
                callback_data="toggle_extract"
            )
        ])
        buttons.append([InlineKeyboardButton("Close", callback_data="close")])

        await query.message.edit_text(
            f"<b><u>🔍 AUTO EXTRACTION SETTINGS</u></b>\n\n"
            f"<b>Current Status:</b> {status_text}\n\n"
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
            reply_markup=InlineKeyboardMarkup(buttons),
        )

    # Linkmode callbacks
    elif data == "linkmode_settings":
        user_id = query.from_user.id
        linkmode = await u_db.get_linkmode(user_id)
        
        buttons = [
            [
                InlineKeyboardButton(
                    "❌ Disable Linkmode" if linkmode else "✅ Enable Linkmode",
                    callback_data="toggle_linkmode"
                )
            ],
            [
                InlineKeyboardButton("🔗 Manage Shortlinks", callback_data="manage_shortlinks"),
                InlineKeyboardButton("📝 Manage Captions", callback_data="manage_linkmode_captions")
            ],
            [
                InlineKeyboardButton("≺≺ Back", callback_data="settings"),
                InlineKeyboardButton("Close", callback_data="close")
            ]
        ]
        
        status = "✅ Enabled" if linkmode else "❌ Disabled"
        await query.message.edit_text(
            f"<b><u>🔗 LINKMODE SETTINGS</u></b>\n\n"
            f"<b>Current Status:</b> {status}\n\n"
            f"<b>🎯 Features:</b>\n"
            f"• Multiple shortener links support\n"
            f"• Advanced caption templates\n"
            f"• Batch file processing\n"
            f"• Special placeholders\n\n"
            f"<b>💡 Use /linkmode_help for detailed guide</b>",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons)
        )

    elif data == "toggle_linkmode":
        user_id = query.from_user.id
        linkmode = await u_db.get_linkmode(user_id)
        new_status = not linkmode
        await u_db.set_linkmode(user_id, new_status)
        
        if new_status:
            await u_db.start_file_batch(user_id)
        else:
            await u_db.clear_file_batch(user_id)
        
        status_text = "✅ Enabled" if new_status else "❌ Disabled"
        await query.answer(f"Linkmode {status_text}!", show_alert=True)
        
        # Refresh the linkmode settings page
        await query.message.edit_text("Loading...", reply_markup=None)
        
        buttons = [
            [
                InlineKeyboardButton(
                    "❌ Disable Linkmode" if new_status else "✅ Enable Linkmode",
                    callback_data="toggle_linkmode"
                )
            ],
            [
                InlineKeyboardButton("🔗 Manage Shortlinks", callback_data="manage_shortlinks"),
                InlineKeyboardButton("📝 Manage Captions", callback_data="manage_linkmode_captions")
            ],
            [
                InlineKeyboardButton("≺≺ Back", callback_data="settings"),
                InlineKeyboardButton("Close", callback_data="close")
            ]
        ]
        
        await query.message.edit_text(
            f"<b><u>🔗 LINKMODE SETTINGS</u></b>\n\n"
            f"<b>Current Status:</b> {status_text}\n\n"
            f"<b>🎯 Features:</b>\n"
            f"• Multiple shortener links support\n"
            f"• Advanced caption templates\n"
            f"• Batch file processing\n"
            f"• Special placeholders\n\n"
            f"<b>💡 Use /linkmode_help for detailed guide</b>",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons)
        )

    elif data == "manage_shortlinks":
        user_id = query.from_user.id
        
        url1, api1 = await u_db.get_shortlink1(user_id)
        url2, api2 = await u_db.get_shortlink2(user_id)
        url3, api3 = await u_db.get_shortlink3(user_id)
        
        buttons = [
            [
                InlineKeyboardButton(
                    f"🔗 Shortlink 1 {'✅' if url1 and api1 else '❌'}",
                    callback_data="edit_shortlink_1"
                )
            ],
            [
                InlineKeyboardButton(
                    f"🔗 Shortlink 2 {'✅' if url2 and api2 else '❌'}",
                    callback_data="edit_shortlink_2"
                )
            ],
            [
                InlineKeyboardButton(
                    f"🔗 Shortlink 3 {'✅' if url3 and api3 else '❌'}",
                    callback_data="edit_shortlink_3"
                )
            ],
            [
                InlineKeyboardButton("≺≺ Back", callback_data="linkmode_settings"),
                InlineKeyboardButton("Close", callback_data="close")
            ]
        ]
        
        text = "<b><u>🔗 MANAGE SHORTLINKS</u></b>\n\n"
        text += f"<b>Shortlink 1:</b> {'✅ Active' if url1 and api1 else '❌ Not set'}\n"
        if url1 and api1:
            text += f"URL: <code>{url1}</code>\n\n"
        else:
            text += "\n"
        
        text += f"<b>Shortlink 2:</b> {'✅ Active' if url2 and api2 else '❌ Not set'}\n"
        if url2 and api2:
            text += f"URL: <code>{url2}</code>\n\n"
        else:
            text += "\n"
        
        text += f"<b>Shortlink 3:</b> {'✅ Active' if url3 and api3 else '❌ Not set'}\n"
        if url3 and api3:
            text += f"URL: <code>{url3}</code>\n\n"
        else:
            text += "\n"
        
        text += "<b>💡 Click on a shortlink to configure it</b>"
        
        await query.message.edit_text(
            text,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons)
        )

    elif data.startswith("edit_shortlink_"):
        shortlink_num = data.split("_")[-1]
        user_id = query.from_user.id
        
        if shortlink_num == "1":
            url, api = await u_db.get_shortlink1(user_id)
        elif shortlink_num == "2":
            url, api = await u_db.get_shortlink2(user_id)
        else:
            url, api = await u_db.get_shortlink3(user_id)
        
        buttons = []
        if url and api:
            buttons.append([
                InlineKeyboardButton("🗑️ Delete Shortlink", callback_data=f"delete_shortlink_{shortlink_num}")
            ])
        buttons.append([
            InlineKeyboardButton("✏️ Set/Change Shortlink", callback_data=f"set_shortlink_{shortlink_num}")
        ])
        buttons.append([
            InlineKeyboardButton("≺≺ Back", callback_data="manage_shortlinks"),
            InlineKeyboardButton("Close", callback_data="close")
        ])
        
        status = f"URL: {url or 'Not set'}\nAPI: {'Set' if api else 'Not set'}"
        
        await query.message.edit_text(
            f"<b><u>🔗 SHORTLINK {shortlink_num} SETTINGS</u></b>\n\n"
            f"<b>Current Status:</b>\n{status}\n\n"
            f"<b>💡 Commands:</b>\n"
            f"<code>/shortlink{shortlink_num} {{url}} {{api}}</code>\n"
            f"<code>/shortlink{shortlink_num} off</code>",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons)
        )

    elif data.startswith("set_shortlink_"):
        shortlink_num = data.split("_")[-1]
        await query.message.delete()
        
        try:
            tamil = await bot.send_message(
                query.message.chat.id,
                f"<b>Please provide your shortener URL for Shortlink {shortlink_num}\n"
                f"Eg: <code>short.com</code>\n"
                f"/cancel - Cancel this process</b>"
            )
            url_input = await bot.listen(chat_id=user_id, timeout=300)
            
            if url_input.text == "/cancel":
                await url_input.delete()
                return await tamil.edit_text(
                    "<b>Process canceled!</b>",
                    reply_markup=InlineKeyboardMarkup([[
                        InlineKeyboardButton('≺≺ Back', callback_data=f"edit_shortlink_{shortlink_num}")
                    ]])
                )
            
            if not domain(url_input.text):
                await url_input.delete()
                return await tamil.edit_text(
                    "<b>Invalid domain format. Please provide a valid domain.</b>",
                    reply_markup=InlineKeyboardMarkup([[
                        InlineKeyboardButton('≺≺ Back', callback_data=f"edit_shortlink_{shortlink_num}")
                    ]])
                )
            
            await url_input.delete()
            await tamil.delete()
            
            tamil1 = await bot.send_message(
                query.message.chat.id,
                f"<b>Please provide your API key for {url_input.text}\n"
                f"Eg: <code>88f4e0fc522facab5fef40d69f4114c260facc9b</code>\n"
                f"/cancel - Cancel this process</b>"
            )
            api_input = await bot.listen(chat_id=user_id, timeout=300)
            
            if api_input.text == "/cancel":
                await api_input.delete()
                return await tamil1.edit_text(
                    "<b>Process canceled!</b>",
                    reply_markup=InlineKeyboardMarkup([[
                        InlineKeyboardButton('≺≺ Back', callback_data=f"edit_shortlink_{shortlink_num}")
                    ]])
                )
            
            try:
                shortzy = Shortzy(api_key=api_input.text, base_site=url_input.text)
                test_link = "https://google.com"
                await shortzy.convert(test_link)
            except Exception as e:
                await api_input.delete()
                return await tamil1.edit_text(
                    f"<b>Your shortener API or URL is invalid!\nError: {e}</b>",
                    reply_markup=InlineKeyboardMarkup([[
                        InlineKeyboardButton('≺≺ Back', callback_data=f"edit_shortlink_{shortlink_num}")
                    ]])
                )
            
            # Save the shortlink
            if shortlink_num == "1":
                await u_db.set_shortlink1(user_id, url_input.text, api_input.text)
            elif shortlink_num == "2":
                await u_db.set_shortlink2(user_id, url_input.text, api_input.text)
            else:
                await u_db.set_shortlink3(user_id, url_input.text, api_input.text)
            
            await api_input.delete()
            await tamil1.edit_text(
                f"<b>✅ Shortlink {shortlink_num} configured successfully!</b>",
                reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton('≺≺ Back', callback_data="manage_shortlinks")
                ]])
            )
            
        except asyncio.exceptions.TimeoutError:
            await tamil.edit_text(
                'Process has been automatically cancelled.',
                reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton('≺≺ Back', callback_data=f"edit_shortlink_{shortlink_num}")
                ]])
            )

    elif data.startswith("delete_shortlink_"):
        shortlink_num = data.split("_")[-1]
        user_id = query.from_user.id
        
        if shortlink_num == "1":
            await u_db.delete_shortlink1(user_id)
        elif shortlink_num == "2":
            await u_db.delete_shortlink2(user_id)
        else:
            await u_db.delete_shortlink3(user_id)
        
        await query.answer(f"Shortlink {shortlink_num} deleted!", show_alert=True)
        
        # Refresh the manage shortlinks page
        await query.message.edit_text("Loading...", reply_markup=None)
        
        url1, api1 = await u_db.get_shortlink1(user_id)
        url2, api2 = await u_db.get_shortlink2(user_id)
        url3, api3 = await u_db.get_shortlink3(user_id)
        
        buttons = [
            [
                InlineKeyboardButton(
                    f"🔗 Shortlink 1 {'✅' if url1 and api1 else '❌'}",
                    callback_data="edit_shortlink_1"
                )
            ],
            [
                InlineKeyboardButton(
                    f"🔗 Shortlink 2 {'✅' if url2 and api2 else '❌'}",
                    callback_data="edit_shortlink_2"
                )
            ],
            [
                InlineKeyboardButton(
                    f"🔗 Shortlink 3 {'✅' if url3 and api3 else '❌'}",
                    callback_data="edit_shortlink_3"
                )
            ],
            [
                InlineKeyboardButton("≺≺ Back", callback_data="linkmode_settings"),
                InlineKeyboardButton("Close", callback_data="close")
            ]
        ]
        
        text = "<b><u>🔗 MANAGE SHORTLINKS</u></b>\n\n"
        text += f"<b>Shortlink 1:</b> {'✅ Active' if url1 and api1 else '❌ Not set'}\n"
        if url1 and api1:
            text += f"URL: <code>{url1}</code>\n\n"
        else:
            text += "\n"
        
        text += f"<b>Shortlink 2:</b> {'✅ Active' if url2 and api2 else '❌ Not set'}\n"
        if url2 and api2:
            text += f"URL: <code>{url2}</code>\n\n"
        else:
            text += "\n"
        
        text += f"<b>Shortlink 3:</b> {'✅ Active' if url3 and api3 else '❌ Not set'}\n"
        if url3 and api3:
            text += f"URL: <code>{url3}</code>\n\n"
        else:
            text += "\n"
        
        text += "<b>💡 Click on a shortlink to configure it</b>"
        
        await query.message.edit_text(
            text,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons)
        )

    elif data == "manage_linkmode_captions":
        user_id = query.from_user.id
        
        caption1 = await u_db.get_linkmode_caption1(user_id)
        caption2 = await u_db.get_linkmode_caption2(user_id)
        caption3 = await u_db.get_linkmode_caption3(user_id)
        active_caption = await u_db.get_active_linkmode_caption(user_id)
        
        buttons = [
            [
                InlineKeyboardButton(
                    f"📝 Caption 1 {'🟢' if active_caption == 1 else '🔴' if caption1 else '❌'}",
                    callback_data="edit_linkmode_caption_1"
                )
            ],
            [
                InlineKeyboardButton(
                    f"📝 Caption 2 {'🟢' if active_caption == 2 else '🔴' if caption2 else '❌'}",
                    callback_data="edit_linkmode_caption_2"
                )
            ],
            [
                InlineKeyboardButton(
                    f"📝 Caption 3 {'🟢' if active_caption == 3 else '🔴' if caption3 else '❌'}",
                    callback_data="edit_linkmode_caption_3"
                )
            ],
            [
                InlineKeyboardButton("≺≺ Back", callback_data="linkmode_settings"),
                InlineKeyboardButton("Close", callback_data="close")
            ]
        ]
        
        text = "<b><u>📝 MANAGE LINKMODE CAPTIONS</u></b>\n\n"
        text += f"<b>Active Caption:</b> Caption {active_caption}\n\n"
        text += f"<b>Caption 1:</b> {'✅ Set' if caption1 else '❌ Not set'}\n"
        text += f"<b>Caption 2:</b> {'✅ Set' if caption2 else '❌ Not set'}\n"
        text += f"<b>Caption 3:</b> {'✅ Set' if caption3 else '❌ Not set'}\n\n"
        text += "<b>🟢 = Active | 🔴 = Set but not active | ❌ = Not set</b>\n\n"
        text += "<b>💡 Click on a caption to configure it</b>"
        
        await query.message.edit_text(
            text,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons)
        )

    elif data.startswith("edit_linkmode_caption_"):
        caption_num = int(data.split("_")[-1])
        user_id = query.from_user.id
        
        if caption_num == 1:
            caption = await u_db.get_linkmode_caption1(user_id)
        elif caption_num == 2:
            caption = await u_db.get_linkmode_caption2(user_id)
        else:
            caption = await u_db.get_linkmode_caption3(user_id)
        
        active_caption = await u_db.get_active_linkmode_caption(user_id)
        is_active = active_caption == caption_num
        
        buttons = []
        if caption:
            buttons.append([
                InlineKeyboardButton("📋 View Caption", callback_data=f"view_linkmode_caption_{caption_num}")
            ])
            if not is_active:
                buttons.append([
                    InlineKeyboardButton("🟢 Set as Active", callback_data=f"activate_linkmode_caption_{caption_num}")
                ])
            buttons.append([
                InlineKeyboardButton("🗑️ Delete Caption", callback_data=f"delete_linkmode_caption_{caption_num}")
            ])
        
        buttons.append([
            InlineKeyboardButton("✏️ Set/Change Caption", callback_data=f"set_linkmode_caption_{caption_num}")
        ])
        buttons.append([
            InlineKeyboardButton("≺≺ Back", callback_data="manage_linkmode_captions"),
            InlineKeyboardButton("Close", callback_data="close")
        ])
        
        status = "✅ Set" if caption else "❌ Not set"
        active_status = " (🟢 Active)" if is_active else " (🔴 Inactive)" if caption else ""
        
        await query.message.edit_text(
            f"<b><u>📝 LINKMODE CAPTION {caption_num} SETTINGS</u></b>\n\n"
            f"<b>Status:</b> {status}{active_status}\n\n"
            f"<b>💡 Special Placeholders for Linkmode:</b>\n"
            f"<code>{{filenamefirst}}</code> - First file name\n"
            f"<code>{{filenamelast}}</code> - Last file name\n"
            f"<code>{{filecaptionfirst}}</code> - First file caption\n"
            f"<code>{{filecaptionlast}}</code> - Last file caption\n"
            f"<code>{{stream_link_1}}</code>, <code>{{download_link_1}}</code>, <code>{{storage_link_1}}</code>\n"
            f"<code>{{stream_link_2}}</code>, <code>{{download_link_2}}</code>, <code>{{storage_link_2}}</code>\n"
            f"<code>{{stream_link_3}}</code>, <code>{{download_link_3}}</code>, <code>{{storage_link_3}}</code>",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons)
        )

    elif data.startswith("view_linkmode_caption_"):
        caption_num = int(data.split("_")[-1])
        user_id = query.from_user.id
        
        if caption_num == 1:
            caption = await u_db.get_linkmode_caption1(user_id)
        elif caption_num == 2:
            caption = await u_db.get_linkmode_caption2(user_id)
        else:
            caption = await u_db.get_linkmode_caption3(user_id)
        
        if len(caption) > 170:
            await query.message.edit_text(
                text=f"<b>📝 Linkmode Caption {caption_num}:</b>\n\n{caption}",
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton('≺≺ Back', callback_data=f"edit_linkmode_caption_{caption_num}")
                ]])
            )
        else:
            await query.answer(f"Linkmode Caption {caption_num}:\n\n{caption}", show_alert=True)

    elif data.startswith("activate_linkmode_caption_"):
        caption_num = int(data.split("_")[-1])
        user_id = query.from_user.id
        
        await u_db.set_active_linkmode_caption(user_id, caption_num)
        await query.answer(f"Caption {caption_num} is now active!", show_alert=True)
        
        # Refresh the manage captions page
        caption1 = await u_db.get_linkmode_caption1(user_id)
        caption2 = await u_db.get_linkmode_caption2(user_id)
        caption3 = await u_db.get_linkmode_caption3(user_id)
        active_caption = caption_num
        
        buttons = [
            [
                InlineKeyboardButton(
                    f"📝 Caption 1 {'🟢' if active_caption == 1 else '🔴' if caption1 else '❌'}",
                    callback_data="edit_linkmode_caption_1"
                )
            ],
            [
                InlineKeyboardButton(
                    f"📝 Caption 2 {'🟢' if active_caption == 2 else '🔴' if caption2 else '❌'}",
                    callback_data="edit_linkmode_caption_2"
                )
            ],
            [
                InlineKeyboardButton(
                    f"📝 Caption 3 {'🟢' if active_caption == 3 else '🔴' if caption3 else '❌'}",
                    callback_data="edit_linkmode_caption_3"
                )
            ],
            [
                InlineKeyboardButton("≺≺ Back", callback_data="linkmode_settings"),
                InlineKeyboardButton("Close", callback_data="close")
            ]
        ]
        
        text = "<b><u>📝 MANAGE LINKMODE CAPTIONS</u></b>\n\n"
        text += f"<b>Active Caption:</b> Caption {active_caption}\n\n"
        text += f"<b>Caption 1:</b> {'✅ Set' if caption1 else '❌ Not set'}\n"
        text += f"<b>Caption 2:</b> {'✅ Set' if caption2 else '❌ Not set'}\n"
        text += f"<b>Caption 3:</b> {'✅ Set' if caption3 else '❌ Not set'}\n\n"
        text += "<b>🟢 = Active | 🔴 = Set but not active | ❌ = Not set</b>\n\n"
        text += "<b>💡 Click on a caption to configure it</b>"
        
        await query.message.edit_text(
            text,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons)
        )

    elif data.startswith("delete_linkmode_caption_"):
        caption_num = int(data.split("_")[-1])
        user_id = query.from_user.id
        
        if caption_num == 1:
            await u_db.delete_linkmode_caption1(user_id)
        elif caption_num == 2:
            await u_db.delete_linkmode_caption2(user_id)
        else:
            await u_db.delete_linkmode_caption3(user_id)
        
        # If the deleted caption was active, set caption 1 as active
        active_caption = await u_db.get_active_linkmode_caption(user_id)
        if active_caption == caption_num:
            await u_db.set_active_linkmode_caption(user_id, 1)
        
        await query.answer(f"Caption {caption_num} deleted!", show_alert=True)
        
        # Refresh the manage captions page
        await query.message.edit_text("Loading...", reply_markup=None)
        
        caption1 = await u_db.get_linkmode_caption1(user_id)
        caption2 = await u_db.get_linkmode_caption2(user_id)
        caption3 = await u_db.get_linkmode_caption3(user_id)
        active_caption = await u_db.get_active_linkmode_caption(user_id)
        
        buttons = [
            [
                InlineKeyboardButton(
                    f"📝 Caption 1 {'🟢' if active_caption == 1 else '🔴' if caption1 else '❌'}",
                    callback_data="edit_linkmode_caption_1"
                )
            ],
            [
                InlineKeyboardButton(
                    f"📝 Caption 2 {'🟢' if active_caption == 2 else '🔴' if caption2 else '❌'}",
                    callback_data="edit_linkmode_caption_2"
                )
            ],
            [
                InlineKeyboardButton(
                    f"📝 Caption 3 {'🟢' if active_caption == 3 else '🔴' if caption3 else '❌'}",
                    callback_data="edit_linkmode_caption_3"
                )
            ],
            [
                InlineKeyboardButton("≺≺ Back", callback_data="linkmode_settings"),
                InlineKeyboardButton("Close", callback_data="close")
            ]
        ]
        
        text = "<b><u>📝 MANAGE LINKMODE CAPTIONS</u></b>\n\n"
        text += f"<b>Active Caption:</b> Caption {active_caption}\n\n"
        text += f"<b>Caption 1:</b> {'✅ Set' if caption1 else '❌ Not set'}\n"
        text += f"<b>Caption 2:</b> {'✅ Set' if caption2 else '❌ Not set'}\n"
        text += f"<b>Caption 3:</b> {'✅ Set' if caption3 else '❌ Not set'}\n\n"
        text += "<b>🟢 = Active | 🔴 = Set but not active | ❌ = Not set</b>\n\n"
        text += "<b>💡 Click on a caption to configure it</b>"
        
        await query.message.edit_text(
            text,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons)
        )

    elif data.startswith("set_linkmode_caption_menu"):
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
        
        await query.message.edit_text(
            "<b><u>📝 LINKMODE CAPTION SETTINGS</u></b>\n\n"
            "Choose an option to manage your linkmode captions:\n\n"
            "<b>💡 Examples:</b> Pre-made caption templates you can use",
            reply_markup=InlineKeyboardMarkup(buttons)
        )

    elif data.startswith("set_example_caption_"):
        example_num = int(data.split("_")[-1])
        user_id = query.from_user.id
        
        if example_num == 1:
            caption = tamilxd.LINKMODE_EXAMPLE_CAPTION1
            await u_db.set_linkmode_caption1(user_id, caption)
            await u_db.set_active_linkmode_caption(user_id, 1)
        elif example_num == 2:
            caption = tamilxd.LINKMODE_EXAMPLE_CAPTION2
            await u_db.set_linkmode_caption2(user_id, caption)
            await u_db.set_active_linkmode_caption(user_id, 2)
        else:
            caption = tamilxd.LINKMODE_EXAMPLE_CAPTION3
            await u_db.set_linkmode_caption3(user_id, caption)
            await u_db.set_active_linkmode_caption(user_id, 3)
        
        await query.answer(f"Example caption {example_num} set and activated!", show_alert=True)
        
        # Refresh the manage captions page
        caption1 = await u_db.get_linkmode_caption1(user_id)
        caption2 = await u_db.get_linkmode_caption2(user_id)
        caption3 = await u_db.get_linkmode_caption3(user_id)
        active_caption = await u_db.get_active_linkmode_caption(user_id)
        
        buttons = [
            [
                InlineKeyboardButton(
                    f"📝 Caption 1 {'🟢' if active_caption == 1 else '🔴' if caption1 else '❌'}",
                    callback_data="edit_linkmode_caption_1"
                )
            ],
            [
                InlineKeyboardButton(
                    f"📝 Caption 2 {'🟢' if active_caption == 2 else '🔴' if caption2 else '❌'}",
                    callback_data="edit_linkmode_caption_2"
                )
            ],
            [
                InlineKeyboardButton(
                    f"📝 Caption 3 {'🟢' if active_caption == 3 else '🔴' if caption3 else '❌'}",
                    callback_data="edit_linkmode_caption_3"
                )
            ],
            [
                InlineKeyboardButton("≺≺ Back", callback_data="linkmode_settings"),
                InlineKeyboardButton("Close", callback_data="close")
            ]
        ]
        
        text = "<b><u>📝 MANAGE LINKMODE CAPTIONS</u></b>\n\n"
        text += f"<b>Active Caption:</b> Caption {active_caption}\n\n"
        text += f"<b>Caption 1:</b> {'✅ Set' if caption1 else '❌ Not set'}\n"
        text += f"<b>Caption 2:</b> {'✅ Set' if caption2 else '❌ Not set'}\n"
        text += f"<b>Caption 3:</b> {'✅ Set' if caption3 else '❌ Not set'}\n\n"
        text += "<b>🟢 = Active | 🔴 = Set but not active | ❌ = Not set</b>\n\n"
        text += "<b>💡 Click on a caption to configure it</b>"
        
        await query.message.edit_text(
            text,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons)
        )

    elif data.startswith("set_linkmode_caption_"):
        caption_num = int(data.split("_")[-1])
        await query.message.delete()
        
        try:
            tamil = await bot.send_message(
                query.message.chat.id,
                f"<b>Send your linkmode caption {caption_num}\n\n"
                f"<b>💡 Special Placeholders:</b>\n"
                f"<code>{{filenamefirst}}</code> - First file name\n"
                f"<code>{{filenamelast}}</code> - Last file name\n"
                f"<code>{{filecaptionfirst}}</code> - First file caption\n"
                f"<code>{{filecaptionlast}}</code> - Last file caption\n"
                f"<code>{{stream_link_1}}</code>, <code>{{download_link_1}}</code>, <code>{{storage_link_1}}</code>\n"
                f"<code>{{stream_link_2}}</code>, <code>{{download_link_2}}</code>, <code>{{storage_link_2}}</code>\n"
                f"<code>{{stream_link_3}}</code>, <code>{{download_link_3}}</code>, <code>{{storage_link_3}}</code>\n\n"
                f"Plus all normal placeholders like <code>{{file_name}}</code>, <code>{{file_size}}</code>, etc.\n\n"
                f"/cancel - Cancel this process</b>"
            )
            caption_input = await bot.listen(chat_id=user_id, timeout=300)
            
            if caption_input.text == "/cancel":
                await caption_input.delete()
                return await tamil.edit_text(
                    "<b>Process canceled!</b>",
                    reply_markup=InlineKeyboardMarkup([[
                        InlineKeyboardButton('≺≺ Back', callback_data=f"edit_linkmode_caption_{caption_num}")
                    ]])
                )
            
            # Test the caption format
            try:
                test_dict = {
                    'file_name': 'test', 'file_size': 'test', 'caption': 'test',
                    'download_link': 'test', 'stream_link': 'test', 'storage_link': 'test',
                    'quality': 'test', 'season': 'test', 'episode': 'test',
                    'stream_link_1': 'test', 'download_link_1': 'test', 'storage_link_1': 'test',
                    'stream_link_2': 'test', 'download_link_2': 'test', 'storage_link_2': 'test',
                    'stream_link_3': 'test', 'download_link_3': 'test', 'storage_link_3': 'test',
                    'filenamefirst': 'test', 'filenamelast': 'test',
                    'filecaptionfirst': 'test', 'filecaptionlast': 'test'
                }
                caption_input.text.format(**test_dict)
            except KeyError as e:
                await caption_input.delete()
                return await tamil.edit_text(
                    f"<b>❌ Invalid placeholder found: <code>{e}</code>\n\n"
                    f"Please check your caption and try again.</b>",
                    reply_markup=InlineKeyboardMarkup([[
                        InlineKeyboardButton('≺≺ Back', callback_data=f"edit_linkmode_caption_{caption_num}")
                    ]])
                )
            
            # Save the caption
            if caption_num == 1:
                await u_db.set_linkmode_caption1(user_id, caption_input.text)
            elif caption_num == 2:
                await u_db.set_linkmode_caption2(user_id, caption_input.text)
            else:
                await u_db.set_linkmode_caption3(user_id, caption_input.text)
            
            await caption_input.delete()
            await tamil.edit_text(
                f"<b>✅ Linkmode Caption {caption_num} saved successfully!</b>",
                reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton('≺≺ Back', callback_data="manage_linkmode_captions")
                ]])
            )
            
        except asyncio.exceptions.TimeoutError:
            await tamil.edit_text(
                'Process has been automatically cancelled.',
                reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton('≺≺ Back', callback_data=f"edit_linkmode_caption_{caption_num}")
                ]])
            )

    ####################### OTHAR CALLBACKS ##########################

    elif data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:  # noqa: E722
            await query.message.delete()
