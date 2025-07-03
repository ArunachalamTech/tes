#Copyright 2021 To 2024-present, Author: MrAKTech
from MrAKTech.config import Telegram
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class tamilxd(object):

    CUSTOM_SHORTNER_TXT = """<b><u>📝 CUSTOM SHORTNER</u>

To shorten your links using your preferred provider, make sure to connect it with me first.

➢ /api - To Add Your Shortener API
➢ /site - To Add Your Shortener URL </b>
    """

    SETTINGS_TXT = '''<b><u>㊂ User Settings</u>

┏📂 Daily Upload  : <code>∞ / ️∞</code> per day
┠♈ Site : <spoiler><code>{URLX}</code></spoiler>
┠♐ API : <spoiler><code>{APIX}</code></spoiler>
┠📄 Caption : <code>{CAPTION}</code>
┗🔍 Auto Extract : <code>{AUTO_EXTRACT}</code>

🦊 Mᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ ›› <a href=https://t.me/MrAK_BotZ>𝙼𝚁𝗔𝗞</a></b>'''

    RESET_SETTINGS = 'Do you want to Reset Settings ?'
    
    #"<b><u>⚙️ SETTINGS</u>\n♻️ ʜᴇʀᴇ ɪs ᴍʏ ᴀʟʟ sᴇᴛᴇᴇɴɢs ᴍᴇɴᴜ ♻️</b>"
    
    USER_ABOUT_MESSAGE = """
**❤️ ʜᴇʀᴇ ᴀʀᴇ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ sᴇᴛᴛɪɴɢs ғᴏʀ ᴛʜɪs ʙᴏᴛ : !!

🌐 ᴡᴇʙsɪᴛᴇ ➙ {shortener_url}

🔌 ᴀᴘɪ ➙ {shortener_api}

🕹 ᴍᴇᴛʜᴏᴅ ➙ {method}

🗃 sᴛᴏʀᴀɢᴇ ➙ {storage}
**"""
    
    CUSTOM_CAPTION_TXT = """<b>📝 Custom Caption Settings</b>

<b>🎯 How to Set Custom Caption:</b>
➢ <code>/addcaption</code> - Add your custom caption template
➢ <code>/showcaption</code> - View your current caption settings

<b>🎨 Formatting Options:</b>
• <a href="https://docs.pyrogram.org/topics/text-formatting#html-style">HTML Style</a> - Use &lt;b&gt;bold&lt;/b&gt;, &lt;i&gt;italic&lt;/i&gt;, etc.
• <a href="https://docs.pyrogram.org/topics/text-formatting#markdown-style">Markdown Style</a> - Use **bold**, *italic*, etc.

<b>📋 Available Variables:</b>
<code>{file_name}</code> - Original file name
<code>{file_size}</code> - File size (e.g., 1.2 GB)
<code>{caption}</code> - Original message caption
<code>{download_link}</code> - Direct download link
<code>{stream_link}</code> - Streaming link for video players

<b>🧠 Smart Auto-Extraction:</b>
<code>{quality}</code> - Video quality (1080p, 720p, 4K, etc.)
<code>{season}</code> - Season number (S01, S02, etc.)
<code>{episode}</code> - Episode number (E01, E02, etc.)

<b>💡 Pro Tip:</b>
<i>The bot automatically extracts information from both filename and original caption for best results!</i>

<b>📝 Example Caption Template:</b>
<code>🎬 {file_name}
📺 Quality: {quality} | Season: {season} | Episode: {episode}
📥 Download: {download_link}
🎮 Stream: {stream_link}</code>"""
    CHL_CUSTOM_CAPTION_TXT = '''<b><u>㊂ Caption Settings :</u>

➲ Custom Caption : <code>{CAPTIONX}</code>

➲ Description : <code>Bot Automatically edit your files Name</code></b>'''

    CHL_CHANNEL_DETAILS_TXT = '''<b><u>📄 Channel Details</u>
    
┏🏷️ TITLE: <code>{TITLEX}</code>
┠📋 CHANNEL ID: <code>{CHANNEL_DIX}</code>
┗👤 USERNAME: {USERNAMEX}

┏📂 Daily Upload  : <code>∞ / ️∞</code> Per Day
┠♈ Site : <spoiler>{URLX}</spoiler>
┠♐ API : <spoiler>{APIX}</spoiler>
┗📄 Caption : <code>{CAPTION}</code>

🦊 Mᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ ›› <a href=https://t.me/MrAK_BotZ>𝙼𝚁𝗔𝗞</a></b>'''

    CHL_SHORTNER_TXT = '''<b><u>㊂ Shortner Settings :</u>

➲ Custom URL : {URLX}
➲ Custom API : {APIX}

➲ Description : None'''

    CHL_CHANNEL_ADD_TXT = '''<b>Please add me as admin with atleast 'Post Messages' and 'Edit message of others' rights to the desired channel

After that, forward a message from the channel.

Cancel this process using /cancel. 

Timeout: 60 sec (If their is no reply in 60 sec, action will be auto cancelled.)</b>'''
    
    START_TXT = """<b>Hello {} 👋

I'm a powerful File-to-Link bot that converts your files into permanent streaming and download links!

<u>✨ What I can do:</u>
• Convert any file (up to 4GB) into permanent links
• Generate both download and streaming links
• Work in private chats and channels
• Auto-extract quality, season, episode info

<i>📤 Just send me any media file and I'll create permanent links for you!</i>

<u>⚠️ Important Rules:</u>
<i>• No adult content allowed - leads to permanent ban
• Use responsibly and respect copyright</i>

� Powered by <a href=https://t.me/MrAK_BotZ>MrAK Technology</a></b>"""

    ABOUT_TXT = """<b>╭──────❰ <u>🤖 Bot Details</u> ❱──────〄
│ 
│ 🤖 Mʏ Nᴀᴍᴇ : <a href=https://t.me/MrAKStreamBot>𝙼𝚁𝗔𝗞 𝐅𝚊𝚖𝚎𝐓𝚘𝐋𝚒𝚗𝚔𝐁𝚘𝚝</a>
│ 👨‍💻 Dev : <a href=https://t.me/MrAK_BotZ>𝙼𝚁𝗔𝗞</a>
│ 📢 Uᴘᴅᴀᴛᴇꜱ : <a href=https://t.me/MrAK_BotZ>𝙼𝚁𝗔𝗞</a>
│ 📡 Server : <a href=https://www.heroku.com/>Heroku Eco</a>
│ 🗣️ Language : <a href=https://www.python.org>Python 3.12.4</a>
│ 📚 Library : <a href=https://github.com/Mayuri-Chan/pyrofork>PyroFork 2.3.37</a> 
│ 🛢️ Database : <a href=https://www.mongodb.com/>MongoDB 7.0.12</a>
│ 🗒️ Build Version : V1.8.2 [ Bᴇᴛᴀ ]
│ 
╰────────────────────⍟</b>"""

    FORCE_SUB_TEXT = "👋 Hello {},\n\n<b>🔐 Join Required!</b>\n\n<i>Please join our updates channel to use this bot. This helps us provide better service and keep you updated with new features!</i>\n\n<b>📢 After joining, come back and try again.</b>\n\nThank you for your support! 💙"
    
    HELP_TXT = """<b>📚 How to Use This Bot</b>

<b>🚀 Quick Start:</b>
⇒ Send me any file or media from Telegram
⇒ I'll instantly create permanent download and streaming links
⇒ Links work forever and never expire!

<b>🎬 For Streaming:</b>
⇒ Copy the streaming link and paste it in any video player
⇒ Works with VLC, MX Player, or any external video player
⇒ Enjoy smooth streaming directly from our servers

<b>📱 Channel Support:</b>
⇒ Add me to your channel as admin with "Post Messages" permission
⇒ I'll automatically process all media files posted
⇒ Perfect for movie channels and content sharing

<b>🛠️ Advanced Features:</b>
⇒ <code>/features</code> - Learn about custom shorteners
⇒ <code>/extract</code> - Auto-extract quality, season, episode info
⇒ <code>/examples</code> - See caption formatting examples
⇒ <code>/test filename</code> - Test filename extraction

<b>⚙️ Custom Settings:</b>
⇒ Add your own URL shortener for extra income
⇒ Customize captions with smart auto-extraction
⇒ Configure settings for optimal performance

<b>❗ Rules & Guidelines:</b>
• No adult content - results in permanent ban
• Respect copyright and fair use policies
• Use for personal or educational purposes

<i>💬 Need help? Contact our support team anytime!</i>

<b>👨‍💻 Support: @IamMrAK_bot
📢 Main Channel: @MrAK_LinkZzz
🔔 Updates: @MrAK_BotZ</b>"""
    
    OWNER_INFO = """<b><u>🤖 Owner Details 🌿</u>

‣ Full Name : 𝙼𝚁𝗔𝗞
‣ Username : @IamMrAK_bot 
‣ Permanent DM link :<a href=https://t.me/IamMrAK_bot>Click Here</a></b>"""
    
    SOURCE_TXT = """<b><u>Notes</u>:

<code>⚠️ This bot is an private source project.

⇒ I will create a bot for you
⇒ Contact me</code> - <a href=https://t.me/IamMrAK_bot>♚ ᴀᴅᴍɪɴ ♚</a></b>"""


    DEV_TXT = """**__Special Thanks & Developers__

» 𝗦𝗢𝗨𝗥𝗖𝗘 𝗖𝗢𝗗𝗘 : [Click Here](https://github.com/MrAKTech) 

• @IamMrAK_bot
• @MrAK_BotZ

📢 𝙼𝙰𝙸𝙽 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 : @MrAK_LinkZzz
❣️ 𝚄𝙿𝙳𝙰𝚃𝙴𝚂 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 : @MrAK_BotZ**"""
    
    COMMENTS_TXT = """<b>💰 How to Connect Your Own URL Shortener</b>

<b>💡 Why Add a Shortener?</b>
• Earn money from every link click
• Track your link analytics
• Customize your link domains

<b>🚀 Setup Commands:</b>
<b>Main Commands:</b>
1. <code>/site</code> or <code>/shortner_url</code> - Set your shortener domain
2. <code>/api</code> or <code>/shortner_api</code> - Add your API key
3. <code>/addcaption</code> - Customize your captions
4. <code>/showcaption</code> - View current caption
5. <code>/settings</code> - View all settings
6. <code>/stats</code> - Check your statistics
7. <code>/status</code> - Bot status information

<b>Other Commands:</b>
1. <code>/about</code> - Bot information
2. <code>/help</code> - Get help
3. <code>/ping</code> - Check bot response
4. <code>/users</code> - User statistics

<b>📝 Example Setup:</b>
<code>/site example.com</code>
<code>/api ec8ba7deff6128848def53bf2d4e69608443cf27</code>

<b>🔗 Popular Shortener Services:</b>
• GPLinks, ShrinkMe, LinkVertise
• Short.st, Ouo.io, Fc.lc
• And many more!

<i>💬 Having trouble? Our support team is here to help!</i>

<b>👨‍💻 Support: @IamMrAK_bot
📢 Main Channel: @MrAK_LinkZzz
🔔 Updates: @MrAK_BotZ</b>"""



    DONATE_TXT = """<b><u>💗 Thank you showing internet in donation</u></b>

<i>Donate us to keep our services continously alive, You can send any amount 😢.</i>

<b><u>How You Can Donate:</u>
You can support us with any amount that suits you, such as ₹20, ₹50, ₹100, or ₹200. Every contribution makes a difference!

<u>📨 Payment Methods:</u>

• UPI ID: <code>mraklinkzz@axl</code></b>

For more information and further queries, please message @TamilXD.

Thank you for your support! 🙏</b>"""    
    ADN_COMS = """
<b> Aᴅᴍɪɴ Cᴏᴍᴍᴀɴᴅs

/ban

/unban

/status 

/broadcast or pin_broadcast

/logs

/invite_link 

/leave

/warnz
</b>
"""

    STREAM_MSG_TXT = """<b>🎉 Your Links Are Ready!</b>

📂 <b>File:</b> {file_name} 
📦 <b>Size:</b> {file_size}

<b>🔗 Your Links:</b>
📥 <b>Download:</b> {download_link}
🎮 <b>Stream/Watch:</b> {stream_link}

<b>📚 How to Use:</b>
• <b>Download:</b> Click the download link to save the file
• <b>Streaming:</b> Copy the stream link and paste it in any video player (VLC, MX Player, etc.)

<b>✨ Features:</b>
• Links are permanent and never expire
• High-speed downloads
• Support for all file types</b>"""

    LINKMODE_EXAMPLE_CAPTION1 = """{filenamefirst} 

❤️‍🔥 Uploaded By - [] [@Back2flix_Links ]

⬆️ ᴅɪʀᴇᴄᴛ ғɪʟᴇs / ᴏɴʟɪɴᴇ ᴡᴀᴛᴄʜɪɴɢ / ꜰᴀꜱᴛ ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ʟɪɴᴋ ⚡️

{file_size}({quality}) :- {stream_link_1}

✔️ ɴᴏᴛᴇ : [ʜᴏᴡ ᴛᴏ ᴏᴩᴇɴ lksfty Url] (https://t.me/shotner_solution/6)

ᴅɪʀᴇᴄᴛ ғɪʟᴇs / ᴏɴʟɪɴᴇ ᴡᴀᴛᴄʜɪɴɢ / ꜰᴀꜱᴛ ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ʟɪɴᴋ ⚡️

{file_size}({quality}) :- {stream_link_2}

✔️ ɴᴏᴛᴇ : [ʜᴏᴡ ᴛᴏ ᴏᴩᴇɴ shortenr Url] (https://t.me/shotner_solution/7)

📱 sʜᴀʀᴇ ᴡɪᴛʜ ғʀɪᴇɴᴅs 📌"""

    LINKMODE_EXAMPLE_CAPTION2 = """🎬 **{file_name}**

📺 Quality: **{quality}** | Season: **{season}** | Episode: **{episode}**
📦 Size: **{file_size}**

🔗 **Download Links:**
📥 Link 1: {download_link_1}
📥 Link 2: {download_link_2}
📥 Link 3: {download_link_3}

🎮 **Stream Links:**
▶️ Stream 1: {stream_link_1}
▶️ Stream 2: {stream_link_2}
▶️ Stream 3: {stream_link_3}

💾 **Storage:** {storage_link}

📱 **Share with friends!**"""

    LINKMODE_EXAMPLE_CAPTION3 = """📁 **Batch Upload Complete!**

🎬 **First File:** {filenamefirst}
🎬 **Last File:** {filenamelast}

📊 **File Details:**
📂 File: {file_name}
📦 Size: {file_size}
🎞️ Quality: {quality}

🔗 **Multiple Download Options:**
🌟 **Option 1:** {download_link_1}
🌟 **Option 2:** {download_link_2}
🌟 **Option 3:** {download_link_3}

▶️ **Stream Online:** {stream_link}

💡 **Tip:** Use different links for backup access!"""

    LINKMODE_HELP_TXT = """<b><u>🔗 LINKMODE COMPREHENSIVE GUIDE</u></b>

<b>🎯 What is Linkmode?</b>
Linkmode is an advanced feature that allows you to:
• Process multiple files in batches
• Use multiple shortener services simultaneously
• Create advanced caption templates with special placeholders
• Generate different shortened links for the same content

<b>📋 How to Use Linkmode:</b>

<b>1️⃣ Enable Linkmode:</b>
• <code>/linkmode on</code> - Start linkmode
• <code>/linkmode off</code> - Stop linkmode

<b>2️⃣ Configure Shorteners:</b>
• <code>/shortlink1 {url} {api}</code> - Set first shortener
• <code>/shortlink2 {url} {api}</code> - Set second shortener  
• <code>/shortlink3 {url} {api}</code> - Set third shortener
• <code>/list_shortlinks</code> - View all configured shorteners

<b>3️⃣ Setup Captions:</b>
• <code>/setlinkmodecaption</code> - Access caption management
• Create up to 3 different caption templates
• Switch between templates anytime

<b>4️⃣ Process Files:</b>
• Send multiple files (they get added to batch)
• Use <code>/complete</code> to process all files

<b>🏷️ Special Linkmode Placeholders:</b>

<b>📁 File Information:</b>
• <code>{filenamefirst}</code> - Name of first file in batch
• <code>{filenamelast}</code> - Name of last file in batch  
• <code>{filecaptionfirst}</code> - Caption of first file
• <code>{filecaptionlast}</code> - Caption of last file

<b>🔗 Shortener-Specific Links:</b>
• <code>{stream_link_1}</code> - Stream link via shortener 1
• <code>{download_link_1}</code> - Download link via shortener 1
• <code>{storage_link_1}</code> - Storage link via shortener 1
• <code>{stream_link_2}</code> - Stream link via shortener 2
• <code>{download_link_2}</code> - Download link via shortener 2
• <code>{storage_link_2}</code> - Storage link via shortener 2
• <code>{stream_link_3}</code> - Stream link via shortener 3
• <code>{download_link_3}</code> - Download link via shortener 3
• <code>{storage_link_3}</code> - Storage link via shortener 3

<b>📝 Regular Placeholders:</b>
All standard placeholders work: <code>{file_name}</code>, <code>{file_size}</code>, <code>{quality}</code>, <code>{season}</code>, <code>{episode}</code>, etc.

<b>💡 Pro Tips:</b>
• If a shortener is not configured, its links will be empty
• Use different shorteners for redundancy
• Test your caption templates before using them
• Linkmode works great for series uploads!</b>"""
# ------------------------------------------------------------------------------

