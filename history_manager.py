import datetime
import json
from dateutil.parser import parse

import notification_pusher

HISTORY_FILE_NAME = "history.json"


def check_create_history_file():
    try:
        # If file exists don't create it again
        with open(HISTORY_FILE_NAME, 'r', encoding='utf-8') as f:
            pass  # do nothing
    except FileNotFoundError:
        create_history_file()


def create_history_file():
    with open(HISTORY_FILE_NAME, 'w+', encoding='utf-8') as f:
        print("Creating file")
        history_dict = {"last_history_update_utc": str(
            datetime.datetime.min), "test": "test"}
        print(history_dict)
        json.dump(history_dict, f, ensure_ascii=False, indent=4, default=str)


def check_add_novel(retrieved_info):
    """
    Check history file to compare new novel data with old
    :param novel_id: ncode of the novel to check in the history file
    :param retrieved_info: newly retrieved info of the novel to compare with
    :return: None
    """
    novel_id = retrieved_info["ncode"]
    try:
        with open(HISTORY_FILE_NAME, 'r', encoding='utf-8') as f:
            history_data = json.load(f)
            if novel_id not in history_data:
                history_data[novel_id] = retrieved_info
                notification_pusher.novel_modified_notification()
            else:
                old_novel_information = history_data[novel_id]
                compare_data(old_novel_information, retrieved_info)
                history_data[novel_id] = retrieved_info
            history_data["last_history_update_utc"] = str(datetime.datetime.now(datetime.timezone.utc))
        with open(HISTORY_FILE_NAME, 'w+', encoding='utf-8') as f:
            json.dump(history_data, f, ensure_ascii=False, indent=4, default=str)

    except FileNotFoundError:
        notification_pusher.history_file_not_found_notification()


def compare_data(old_novel_data, new_novel_data):
    # Convert both from str to datetime and compare
    old_novelupdated_at = parse(old_novel_data["novelupdated_at"])
    new_novelupdated_at = parse(new_novel_data["novelupdated_at"])

    old_general_lastup = parse(old_novel_data["general_lastup"])
    new_general_lastup = parse(new_novel_data["general_lastup"])

    if new_general_lastup > old_general_lastup:
        notification_pusher.new_chapter_notification()
    elif new_novelupdated_at > old_novelupdated_at:
        notification_pusher.novel_modified_notification()


def get_last_history_updated_utc():
    try:
        with open(HISTORY_FILE_NAME, 'r', encoding='utf-8') as f:
            history_data = json.load(f)
            return history_data["last_history_update_utc"]
    except FileNotFoundError:
        notification_pusher.history_file_not_found_notification()


def can_update_already():
    last_update_time = get_last_history_updated_utc()
    print(last_update_time)
    last_update_time = datetime.datetime.strptime(last_update_time, '%Y-%m-%d %H:%M:%S.%f%z')
    current_time = datetime.datetime.now(datetime.timezone.utc)
    time_difference = current_time - last_update_time
    # Arbitrarily chose half-hour time difference
    if time_difference.total_seconds() > 1800:
        return True
    return False
