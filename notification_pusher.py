from winotify import Notification, audio
import os

app_id = "Syosetu notifier"

novels_url = "https://ncode.syosetu.com/"


def new_chapter_notification(author, title, ncode):
    toast = Notification(app_id=app_id,
                         title=f"New chapter for {title} released",
                         msg=f"{author} has added a new chapter for {title}",
                         icon=os.path.abspath("res/bookmark-book.png"))
    toast.set_audio(audio.Default, loop=False)
    # Using uppercase n-codes in URL results in a redirect page despite that format being used by the API
    toast.add_actions(label="Go to novel's homepage",
                      launch=f"https://ncode.syosetu.com/{ncode.lower()}/")
    toast.show()


def novel_modified_notification(author, title, ncode):
    toast = Notification(app_id=app_id,
                         title=f"{title} was modified",
                         msg=f"{author} has made modifications to {title}",
                         icon=os.path.abspath("res/bookmark-book.png"))
    toast.set_audio(audio.Default, loop=False)
    # Using uppercase n-codes in URL results in a redirect page despite that format being used by the API
    toast.add_actions(label="Go to novel's homepage",
                      launch=f"https://ncode.syosetu.com/{ncode.lower()}/")
    toast.show()


def history_file_not_found_notification():
    toast = Notification(app_id=app_id,
                         title="History file missing",
                         msg="History file could not be found despite previously being defined",
                         icon=os.path.abspath("res/file-not-found.png"))
    toast.set_audio(audio.Default, loop=False)
    toast.show()


def config_file_not_found_notification():
    toast = Notification(app_id=app_id,
                         title="Config file missing or corrupted",
                         msg="The config file is either missing or has incorrect values.",
                         icon=os.path.abspath("res/file-not-found.png"))
    toast.set_audio(audio.Default, loop=False)
    toast.show()


def custom_error_notification(title, msg):
    toast = Notification(app_id=app_id,
                         title=title,
                         msg=msg,
                         icon=os.path.abspath("res/cloud-xmark.png"))
    toast.set_audio(audio.Default, loop=False)
    toast.show()


def no_updates_notification():
    toast = Notification(app_id=app_id,
                         title="No novel updates found",
                         msg="No new novel information found during scheduled syosetu API check",
                         icon=os.path.abspath("res/bookmark-book.png"))
    toast.set_audio(audio.Default, loop=False)
    toast.show()
