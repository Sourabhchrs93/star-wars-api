from flask_restful import Resource
from flask import request

from src.services.movies import MoviesService
from flask_restful_swagger import swagger


class MoviesResource(Resource):

    def __init__(self):
        self.movies_service = MoviesService()

    @swagger.operation(
        nickname='movies list',
        notes='fetch movies list search by Title with pagination',
        parameters=[
            {
                "name": "keyword",
                "dataType": "string",
                "paramType": "query",
                "description": "search parameter that filters movies by Title"
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
        resp = self.movies_service.search(keyword, page)
        return resp
