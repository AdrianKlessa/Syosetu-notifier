from winotify import Notification
import os


toast = Notification(app_id="Syosetu notifier",
                     title="Update found!",
                     msg="New Notification!",
                     icon=os.path.abspath("res/bookmark-book.png"))

toast.show()