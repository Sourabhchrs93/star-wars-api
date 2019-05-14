from flask_restful import Resource
from flask import request

from src.services.planets import PlanetsService
from flask_restful_swagger import swagger


class PlanetsResource(Resource):

    def __init__(self):
        self.planet_service = PlanetsService()

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
