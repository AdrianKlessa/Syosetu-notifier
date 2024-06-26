import requests
import yaml
import notification_pusher

main_url = "https://api.syosetu.com/novelapi/api/"


# Response content for one full example request (one novel) info was 573KB
# Down to 88 KB when limiting response parameters

def get_novels_info_dict(novel_id_list, limit_parameters=True):
    """
    Gets information about the provided novels from Syosetu API. Notes about the datetimes retrieved:

    novelupdated_at is relevant to all modifications for the novel (typo corrections etc.)
    general_firstup is when the novel was first uploaded / added to syosetu
    general_lastup is updated when a new chapter is added, but NOT when modifications are made to existing chapters

    :param limit_parameters: If True, limits request to only ask for the fields needed by the application
    :param novel_id_list: List of strings defining the novel ncodes
    :return: python dictionary with novel information and boolean indicating if the request was successful
    """
    if len(novel_id_list) == 0:
        return None, False

    novels_string = "-".join(
        novel_id_list)  # Novel ids are joined by "-" in the api (e.g. /api/?ncode=n0001a-n1111b-n9999d)

    request_params = {"ncode": novels_string}
    if limit_parameters:
        # title, ncode, writer, general_firstup, general_lastup, novelupdated_at
        of_parameter = "-".join(["t", "n", "w", "gf", "gl", "nu"])
        request_params["of"] = of_parameter
    try:
        print("Getting novel info from Syosetu API...")
        response = requests.get(main_url, params=request_params)
        if response.status_code == 200:
            python_dict_response = yaml.safe_load(response.text)
            success = True
        else:
            python_dict_response = None
            success = False
    except requests.exceptions.Timeout as errt:
        python_dict_response = None
        success = False
        notification_pusher.custom_error_notification("Connection timeout while getting novel info!", repr(errt))
    except requests.exceptions.TooManyRedirects as errtmr:
        python_dict_response = None
        success = False
        notification_pusher.custom_error_notification("Too Many Redirects while getting novel info!", repr(errtmr))
    except requests.exceptions.RequestException as e:
        python_dict_response = None
        success = False
        notification_pusher.custom_error_notification("Error encountered while getting novel info!", repr(e))
    return python_dict_response, success
