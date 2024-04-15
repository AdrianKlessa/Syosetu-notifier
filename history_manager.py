import datetime
import json
from dateutil.parser import parse

import notification_pusher

HISTORY_FILE_NAME = "history.json"


def check_create_history_file():
    try:
        # If file exists don't create it again
        with open(HISTORY_FILE_NAME, 'r') as f:
            pass  # do nothing
    except FileNotFoundError:
        with open(HISTORY_FILE_NAME, 'a+') as f:
            json.dump(dict(), f, ensure_ascii=False, indent=4)
    finally:
        pass


def check_add_novel(novel_id, retrieved_info):
    """
    Check history file to compare new novel data with old
    :param novel_id: ncode of the novel to check in the history file
    :param retrieved_info: newly retrieved info of the novel to compare with
    :return: None
    """
    try:
        # If file exists don't create it again
        with open(HISTORY_FILE_NAME, 'r') as f:
            pass  # File exists, we're good
        with open(HISTORY_FILE_NAME, 'w+') as f:
            history_data = json.load(f, encoding='utf-8')
            if novel_id not in history_data:
                history_data[novel_id] = retrieved_info
                notification_pusher.novel_modified_notification()
            else:
                old_novel_information = history_data[novel_id]
                compare_data(old_novel_information, retrieved_info)
                history_data[novel_id] = retrieved_info
            history_data["last_history_update_utc"] = datetime.datetime.now(datetime.timezone.utc)
            json.dump(history_data, f, ensure_ascii=False, indent=4)

    except FileNotFoundError:
        notification_pusher.history_file_not_found_notification()
    finally:
        pass


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
