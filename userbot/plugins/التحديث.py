# updater for MFM

import asyncio
import sys
from os import environ, execle, path, remove

from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError

HEROKU_APP_NAME = Config.HEROKU_APP_NAME or None
HEROKU_API_KEY = Config.HEROKU_API_KEY or None
UPSTREAM_REPO_BRANCH = Config.UPSTREAM_REPO_BRANCH
UPSTREAM_REPO = "https://github.com/MFMVIP/MFM_USERBOT"
T = Config.COMMAND_HAND_LER

requirements_path = path.join(
    path.dirname(path.dirname(path.dirname(__file__))), "requirements.txt"
)


async def gen_chlog(repo, diff):
    ch_log = ""
    d_form = "%d/%m/%y"
    for c in repo.iter_commits(diff):
        ch_log += (
            f"  โข {c.summary} ({c.committed_datetime.strftime(d_form)}) <{c.author}>\n"
        )
    return ch_log


async def print_changelogs(event, ac_br, changelog):
    changelog_str = f"๐ฐ ๐๐ค๐ช๐ง๐๐ ๐๐ค๐ ๐๐ค - ๐ผ๐ท๐ซ๐จ๐ป๐ฌ ๐ด๐บ๐ฎ ๐ช\n ูดโถโโโโโโบแดแดแดสแดโปโโโโโโท\n** โชผ ููุฌูุฏ ุชุญูุฏูุซ ุฌุฏูุฏ ูุณูุฑุณ ุทูููู เผ.**\n\n`{changelog}`\n ูดโถโโโโโโบแดแดแดสแดโปโโโโโโท\n ๐ฐ ๐๐๐๐๐พ๐ ๐ฟ๐๐ - @MFMVIP ๐ช"
    if len(changelog_str) > 4096:
        await event.edit("`Changelog is too big, view the file to see it.`")
        with open("output.txt", "w+") as file:
            file.write(changelog_str)
        await event.client.send_file(
            event.chat_id,
            "output.txt",
            reply_to=event.id,
        )
        remove("output.txt")
    else:
        await event.client.send_message(
            event.chat_id,
            changelog_str,
            reply_to=event.id,
        )
    return True