class BUTTON(object):
    
    OWNER_BUTTONS =  InlineKeyboardMarkup([
        InlineKeyboardButton('𝙼𝚁𝗔𝗞', url= Telegram.MAIN )
    ])

    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📢 𝙼𝙰𝙸𝙽 𝙲𝙷𝙰𝙽𝙽𝙴𝙻', url= Telegram.MAIN),
        InlineKeyboardButton('⚡ 𝚄𝙿𝙳𝙰𝚃𝙴𝚂 𝙲𝙷𝙰𝙽𝙽𝙴𝙻', url= Telegram.AUTH_CHANNEL3)
        ],[
        InlineKeyboardButton('📢 𝙼𝙾𝚅𝙸𝙴 𝙶𝚁𝙾𝚄𝙿', url= Telegram.AUTH_GROUP)
        ],[
        InlineKeyboardButton('⚙️ Hᴇʟᴘ', callback_data='help'),
        InlineKeyboardButton('📚 Aʙᴏᴜᴛ', callback_data='about')
        ],[
        InlineKeyboardButton('⚙️ Sᴇᴛᴛɪɴɢs ', callback_data='settings')
        ]]
    )

    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton("📊 Status", callback_data="stats")
        ],[
        InlineKeyboardButton("⛺ Home", callback_data="start"),
        InlineKeyboardButton("🗑 Close", callback_data="close")
        ]]
    )

    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📢 𝙼𝙰𝙸𝙽 𝙲𝙷𝙰𝙽𝙽𝙴𝙻', url= Telegram.MAIN),
        InlineKeyboardButton('⚡ 𝚄𝙿𝙳𝙰𝚃𝙴𝚂 𝙲𝙷𝙰𝙽𝙽𝙴𝙻', url= Telegram.AUTH_CHANNEL3)
        ],[
        InlineKeyboardButton('📢 𝙼𝙾𝚅𝙸𝙴 𝙶𝚁𝙾𝚄𝙿', url= Telegram.AUTH_GROUP)
        ],[
        InlineKeyboardButton("🌿 sᴏᴜʀᴄᴇ", callback_data = "source"),
        InlineKeyboardButton("👨‍💻 Dᴇᴠs 🥷", callback_data = "dev")
        ],[
        InlineKeyboardButton("⛺ Hᴏᴍᴇ", callback_data = "start"),
        InlineKeyboardButton("🗑 Cʟᴏsᴇ", callback_data = "close")
        ]]
    )
    
    DONATE_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton("Pᴀʏ 💰 Aᴍᴏᴜɴᴛ",
                                             url= Telegram.SUPPORT)
        ],[
        InlineKeyboardButton("⛺ Hᴏᴍᴇ", callback_data="start"),
        InlineKeyboardButton("🗑 Cʟᴏsᴇ", callback_data="close")
        ]]
    ) 

    DEV_BUTTONS = InlineKeyboardMarkup( 
        [[
        InlineKeyboardButton('𝙼𝚁𝗔𝗞', url= Telegram.SUPPORT),
        ],[
        InlineKeyboardButton("≺≺ Back", callback_data = "about"),
        InlineKeyboardButton("🗑 Close", callback_data = "close")
        ]]
    ) 

    ADN_BUTTONS = InlineKeyboardMarkup( 
        [[
        InlineKeyboardButton("🗑 Close", callback_data = "close")
        ]]
    ) 

    SOURCE_BUTTONS = InlineKeyboardMarkup( 
        [[
        InlineKeyboardButton("♙ ʜᴏᴍᴇ", callback_data = "start"),
        InlineKeyboardButton("🗑 Close", callback_data = "close")
        ]]
    )
