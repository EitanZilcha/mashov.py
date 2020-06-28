from datetime import datetime
import pytest
import re
import responses

from mashov.client_helper_funcs import get_grades
from mashov.models import Grade, School
from mashov.username_password_client import UsernamePasswordClient

API_BASE_URL = "https://web.mashov.info/api"

# None accepted to deal with non-authorized client
grade_url_ex = re.compile(
    f"{API_BASE_URL}/students/(\b[0-9a-f]{8}\b-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-\b[0-9a-f]{12}\b|None)/grades"
)


@pytest.fixture
def grade_list():
    return [{
        "gradingEventId": 123,
        "grade": 100,
        "rangeGrade": "Great",
        "timestamp": "2019-08-21T19:45:45",
        "teacherName": "Test Teacher",
        "groupId": 1234,
        "groupName": "Test Group",
        "subjectName": "Test Subject",
        "eventDate": "2019-08-21T00:00:00",
        "id": 123,
        "gradingPeriod": 0,
        "gradingEvent": "Test Event",
        "gradeTypeId": 1,
        "gradeType": "Test Type"
    }]


# TODO: Use client fixture from other test file
@pytest.fixture
def username_password_client():
    return UsernamePasswordClient(
        school=School.from_params(**{
            "semel": 123123,
            "name": "Testing School",
            "years": [2019, 2020]
        }),
        username="test_username",
        password="test_password")


@responses.activate
def test_get_grades(grade_list, username_password_client):
    responses.add(responses.GET, grade_url_ex, json=grade_list)
    grades = get_grades(username_password_client.session,
                        username_password_client.guid)
    assert isinstance(grades, list)
    grade = grades[0]
    example_grade = grade_list[0]
    assert isinstance(grade, Grade)
    assert grade.event_id == example_grade["gradingEventId"]
    assert grade.grade == example_grade["grade"]
    assert grade.grade_range == example_grade["rangeGrade"]
    assert grade.timestamp == datetime.strptime(example_grade["timestamp"],
                                                "%Y-%m-%dT%H:%M:%S")
    assert grade.teacher_name == example_grade["teacherName"]
    assert grade.group_id == example_grade["groupId"]
    assert grade.group_name == example_grade["groupName"]
    assert grade.subject == example_grade["subjectName"]
    assert grade.event_date == datetime.strptime(example_grade["eventDate"],
                                                 "%Y-%m-%dT%H:%M:%S").date()
    assert grade.id == example_grade["id"]
    assert grade.grading_period == example_grade["gradingPeriod"]
    assert grade.grading_event == example_grade["gradingEvent"]
    assert grade.type_id == example_grade["gradeTypeId"]
    assert grade.type == example_grade["gradeType"]
