#    MFM - UserBot
#    (c) @MFMVIP

U = "๐ฐ ๐๐ค๐ช๐ง๐๐ ๐๐ค๐ ๐๐ค - ๐ช๐ถ๐ด๐ด๐ฌ๐ต๐ซ๐บ ๐ช\nูดโถโโโโโโบแดแดแดสแดโปโโโโโโท\n**โ โซ ูุงุฆููู ุงูุงูุฑ ุงูุงูุนุงุจ :** \nโชผ `.ุจูุงู` ูุนุฑุถ ูุงุฆููุฉ ุงูุงูุนูุงุจ ุงูุงุญุชุฑุงูููู\nโชผ `.ุงูุณ ุงู`\nโชผ `.ุณูู`\nโชผ `.ูุฑุฏ`\nโชผ `.ุณูุฉ`\nโชผ `.ูุฏู`\nโชผ `.ุญุธ` \nูดโถโโโโโโบแดแดแดสแดโปโโโโโโท\n๐ฉ ๐๐ค๐ช๐ง๐๐ ๐๐ค๐ ๐๐ค - [๐ฟ๐๐](t.me/MFMVIP) ๐ช"

@bot.on(admin_cmd(pattern="ู22"))
@bot.on(sudo_cmd(pattern="ู22", allow_sudo=True))
async def wspr(kimo):
    await eor(kimo, U)

@bot.on(admin_cmd(pattern="ุงูุณ ุงู$"))
@bot.on(sudo_cmd(pattern="ุงูุณ ุงู$", allow_sudo=True))
async def gamez(event):
    if event.fwd_from:
        return
    botusername = "@xobot"
    noob = "play"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, noob)
    await tap[0].click(event.chat_id)
    await event.delete()
