Shousetsuka ni Narou is a Japanese-language website where authors publically upload their works. Many of the works originating from this website have later been published as physical books and then adapted into anime.

While the website has functionality for informing the user about novel updates, one has to log in and check their main user page to do so. There is no functionality for sending email notifications, or a webhook.

The goal of this application is to create a lightweight python application that could run in the background and periodically check for updates of specified novels, notifying the user about new chapters being added. Potentially author posts and/or modifications to previously added chapters.

The website's API is described here: https://dev.syosetu.com/man/api/

Notes:

- Syosetu has a request limit of 80k requests OR 400MB data transfer per day
- The limit is based on the IP address of the request origination, there is no user/password or token authentication in the API
- I plan to limit the update checks to 1~2 times per day and add some sanity checks for update checks to make sure the application does not cross the limit

Icons used in /res directory are modified version of icons downloaded from https://iconoir.com/ . The relevant copyright and permission notice is included in that directory.