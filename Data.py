from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hii {}

I am Auto Captions Injector bot created by @pyrogrammers.
I can automatically add Captions with buttons to every post of your channel.
I can also add stickers after every post.
Hit /help to know how to use me.

𝗜𝗳 𝘆𝗼𝘂 𝗹𝗶𝗸𝗲 𝘁𝗵𝗶𝘀 𝗯𝗼𝘁 𝗮𝗻𝗱 𝘄𝗮𝗻𝘁 𝘁𝗼 𝗵𝗲𝗹𝗽 𝗱𝗲𝘃𝗹𝗼𝗽𝗲𝗿 𝗽𝗹𝗲𝗮𝘀𝗲 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲 𝗺𝘆 𝘆𝗼𝘂𝘁𝘂𝗯𝗲 𝗰𝗵𝗮𝗻𝗻𝗲𝗹.
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="𝗠𝗮𝗶𝗻 𝗺𝗲𝗻𝘂", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("📺 𝗠𝘆 𝗬𝗼𝘂𝗧𝘂𝗯𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url="https://youtube.com/channel/UC2anvk7MNeNzJ6B4c0SZepw")],
        [
            InlineKeyboardButton("📢 𝗠𝘆 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url="https://t.me/pyrogrammers"),
            InlineKeyboardButton("🎎 𝗠𝘆 𝗚𝗿𝗼𝘂𝗽", url="https://t.me/+7ScFy39Vckk5MWQ1")
        ],
    ]

    # Help Message
    HELP = """
 **Available Commands** 
/help - This Message
/start - Check bot Is alive or not

More Commands
/channels - List of all your Channels
/add - Add a new channel
/report - Report Problems
    """

    # About Message
    ABOUT = """ """
