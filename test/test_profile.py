import pytest
import responses

from pywisetransfer.profile import Profile


@pytest.fixture
def profile_list_response():
    return [
        {
            "id": 0,
            "type": "personal",
            "details": {
                "firstName": "Oliver",
                "lastName": "Wilson",
                "dateOfBirth": "1977-07-01",
                "phoneNumber": "+3725064992",
                "avatar": "",
                "occupation": "",
                "occupations": None,
                "primaryAddress": None,
                "firstNameInKana": None,
                "lastNameInKana": None,
            },
        },
        {
            "id": 1,
            "type": "business",
            "details": {
                "name": "ABC Logistics Ltd",
                "registrationNumber": "12144939",
                "acn": None,
                "abn": None,
                "arbn": None,
                "companyType": "LIMITED",
                "companyRole": "OWNER",
                "descriptionOfBusiness": "CHARITY_AND_NOT_FOR_PROFIT",
                "webpage": "https://abc-logistics.com",
                "primaryAddress": None,
                "businessCategory": "CHARITY_AND_NOT_FOR_PROFIT",
                "businessSubCategory": "CHARITY_ALL_ACTIVITIES",
            },
        },
    ]


@responses.activate
def test_profile_list_unfiltered(profile_list_response):
    responses.add(
        responses.GET,
        "https://api.sandbox.transferwise.tech/v1/profiles",
        json=profile_list_response,
    )

    endpoint = Profile()
    results = list(endpoint.list())

    assert len(results) == 2


@responses.activate
def test_profile_list_type_filtered(profile_list_response):
    responses.add(
        responses.GET,
        "https://api.sandbox.transferwise.tech/v1/profiles",
        json=profile_list_response,
    )

    endpoint = Profile()
    results = list(endpoint.list(type="business"))

    assert len(results) == 1
