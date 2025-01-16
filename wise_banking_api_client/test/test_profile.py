from datetime import date
import pytest
import responses

from wise_banking_api_client import Client


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
                "businessCategory": "CHARITY_NON_PROFIT",
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

    endpoint = Client(api_key="test-key").profiles
    results = list(endpoint.list())

    assert len(results) == 2


@responses.activate
def test_profile_list_type_filtered(profile_list_response):
    responses.add(
        responses.GET,
        "https://api.sandbox.transferwise.tech/v1/profiles",
        json=profile_list_response,
    )

    endpoint = Client(api_key="test-key").profiles
    results = list(endpoint.list(type="business"))

    assert len(results) == 1


def test_model_has_correct_date():
    from wise_banking_api_client.model.profile import PersonalProfileDetails

    assert PersonalProfileDetails.model_example().dateOfBirth == date(1977, 7, 1)


def test_personal_profile_has_a_name():
    from wise_banking_api_client.model.profile import PersonalProfileDetails

    e = PersonalProfileDetails.model_example()
    assert e.name == e.firstName + " " + e.lastName
