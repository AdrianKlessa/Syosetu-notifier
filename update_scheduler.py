import configparser
import time
import api_client
import notification_pusher
import history_manager
from pathlib import Path

DEFAULT_SLEEP = 3600
DEFAULT_VERBOSE = False
DEFAULT_FOLLOWED_NOVELS = []
DEFAULT_MODIFIED_NOTIFICATION = False
CONFIG_FILE_NAME = Path(__file__).with_name("config.ini").absolute()

def read_config():
    config_file = configparser.ConfigParser()
    config_file.read(CONFIG_FILE_NAME)
    config = dict()
    try:
        config["sleep_time"] = int(config_file["Scheduler"]["SleepTime"])
        config["verbose"] = config_file["Scheduler"].getboolean("Verbose")
        config["novel_modified_notifications"] = config_file["Notifications"].getboolean("NovelModifiedNotifications")
        # join/split to support spaces between novel codes
        config["followed_novels"] = ''.join(config_file["Novels"]["FollowedNovels"].split()).split(',')
        if config["sleep_time"] is None or config["verbose"] is None or config["followed_novels"] is None or config[
            "novel_modified_notifications"] is None:
            raise ValueError("Missing value in config file")
        if not all(isinstance(item, str) for item in config["followed_novels"]):
            raise ValueError("Failed to parse novel ncodes")
    except (KeyError, ValueError):
        notification_pusher.config_file_not_found_notification()
        config["sleep_time"] = DEFAULT_SLEEP
        config["verbose"] = DEFAULT_VERBOSE
        config["followed_novels"] = DEFAULT_FOLLOWED_NOVELS
        config["novel_modified_notifications"] = DEFAULT_MODIFIED_NOTIFICATION
    return config


def main_update_loop():
    history_manager.check_create_history_file()
    while True:
        config = read_config()
        updated_number = 0

        # Don't like the number of ifs here but don't see a good way to refactor ATM
        if history_manager.can_update_already():
            new_novel_info, success = api_client.get_novels_info_dict(config["followed_novels"])
            if success:
                # First entry is the result count
                novels_list = new_novel_info[1:]
                for novel in novels_list:
                    updated = history_manager.check_add_novel(novel)
                    if updated:
                        updated_number += 1
                if updated_number == 0 and config["verbose"]:
                    notification_pusher.no_updates_notification()
        time.sleep(config["sleep_time"])