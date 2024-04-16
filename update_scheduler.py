import configparser


# TODO: Utilize the "verbose" debug option to notify when getting updates even if no novel was updated

def read_config():
    config_file = configparser.ConfigParser()
    config_file.read('config.ini')
    config = dict()
    config["sleep_time"] = int(config_file["Scheduler"]["SleepTime"])
    config["verbose"] = config_file["Scheduler"].getboolean("Verbose")
    config["followed_novels"] = ''.join(config_file["Novels"]["FollowedNovels"].split()).split(',')
    return config


def get_followed_novels():
    # TODO: For each from followed novels use api_client
    pass


def main_update_loop():
    # TODO: Sanity check using the data in history file and current time here
    # TODO: In a while loop get the followed novels from file, get updates and then wait the configured amount of time
    pass


print(read_config())
