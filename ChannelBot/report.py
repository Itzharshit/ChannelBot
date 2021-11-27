from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(filters.regex(r'^✉️ Submit Issue$') | filters.command('report'))
async def _manage(_, msg):
    how = '**Report a Problem** \n\n'
    how += "If you are facing any issue in this bot then you can report it to us.\n\n"
    how += '**Steps you have to follow** \n'
    how += 'Capture screenshot of problem you are facing in this bot. \n'
    how += 'Go to pyrogramers groups and explain your problem briefly.'
    how += "If you don't get a reply, ping @admin."
    await msg.reply(
        how,
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton('Pyrogrammers Group', url='https://t.me/+7ScFy39Vckk5MWQ1')]
        ]),
        quote=True
    )
