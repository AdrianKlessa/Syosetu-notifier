Shousetsuka ni Narou is a Japanese-language website where authors publically upload their works. Many of the works originating from this website have later been published as physical books and then adapted into anime.

While the website has functionality for informing the user about novel updates, one has to log in and check their main user page to do so. There is no functionality for sending email notifications, or a webhook.

This application is a lightweight python app that can run in the background and periodically check for updates of specified novels, notifying the user about new chapters being added and modifications to existing chapters (if enabled).

The website's API is described here: https://dev.syosetu.com/man/api/

### Requirements (tested version in parenthesis)

* Windows 10 - might work on 11 but untested
* winotify (1.1.0)
* PyYAML (6.0)
* python-dateutil (2.8.2)


### Installation instructions

1. Have python and the dependencies listed above installed
2. Clone this repository into a location where you want to store this app.
3. Adjust the config.ini file:
   * `FollowedNovels` is the list of (comma-seperated) ncodes of novels you want to follow. These can be found by going to the home page of the novel you are interested in, and seeing the url. It will look like `https://ncode.syosetu.com/nXXXXYY/`. The `nXXXXYY` is the ncode. The default config has example values for Overlord and Mitsuba Monogatari.
   * Examples of correct values: `n4402bd,n0388ee` or `n4402bd` or `n4402bd,n0388ee,n0432fz`
   * Set `NovelModifiedNotifications` to 1 if you want to be notified when an author made changes to a novel that are not new chapters (typo fixes, rewrites of previous chapters etc.)
   * Set `SleepTime` to a higher/lower value if you want a different update schedule. For updates more frequent than every 30 minutes, check the notes section below.
4. During the first startup the app will create its history file (used for comparing new info from the API) and notify you that there were novel updates (since the history file is empty at this point and any data received is new).

### Adding to autostart
1. Make a shortcut to `syosetu_notifier.pyw`
2. Move the shortcut to your startup directory (can be found by pressing `Windows logo key + R`, typing `shell:startup` and pressing `enter`)

Can later be removed from startup by going to `Startup Apps` in Windows and disabling `syosetu_notifier.pyw` there.

### Features
* Windows 10 toast popups (thanks to the winotify package)
* Novel update popups have a button that takes you to the novel's homepage
* Customizable list of followed novels
* Option to notify about minor modifications to novels (information about which is not currently visible when going to the author's homepage in the web browser)


Notes:

- Syosetu has a request limit of 80k requests OR 400MB data transfer per day
- The limit is based on the IP address of the request origination, there is no user/password or token authentication in the API
- This app's default setting is to check the API once per hour. There is a second, hard-coded sanity check in history_manager that makes sure that 30+ minutes passed since the last request was sent. To make checks more often that value would need to be also adjusted.

Icons used in /res directory are modified version of icons downloaded from https://iconoir.com/ . The relevant copyright and permission notice is included in that directory.
