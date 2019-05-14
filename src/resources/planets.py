from flask_restful import Resource
from flask import request
from flask_restful_swagger import swagger

import json

from src.services.planets import PlanetsService
from src.services.db_services import LocalDatabase

from src.swagger.swagger import LocalSave
from src.commons.json_utils import to_json
from src.constants.constants import (
    db_file_path,
    HTTP_status_201,
    HTTP_status_422
)


class PlanetsResource(Resource):

    def __init__(self):
        self.planet_service = PlanetsService()
        self.db_service = LocalDatabase(db_file_path)

    @swagger.operation(
        nickname='planets list',
        notes='fetch planets list search by Title with pagination',
        parameters=[
            {
                "name": "keyword",
                "dataType": "string",
                "paramType": "query",
                "description": "search parameter that filters planets by Title"
            },
            {
                "name": "page",
                "dataType": "integer",
                "paramType": "query",
                "description": "pagination"
            }]
    )
    def get(self):
        keyword = request.args.get('keyword', '')
        page = request.args.get('page', '')
        resp = self.planet_service.search(keyword, page)
        return resp

    @swagger.operation(
        nickname='save planet details',
        notes='save planet details in a local storage',
        parameters=[
            {
                "name": "parameters",
                "dataType": LocalSave.__name__,
                "paramType": "body",
                "required": True,
                "description": "'name' field accept planet name & 'url' is the swapi.co api to fetch planet detail"
            }
        ])
    def post(self):
        data = json.loads(request.data.decode('utf-8'))
        csv_data = "planets,{0},{1}".format(data['name'], data['url'])
        if self.db_service.write(csv_data):
            return to_json({"message": "planet saved to DataBase"}), HTTP_status_201
        else:
            return to_json({"message": "entry already exits in DataBase"}, is_error=True), HTTP_status_422
