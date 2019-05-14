from src.constants.constants import (
    HTTP_status_201,
    HTTP_status_422
)
from src.commons.json_utils import to_json


class LocalDatabase():

    def __init__(self, file_path):
        self.file_path = file_path

    def is_exist(self, data_str):
        data_str = "{0}\n".format(data_str)
        with open(self.file_path, 'r') as f:
            file_data = f.readlines()
        if data_str in file_data:
            return True
        else:
            return False

    def write(self,data_str):
        if not self.is_exist(data_str):
            with open(self.file_path, 'a') as f:
                f.write('{0}\n'.format(data_str))
            return to_json({"message": "saved to DataBase"}), HTTP_status_201
        else:
            return to_json({"message": "entry already exits in DataBase"}), HTTP_status_422

