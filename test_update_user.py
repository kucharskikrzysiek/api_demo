#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Krzysztof Kucharski"

import allure
import pytest
import requests
from datetime import datetime
from http import HTTPStatus
import common_methods
from data.test_data import generate_user_data


@pytest.fixture(scope="module", autouse=True)
def context():
    user_data = generate_user_data()
    _response = response(user_data)
    return _response, user_data


def response(user_data):
    _response = requests.patch(f"{common_methods.BASE_API_URL}/1", json=user_data, headers=common_methods.HEADERS)
    allure.attach(str(_response.json()), f'response_content_{datetime.now().strftime("%Y%m%d_%H%M%S")}')
    return _response


def test_status_code(context):
    _response, user_data = context
    common_methods.test_status_code(_response, [HTTPStatus.OK, HTTPStatus.NO_CONTENT])


@pytest.mark.parametrize('name', ["id", "name", "username", "email", "address", "phone", "website", "company"])
def test_check_parameter_in_response(context, name):
    _response, user_data = context
    with allure.step(f'check if in the response {name} parameter exist'):
        assert _response.json()[name], f"In the response parameter {name} has not been found"
        if name == "address":
            check_lower_parameter_level(name, ["street", "city", "zipcode"], _response)
        elif name == "company":
            check_lower_parameter_level(name, ["name"], _response)


def check_lower_parameter_level(name, parameters, _response):
    for parameter in parameters:
        with allure.step(f'check if in the response {parameter} lower parameter level exist'):
            assert _response.json()[name][parameter], f"In the response parameter {name} has not been found"


def test_updated_user(context):
    _response = context[0]
    with allure.step('check if user has been updated'):
        pytest.skip('jsonplaceholder does not update an entry\n'
                    'Important: the resource will not be really updated on the server but it will be faked as if.')
        # request https://jsonplaceholder.typicode.com/users?id=<updated_user_id>
