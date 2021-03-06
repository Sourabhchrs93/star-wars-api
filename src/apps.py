from flask import Flask
from flask_restful import Api
from flask_restful_swagger import swagger

from src.resources.planets import PlanetsResource
from src.resources.movies import MoviesResource
from src.resources.favourites import FavouriteResource

app = Flask(__name__)
api = swagger.docs(
    Api(app),
    apiVersion='1.0.0',
    api_spec_url='/api/spec',
    description="docs for star-wars api")


@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"


api.add_resource(PlanetsResource, '/api/planets')
api.add_resource(MoviesResource, '/api/movies')
api.add_resource(FavouriteResource, '/api/favourites/<string:fav_type>')


if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0', port=8000)
