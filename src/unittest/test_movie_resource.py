from unittest import TestCase
import unittest

from src.services.movies import MoviesService
from src.constants.constants import (
    HTTP_status_200,
    HTTP_status_404
)


class TestMovieService(TestCase):
    def setUp(self):
        self.movie_service = MoviesService()
        self.valid_input = {
            'keyword': "Alderaan",
            'page': 1
        }
        self.empty_input = {
            'keyword': "",
            'page': ""
        }
        self.invalid_page_input = {
            'keyword': "al",
            'page': "abc"
        }

    def tearDown(self):
        pass

    def test_movie_service(self):
        # test with valid params
        keyword = self.valid_input['keyword']
        page = self.valid_input['page']
        data, status_code = self.movie_service.search(keyword, page)
        assert status_code == HTTP_status_200

        # test with empty params
        keyword = self.empty_input['keyword']
        page = self.empty_input['page']
        data, status_code = self.movie_service.search(keyword, page)
        assert status_code == HTTP_status_200

        # test with invalid page number
        keyword = self.invalid_page_input['keyword']
        page = self.invalid_page_input['page']
        data, status_code = self.movie_service.search(keyword, page)
        assert status_code == HTTP_status_404


if __name__ == '__main__':
    unittest.main()
