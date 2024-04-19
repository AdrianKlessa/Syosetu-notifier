import configparser

import notification_pusher

DEFAULT_SLEEP = 3600
DEFAULT_VERBOSE = False
DEFAULT_FOLLOWED_NOVELS = []

# TODO: Utilize the "verbose" debug option to notify when getting updates even if no novel was updated

def read_config():
    config_file = configparser.ConfigParser()
    config_file.read('config.ini')
    config = dict()
    try:
        config["sleep_time"] = int(config_file["Scheduler"]["SleepTime"])
        config["verbose"] = config_file["Scheduler"].getboolean("Verbose")
        # join/split to support spaces between novel codes
        config["followed_novels"] = ''.join(config_file["Novels"]["FollowedNovels"].split()).split(',')
        if config["sleep_time"] is None or config["verbose"] is None or config["followed_novels"] is None:
            raise ValueError("Missing value in config file")
        if not all(isinstance(item, str) for item in config["followed_novels"]):
            raise ValueError("Failed to parse novel ncodes")
    except (KeyError, ValueError):
        notification_pusher.config_file_not_found_notification()
        config["sleep_time"] = DEFAULT_SLEEP
        config["verbose"] = DEFAULT_VERBOSE
        config["followed_novels"] = DEFAULT_FOLLOWED_NOVELS
    return config


def get_followed_novels():
    # TODO: For each from followed novels use api_client
    pass


def main_update_loop():
    # TODO: Sanity check using the data in history file and current time here
    # TODO: In a while loop get the followed novels from file, get updates and then wait the configured amount of time
    # TODO: Check the status returned by api_client
    pass


print(read_config())
