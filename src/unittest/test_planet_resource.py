from unittest import TestCase
import unittest

from src.services.planets import PlanetsService
from src.constants.constants import(
    HTTP_status_200,
    HTTP_status_404
)


class TestPlanetService(TestCase):
    def setUp(self):
        self.planet_service = PlanetsService()
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

    def test_planet_service(self):
        # test with valid params
        keyword = self.valid_input['keyword']
        page = self.valid_input['page']
        data, status_code = self.planet_service.search(keyword, page)
        assert status_code == HTTP_status_200

        # test with empty params
        keyword = self.empty_input['keyword']
        page = self.empty_input['page']
        data, status_code = self.planet_service.search(keyword, page)
        assert status_code == HTTP_status_200

        # test with invalid page number
        keyword = self.invalid_page_input['keyword']
        page = self.invalid_page_input['page']
        data, status_code = self.planet_service.search(keyword, page)
        assert status_code == HTTP_status_404


if __name__ == '__main__':
    unittest.main()
