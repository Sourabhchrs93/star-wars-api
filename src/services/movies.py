# from src.utils.json_utils import to_json, to_list_json
import requests
import json
from src.constants.constants import (
    swapi_movies_url,
    HTTP_status_200,
    HTTP_status_500
)
from src.commons.json_utils import to_json


class MoviesService:

    def __init__(self):
        self.url = swapi_movies_url

    def search(self, keyword='', page=''):
        try:
            if page:
                int(page)
        except Exception as e:
            return to_json({"message": "'page' must be a integer"}, is_error=True), HTTP_status_500

        params_added_url = "{0}?search={1}&page={2}".format(self.url, keyword, page)

        response = requests.request("GET", params_added_url)
        resp_text = json.loads(response.text)

        if response.status_code != HTTP_status_200:
            return to_json({"message": resp_text}, is_error=True), response.status_code

        return to_json(resp_text), response.status_code
