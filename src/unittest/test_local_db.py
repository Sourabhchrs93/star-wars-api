from unittest import TestCase
import unittest

from src.services.db_services import LocalDatabase


class TestDBService(TestCase):
    def setUp(self):
        self.local_db_path = 'local-db-test/db_test.csv'
        self.local_db_service = LocalDatabase(self.local_db_path)
        self.writable_planet_data = "planets,Alderaan,https://swapi.co/api/planets/2/"
        self.writable_movie_data = "movies,A New Hope,https://swapi.co/api/films/1/"
        self.fav_type_is_planet = 'planets'
        self.fav_type_is_movie = 'movies'
        self.fav_type_is_both = 'all'

    def tearDown(self):
        pass

    def test_local_db_service(self):
        # insert planet data
        assert self.local_db_service.write(self.writable_planet_data) is True

        # insert movie data
        assert self.local_db_service.write(self.writable_movie_data) is True

        # inserting duplicate planet data
        assert self.local_db_service.write(self.writable_planet_data) is False

        # read planet data
        data_out, count = self.local_db_service.read(self.fav_type_is_planet)
        assert count == 1

        # read planet data
        data_out, count = self.local_db_service.read(self.fav_type_is_movie)
        assert count == 1

        # read planet data
        data_out, count = self.local_db_service.read(self.fav_type_is_both)
        assert count == 2

        # clear local test db
        assert self.local_db_service.clean() is True


if __name__ == '__main__':
    unittest.main()
