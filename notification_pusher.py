from winotify import Notification, audio
import os

# TODO: Pass novel information (name, title) to notifications
def new_chapter_notification():
    toast = Notification(app_id="Syosetu notifier",
                         title="New chapter for novel!",
                         msg="New chapter for novel!",
                         icon=os.path.abspath("res/bookmark-book.png"))
    toast.set_audio(audio.Default, loop=False)
    toast.show()

def novel_modified_notification():
    toast = Notification(app_id="Syosetu notifier",
                         title="Novel chapter modified!",
                         msg="Novel chapter modified!",
                         icon=os.path.abspath("res/bookmark-book.png"))
    toast.set_audio(audio.Default, loop=False)
    toast.show()

def history_file_not_found_notification():
    toast = Notification(app_id="Syosetu notifier",
                         title="History file missing!",
                         msg="History file could not be found despite previously being defined",
                         icon=os.path.abspath("res/bookmark-book.png"))
    toast.set_audio(audio.Default,loop=False)

    toast.show()