from winotify import Notification, audio
from pathlib import Path

RES_DIRECTORY = Path(__file__).parent.resolve()
RES_DIRECTORY = RES_DIRECTORY / "res"

APP_ID = "Syosetu notifier"

novels_url = "https://ncode.syosetu.com/"

def new_chapter_notification(author, title, ncode):
    toast = Notification(app_id=APP_ID,
                         title=f"New chapter for: {title}",
                         msg=f"{author} has added a new chapter for {title}",
                         icon=str(RES_DIRECTORY.joinpath("bookmark-book.png").absolute()))
    toast.set_audio(audio.Default, loop=False)
    # Using uppercase n-codes in URL results in a redirect page despite that format being used by the API
    toast.add_actions(label="Go to novel's homepage",
                      launch=f"https://ncode.syosetu.com/{ncode.lower()}/")
    toast.show()


def novel_modified_notification(author, title, ncode):
    toast = Notification(app_id=APP_ID,
                         title=f"Novel modified: {title}",
                         msg=f"{author} has made modifications to {title}",
                         icon=str(RES_DIRECTORY.joinpath("edit-pencil.png").absolute()))
    toast.set_audio(audio.Default, loop=False)
    # Using uppercase n-codes in URL results in a redirect page despite that format being used by the API
    toast.add_actions(label="Go to novel's homepage",
                      launch=f"https://ncode.syosetu.com/{ncode.lower()}/")
    toast.show()


def history_file_not_found_notification():
    toast = Notification(app_id=APP_ID,
                         title="History file missing",
                         msg="History file could not be found despite previously being defined",
                         icon=str(RES_DIRECTORY.joinpath("file-not-found.png").absolute()))
    toast.set_audio(audio.Default, loop=False)
    toast.show()


def config_file_not_found_notification():
    toast = Notification(app_id=APP_ID,
                         title="Config file missing or corrupted",
                         msg="The config file is either missing or has incorrect values.",
                         icon=str(RES_DIRECTORY.joinpath("file-not-found.png").absolute()))
    toast.set_audio(audio.Default, loop=False)
    toast.show()


def custom_error_notification(title, msg):
    toast = Notification(app_id=APP_ID,
                         title=title,
                         msg=msg,
                         icon=str(RES_DIRECTORY.joinpath("cloud-xmark.png").absolute()))
    toast.set_audio(audio.Default, loop=False)
    toast.show()


def no_updates_notification():
    toast = Notification(app_id=APP_ID,
                         title="No novel updates found",
                         msg="No new novel information found during scheduled syosetu API check",
                         icon=str(RES_DIRECTORY.joinpath("bookmark-book.png").absolute()))
    toast.set_audio(audio.Default, loop=False)
    toast.show()