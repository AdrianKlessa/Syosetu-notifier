import requests
import yaml
main_url = "https://api.syosetu.com/novelapi/api/"

mitsuba_monogatari_id = "n0388ee"

test_id1="n0001a"
test_id2="n1111b"
test_id3="n9999d"

print("-".join([test_id1]))

print("-".join([test_id1,test_id2]))
print("-".join([test_id1,test_id2,test_id3]))


# Response content for one example request (one novel) info was 573KB
def get_novels_info(novel_id_list):
    """

    :param novel_id_list: List of strings defining the novel ncodes
    :return: yaml-formatted text and boolean indicating if the request was successful
    """
    novels_string = "-".join(novel_id_list) # Novel ids are joined by "-" in the api (e.g. /api/?ncode=n0001a-n1111b-n9999d)
    response = requests.get(main_url, params={"ncode": novels_string})
    if response.status_code==200:
        response_data = response.text
        success = True
    else:
        response_data = None
        success = False
    return (response_data,success)

def get_novels_info_dict(novel_id_list):
    """

    :param novel_id_list: List of strings defining the novel ncodes
    :return: python dictionary with novel information and boolean indicating if the request was successful
    """
    novels_string = "-".join(novel_id_list) # Novel ids are joined by "-" in the api (e.g. /api/?ncode=n0001a-n1111b-n9999d)
    response = requests.get(main_url, params={"ncode": novels_string})
    if response.status_code==200:
        python_dict_response = yaml.load(response.text, Loader=yaml.BaseLoader)
        success = True
    else:
        python_dict_response = None
        success = False
    return (python_dict_response,success)



print(get_novels_info_dict([mitsuba_monogatari_id]))