async def update_requirements():
    reqs = str(requirements_path)
    try:
        process = await asyncio.create_subprocess_shell(
            " ".join([sys.executable, "-m", "pip", "install", "-r", reqs]),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        await process.communicate()
        return process.returncode
    except Exception as e:
        return repr(e)


async def deploy(event, repo, ups_rem, ac_br, txt):
    if HEROKU_API_KEY is not None:
        import heroku3

        heroku = heroku3.from_key(HEROKU_API_KEY)
        heroku_app = None
        heroku_applications = heroku.apps()
        if HEROKU_APP_NAME is None:
            await event.edit(
                "`Please set up the` **HEROKU_APP_NAME** `Var`"
                " to be able to deploy your userbot...`"
            )
            repo.__del__()
            return
        for app in heroku_applications:
            if app.name == HEROKU_APP_NAME:
                heroku_app = app
                break
        if heroku_app is None:
            await event.edit(f"{txt}\n" "ุจูุงูุงุช ุงุนุชูุงุฏ ููุฑููู ุบูุฑ ุตุงูุญุฉ ูุชูุตูุจ ุทูููู")
            return repo.__del__()
        await event.edit(
            "**ุชูุตูุจ ุชุญุฏูุซ ุทูููู ููุฏ ุงูุชูุฏู ุ ูุฑุฌู ุงูุงูุชุธุงุฑ ุญุชู ุชูุชูู ุงูุนูููุฉ ุ ูุนุงุฏุฉ ูุง ูุณุชุบุฑู ุงูุชุญุฏูุซ ูู 4 ุฅูู 5 ุฏูุงุฆู.**"
        )
        ups_rem.fetch(ac_br)
        repo.git.reset("--hard", "FETCH_HEAD")
        heroku_git_url = heroku_app.git_url.replace(
            "https://", "https://api:" + HEROKU_API_KEY + "@"
        )
        if "heroku" in repo.remotes:
            remote = repo.remote("heroku")
            remote.set_url(heroku_git_url)
        else:
            remote = repo.create_remote("heroku", heroku_git_url)
        try:
            remote.push(refspec="HEAD:refs/heads/master", force=True)
        except Exception as error:
            await event.edit(f"{txt}\n`Here is the error log:\n{error}`")
            return repo.__del__()
        build = app.builds(order_by="created_at", sort="desc")[0]
        if build.status == "failed":
            await event.edit(
                "`Build failed!\n" "Cancelled or there were some errors...`"
            )
            await asyncio.sleep(5)
            return await event.delete()
        await event.edit("`Successfully deployed!\n" "Restarting, please wait...`")
    else:
        await event.edit("`Please set up`  **HEROKU_API_KEY**  ` Var...`")
    return


async def update(event, repo, ups_rem, ac_br):
    try:
        ups_rem.pull(ac_br)
    except GitCommandError:
        repo.git.reset("--hard", "FETCH_HEAD")
    await update_requirements()
    await event.edit(
        "๐ฐ ๐๐ค๐ช๐ง๐๐ ๐๐ค๐ ๐๐ค - ๐ผ๐ท๐ซ๐จ๐ป๐ฌ ๐ด๐บ๐ฎ ๐ช\nูดโถโโโโโโบแดแดแดสแดโปโโโโโโท\n**โชผ ุชู ุงูุชุญุฏูุซ ุจูุฌุงุญ โ**\n ** ุฌุงุฑู ุฅุนุงุฏุฉ ุชุดุบูู ุจูุช ุทูููู ุ ุงูุชุธุฑ ๐ฐ.**"
    )
    # Spin a new instance of bot
    args = [sys.executable, "-m", "userbot"]
    execle(sys.executable, *args, environ)
    return


@icssbot.on(admin_cmd(outgoing=True, pattern=r"ุชุญุฏูุซ($| (ุงูุงู|ุงูุจูุช))"))
@icssbot.on(sudo_cmd(pattern="ุชุญุฏูุซ($| (ุงูุงู|ุงูุจูุช))", allow_sudo=True))
async def upstream(event):
    "ุจุงููุณุจุฉ ูุฃูุฑ ุงูุชุญุฏูุซ ุ ุชุญูู ููุง ุฅุฐุง ูุงู ุจูุช ุทูููู ูุญุฏุซูุง ุ ุฃู ูู ุจุงูุชุญุฏูุซ ุฅุฐุง ุชู ุจุชุญุฏูุซู"
    conf = event.pattern_match.group(1).strip()
    event = await edit_or_reply(
        event,
        "๐ฐ ๐๐ค๐ช๐ง๐๐ ๐๐ค๐ ๐๐ค - ๐ผ๐ท๐ซ๐จ๐ป๐ฌ ๐ด๐บ๐ฎ ๐ช\n ูดโถโโโโโโบแดแดแดสแดโปโโโโโโท\n**โชผ ุฌุงุฑู ุงูุจุญุซ ุนู ุงูุชุญุฏูุซุงุช  ๐.. ๐ฐุ**",
    )
    off_repo = UPSTREAM_REPO
    force_update = False
    if HEROKU_API_KEY is None or HEROKU_APP_NAME is None:
        return await edit_or_reply(
            event,
            "๐ฐ ๐๐ค๐ช๐ง๐๐ ๐๐ค๐ ๐๐ค - ๐ผ๐ท๐ซ๐จ๐ป๐ฌ ๐ด๐บ๐ฎ ๐ช\n ูดโถโโโโโโบแดแดแดสแดโปโโโโโโท\n** โชผ ุงุถุจุท ุงููุชุบูุฑุงุช ุงููุทููุจุฉ ุฃููุงู ูุชุญุฏูุซ ุจูุช ุทูููู ๐ฐุ**",
        )
    try:
        txt = "`ุนูููุง .. ูุง ูููู ูุจุฑูุงูุฌ ุงูุชุญุฏูุซ ุงููุชุงุจุนุฉ ุจุณุจุจ "
        txt += "ุญุฏุซุช ุจุนุถ ุงููุดุงูู`\n\n**ุชุชุจุน ุงูุณุฌู:**\n"
        repo = Repo()
    except NoSuchPathError as error:
        await event.edit(f"{txt}\nุงูุฏููู {error} ุบูุฑ ููุฌูุฏ")
        return repo.__del__()
    except GitCommandError as error:
        await event.edit(f"{txt}\n`ูุดู ูุจูุฑ! {error}`")
        return repo.__del__()
    except InvalidGitRepositoryError as error:
        if conf is None:
            return await event.edit(
                f"`Unfortunately, the directory {error} "
                "does not seem to be a git repository.\n"
                "But we can fix that by force updating the userbot using "
                ".update now.`"
            )
        repo = Repo.init()
        origin = repo.create_remote("upstream", off_repo)
        origin.fetch()
        force_update = True
        repo.create_head("master", origin.refs.master)
        repo.heads.master.set_tracking_branch(origin.refs.master)
        repo.heads.master.checkout(True)
    ac_br = repo.active_branch.name
    if ac_br != UPSTREAM_REPO_BRANCH:
        await event.edit(
            "**[UPDATER]:**\n"
            f"`Looks like you are using your own custom branch ({ac_br}). "
            "in that case, Updater is unable to identify "
            "which branch is to be merged. "
            "please checkout to any official branch`"
        )
        return repo.__del__()
    try:
        repo.create_remote("upstream", off_repo)
    except BaseException:
        pass
    ups_rem = repo.remote("upstream")
    ups_rem.fetch(ac_br)
    changelog = await gen_chlog(repo, f"HEAD..upstream/{ac_br}")
    # Special case for deploy
    if conf == "ุงูุจูุช":
        await event.edit(
            "๐ฐ ๐๐ค๐ช๐ง๐๐ ๐๐ค๐ ๐๐ค - ๐ผ๐ท๐ซ๐จ๐ป๐ฌ ๐ด๐บ๐ฎ ๐ช\nูดโถโโโโโโบแดแดแดสแดโปโโโโโโท\n**โชผ ูุชู ุชูุตูุจ ุงูุชุญุฏูุซ  ุงูุชุธุฑ ๐ ๐ฐุ**"
        )
        await deploy(event, repo, ups_rem, ac_br, txt)
        return
    if changelog == "" and not force_update:
        await event.edit(
            "\n๐ฐ ๐๐ค๐ช๐ง๐๐ ๐๐ค๐ ๐๐ค  - ๐ผ๐ท๐ซ๐จ๐ป๐ฌ ๐ด๐บ๐ฎ ๐ช\nูดโถโโโโโโบแดแดแดสแดโปโโโโโโท\n**โชผ ุณูุฑุณ ุทูููู ูุญุฏุซ ูุฃุฎุฑ ุงุตุฏุงุฑ เผ. **"
        )
        return repo.__del__()
    if conf == "" and not force_update:
        await print_changelogs(event, ac_br, changelog)
        await event.delete()
        return await event.respond(
            "๐ฐ ๐๐ค๐ช๐ง๐๐ ๐๐ค๐ ๐๐ค - ๐ผ๐ท๐ซ๐จ๐ป๐ฌ ๐ด๐บ๐ฎ ๐ช\n ูดโถโโโโโโบแดแดแดสแดโปโโโโโโท\nโชผ ุงุถุบุท ููุง **ููุชุญุฏูุซ ุงูุณุฑูุน โซ **[`{}ุชุญุฏูุซ ุงูุงู`] ุงู ุงุถุบุท ููุง **ูุชูุตูุจ ุงูุชุญุฏูุซ** ููุฏ ูุณุชุบุฑู 5 ุฏูุงุฆู โซ [`{}ุชุญุฏูุซ ุงูุจูุช`]".format(T, T)
        )

    if force_update:
        await event.edit(
            "`Force-Syncing to latest stable userbot code, please wait...`"
        )
    if conf == "ุงูุงู":
        await event.edit(
            "๐ฐ ๐๐ค๐ช๐ง๐๐ ๐๐ค๐ ๐๐ค - ๐ผ๐ท๐ซ๐จ๐ป๐ฌ ๐ด๐บ๐ฎ ๐ช\n ูดโถโโโโโโบแดแดแดสแดโปโโโโโโท\n**โชผ ูุชู ุชุญุฏูุซ ุจูุช ุทูููู ุงูุชุธุฑ ๐..๐ฐุ**"
        )
        await update(event, repo, ups_rem, ac_br)
    return


CMD_HELP.update(
    {
        "ุงูุชุญุฏูุซ": "**Plugin : **`ุงูุชุญุฏูุซ`\n"
        f" โข `{T}ุชุญุฏูุซ` ~ ูุนุฑุถ ุชุญุฏูุซุงุช ุงูุณูุฑุณ\n"
        f" โข `{T}ุชุญุฏูุซ ุงูุงู` ~ ูุชุญุฏูุซ ุงูุณุฑูุน"
    }
)
