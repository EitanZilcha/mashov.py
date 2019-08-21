from mashov import fetch_schools
from mashov.school import School
import pytest
import responses

API_BASE_URL = "https://web.mashov.info/api"


@pytest.fixture
def school_fields():
    return ["semel", "name", "years"]


def test_schools_backend(school_fields):
    import requests
    schools = requests.get(f"{API_BASE_URL}/schools").json()
    assert set(school_fields).issubset(schools[0].keys())


@pytest.fixture
def school_list():
    return [{"semel": 123123, "name": "Testing School", "years": [2019, 2020]}]


@responses.activate
def test_schools_parsing(school_list):
    responses.add(responses.GET, f"{API_BASE_URL}/schools", json=school_list)
    parsed_school = fetch_schools()[0]
    example_school = school_list[0]
    assert isinstance(parsed_school, School)
    assert parsed_school.id == example_school["semel"]
    assert parsed_school.name == example_school["name"]
    assert parsed_school.years == example_school["years"]
