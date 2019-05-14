from flask_restful import Resource
from flask_restful_swagger import swagger

from src.services.db_services import LocalDatabase
from src.constants.constants import db_file_path
from src.commons.json_utils import to_json
from src.constants.constants import HTTP_status_200


class FavouriteResource(Resource):

    def __init__(self):
        self.db_service = LocalDatabase(db_file_path)

    @swagger.operation(
        nickname='favourite list',
        notes='fetch list of favourite planets and movies',
        parameters=[
            {
                "name": "fav_type",
                "dataType": "string",
                "paramType": "path",
                "required": True,
                "description": "accepts 'planets', 'movies', 'all'"
            }]
    )
    def get(self, fav_type):
        resp, count = self.db_service.read(fav_type)
        return to_json(resp), HTTP_status_200
