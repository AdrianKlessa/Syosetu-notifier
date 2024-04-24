from winotify import Notification, audio
import os

app_id = "Syosetu notifier"


# TODO: Pass novel information (name, title) to notifications
# TODO: On-click to link to the novel website?
def new_chapter_notification():
    toast = Notification(app_id=app_id,
                         title="New chapter for novel!",
                         msg="New chapter for novel!",
                         icon=os.path.abspath("res/bookmark-book.png"))
    toast.set_audio(audio.Default, loop=False)
    toast.show()


def novel_modified_notification():
    toast = Notification(app_id=app_id,
                         title="Novel chapter modified!",
                         msg="Novel chapter modified!",
                         icon=os.path.abspath("res/bookmark-book.png"))
    toast.set_audio(audio.Default, loop=False)
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
