#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Krzysztof Kucharski"

import pytest
import allure
import requests
#from datetime import datetime
from http import HTTPStatus
import common_methods


@pytest.fixture(scope="module", autouse=True)
def response():
    _response = requests.get(f"{common_methods.BASE_API_URL}/1")
    # allure.attach(str(_response.json()), f'response_content_{datetime.now().strftime("%Y%m%d_%H%M%S")}')
    # no content
    return _response


def test_status_code(response):
    common_methods.test_status_code(response, [HTTPStatus.OK, HTTPStatus.ACCEPTED, HTTPStatus.NO_CONTENT])


def test_user_has_been_removed(response):
    with allure.step('check if the user has been removed'):
        pytest.skip('jsonplaceholder does not remove user\n'
                    'Important: the resource will not be really deleted on the server but it will be faked as if.')
        # request https://jsonplaceholder.typicode.com/users?id=1
