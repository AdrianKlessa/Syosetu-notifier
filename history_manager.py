import datetime
import json
from dateutil.parser import parse

import notification_pusher
import update_scheduler

HISTORY_FILE_NAME = "history.json"
MINIMUM_UPDATE_INTERVAL = 1800


def check_create_history_file():
    try:
        # If file exists don't create it again
        with open(HISTORY_FILE_NAME, 'r', encoding='utf-8') as f:
            pass  # do nothing
    except FileNotFoundError:
        create_history_file()


def create_history_file():
    with open(HISTORY_FILE_NAME, 'w+', encoding='utf-8') as f:
        print("Creating history file")
        datetime_min = datetime.datetime.min
        datetime_min = datetime_min.replace(tzinfo=datetime.timezone.utc)
        history_dict = {"last_history_update_utc": datetime_min.strftime("%Y-%m-%d %H:%M:%S.%f%z")}
        print("History dictionary after creation:")
        print(history_dict)
        json.dump(history_dict, f, ensure_ascii=False, indent=4, default=str)


def check_add_novel(retrieved_info):
    """
    Check history file to compare new novel data with old and notify about updates.
    :param retrieved_info: newly retrieved info of the novel to compare with
    :return: True if new novel info was added, False otherwise
    """
    novel_id = retrieved_info["ncode"]
    updated = False
    try:
        with open(HISTORY_FILE_NAME, 'r', encoding='utf-8') as f:
            history_data = json.load(f)
            if novel_id not in history_data:
                history_data[novel_id] = retrieved_info
                notification_pusher.novel_modified_notification(retrieved_info["writer"], retrieved_info["title"])
            else:
                old_novel_information = history_data[novel_id]
                updated = compare_data(old_novel_information, retrieved_info)
                history_data[novel_id] = retrieved_info
            history_data["last_history_update_utc"] = str(datetime.datetime.now(datetime.timezone.utc))
        with open(HISTORY_FILE_NAME, 'w+', encoding='utf-8') as f:
            json.dump(history_data, f, ensure_ascii=False, indent=4, default=str)

    except FileNotFoundError:
        notification_pusher.history_file_not_found_notification()
    finally:
        return updated


def compare_data(old_novel_data, new_novel_data):
    # Convert both from str to datetime and compare
    old_novelupdated_at = parse(old_novel_data["novelupdated_at"])
    new_novelupdated_at = parse(new_novel_data["novelupdated_at"])

    old_general_lastup = parse(old_novel_data["general_lastup"])
    new_general_lastup = parse(new_novel_data["general_lastup"])

    updated = False
    if new_general_lastup > old_general_lastup:
        notification_pusher.new_chapter_notification(new_novel_data["writer"], new_novel_data["title"])
        updated = True
    elif new_novelupdated_at > old_novelupdated_at:
        config = update_scheduler.read_config()
        if config["novel_modified_notifications"]:
            notification_pusher.novel_modified_notification(new_novel_data["writer"], new_novel_data["title"])
            updated = True
    return updated


def get_last_history_updated_utc():
    try:
        with open(HISTORY_FILE_NAME, 'r', encoding='utf-8') as f:
            history_data = json.load(f)
            return history_data["last_history_update_utc"]
    except FileNotFoundError:
        notification_pusher.history_file_not_found_notification()


def can_update_already():
    """
    Checks if the time elapsed from last update is bigger than MINIMUM_UPDATE_INTERVAL.
    Designed as an additional check to prevent sending requests to Syosetu API too often.
    :return: True if time from last update is bigger than the set global (in seconds), False otherwise
    """
    last_update_time = get_last_history_updated_utc()
    print(f"Last update time (for sanity checking): {last_update_time}")
    last_update_time = datetime.datetime.strptime(last_update_time, '%Y-%m-%d %H:%M:%S.%f%z')
    current_time = datetime.datetime.now(datetime.timezone.utc)
    time_difference = current_time - last_update_time
    # Arbitrarily chose half-hour time difference
    if time_difference.total_seconds() > MINIMUM_UPDATE_INTERVAL:
        return True
    return False
