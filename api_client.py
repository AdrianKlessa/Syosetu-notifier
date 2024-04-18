import requests
import yaml
import notification_pusher

main_url = "https://api.syosetu.com/novelapi/api/"

mitsuba_monogatari_id = "n0388ee"

test_id1 = "n0001a"
test_id2 = "n1111b"
test_id3 = "n9999d"

print("-".join([test_id1]))

print("-".join([test_id1, test_id2]))
print("-".join([test_id1, test_id2, test_id3]))

# Response content for one full example request (one novel) info was 573KB
# Down to 88 KB when limiting response parameters

def get_novels_info_dict(novel_id_list,limit_parameters=True):
    """
    :param limit_parameters: If True, limits request to only ask for the fields needed by the application
    :param novel_id_list: List of strings defining the novel ncodes
    :return: python dictionary with novel information and boolean indicating if the request was successful
    """
    novels_string = "-".join(
        novel_id_list)  # Novel ids are joined by "-" in the api (e.g. /api/?ncode=n0001a-n1111b-n9999d)

    request_params = {"ncode": novels_string}
    if limit_parameters:
        # title, ncode, writer, general_firstup, general_lastup, novelupdated_at
        of_parameter = "-".join(["t", "n", "w", "gf", "gl", "nu"])
        request_params["of"]=of_parameter
    try:
        response = requests.get(main_url, params=request_params)
        if response.status_code == 200:
            python_dict_response = yaml.load(response.text, Loader=yaml.BaseLoader)
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
    return (python_dict_response, success)


print(get_novels_info_dict([mitsuba_monogatari_id]))
