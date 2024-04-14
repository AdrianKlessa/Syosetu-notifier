import requests
import json

main_url = "https://api.syosetu.com/novelapi/api/"

mitsuba_monogatari_id = "n0388ee"

test_id1="n0001a"
test_id2="n1111b"
test_id3="n9999d"

print("-".join([test_id1]))

print("-".join([test_id1,test_id2]))
print("-".join([test_id1,test_id2,test_id3]))


def get_novels_info(novel_id_list):
    """

    :param novel_id_list: List of strings defining the novel ncodes
    :return: jsonized response
    """
    novels_string = "-".join(novel_id_list) # Novel ids are joined by "-" in the api (e.g. /api/?ncode=n0001a-n1111b-n9999d)
    response = requests.get(main_url, params={"ncode": novels_string})
    response_data = response.text # TODO: Validate response code
    return response_data

print(get_novels_info([mitsuba_monogatari_id]))
