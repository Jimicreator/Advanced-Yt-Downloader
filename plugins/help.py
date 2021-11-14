from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Currently Sorry 😔 Only supports Youtube Single  (Not playlist) Just Send Youtube Url"
    await message.reply_text(helptxt)
