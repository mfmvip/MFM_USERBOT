from . import reply_id as rd
from userbot.tosh import *


WPIC = "https://telegra.ph/file/967209504b62689f5f770.jpg"
T = "๐ฐ ๐๐ค๐ช๐ง๐๐ ๐๐ค๐ ๐๐ค - ๐บ๐ฌ๐ช๐น๐ฌ๐ป ๐ด๐บ๐ฎ ๐ช\nูดโถโโโโโโบแดแดแดสแดโปโโโโโโท\n**โ โซ ูุงุฆููู ุงูุงูุฑ ุงูููุณู :** \nโชผ `.ุงูููุณู` ูุนุฑุถ ููููู ุงุฑุณุงู ุงูููุณู ูู ุจูุชู\nโชผ `.ููุณู` ูุงุฑุณุงู ููุณู ุนู ุทุฑูู ุจูุช ุงูููุณู  \nูดโถโโโโโโบแดแดแดสแดโปโโโโโโท\n๐ฉ ๐๐ค๐ช๐ง๐๐ ๐๐ค๐ ๐๐ค - [ููุงุฉ ุงูุณูุฑุณ](t.me/TOKYO_TEAM) ๐ช"

@bot.on(admin_cmd(pattern="ู21"))
@bot.on(sudo_cmd(pattern="ู21", allow_sudo=True))
async def wspr(kimo):
    await eor(kimo, T)


# Wespr - ููุณู
@bot.on(admin_cmd(pattern="ุงูููุณู$"))
@bot.on(sudo_cmd(pattern="ุงูููุณู$", allow_sudo=True))
async def kimo(lon):
    if lon.fwd_from:
        return
    ld = await rd(lon)
    if WPIC:
        ics_c = f"- ููููู ุงุฑุณุงู ููุณุฉ ูุนุฏู ุงุดุฎุงุต ูุฑู ูุงุญุฏู\n- ููููู ููุณ ( ููุตู - ุตูุฑู - ุตูุช - ูุชุญุฑู - ููุฏูู ) ููุท ุงุฑุณู ููุจูุช @BYYiBoT \n- ููุตู ุงุดุนุนุงุฑ ูู ุดุงูุฏ ููุณุชู ููุท ุงุฐุง ูุงูุช ุงูููุณู ูุต ููุดุงูุฏู ุงูุทุฑููู @nayy2019๐คโจ.\n"
        ics_c += f"**- ูู ุจูุณุฎ :**\n `@BYYiBoT ุงูุฑุณุงูู ุซู ูุนุฑู ุงูุดุฎุต`"
        await lon.client.send_file(lon.chat_id, WPIC, caption=ics_c, reply_to=ld)


# Wespr - ููุณู
@bot.on(admin_cmd(pattern="ููุณู ?(.*)"))
@bot.on(sudo_cmd(pattern="ููุณู ?(.*)", allow_sudo=True))
async def wspr(event):
    if event.fwd_from:
        return
    wwwspr = event.pattern_match.group(1)
    bu = "@BYYiBoT"
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    tap = await bot.inline_query(bu, wwwspr) 
    await tap[0].click(event.chat_id)
    await event.delete()
