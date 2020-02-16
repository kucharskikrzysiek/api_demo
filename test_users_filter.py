#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Krzysztof Kucharski"

import pytest
import allure
import requests
from http import HTTPStatus
from datetime import datetime
import common_methods


@pytest.fixture(scope="module", autouse=True)
def response():
    _response = requests.get(f"{common_methods.BASE_API_URL}?username=Maxime_Nienow")
    allure.attach(str(_response.json()), f'response_content_{datetime.now().strftime("%Y%m%d_%H%M%S")}')
    return _response


def test_status_code(response):
    common_methods.test_status_code(response, HTTPStatus.OK)


def test_number_of_users(response):
    with allure.step('check number of users'):
        users_number = len(response.json())
        expected = 1
        assert users_number == expected, f"Unexpected number of users. Expected: {expected} Actual: {users_number}"


@pytest.mark.parametrize('name', ["id", "name", "username", "email", "address", "phone", "website", "company"])
def test_check_parameter_in_response(response, name):
    with allure.step(f'check if in the response {name} parameter exist'):
        assert response.json()[0][name], f"In the response parameter {name} has not been found"
