#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Krzysztof Kucharski"

import allure


BASE_API_URL = 'https://jsonplaceholder.typicode.com/users/'
HEADERS = {"Content-type": "application/json; charset=UTF-8"}


def test_status_code(response, expected_status):
    with allure.step('check status code'):
        if type(expected_status) is list:
            assert response.status_code in expected_status, \
                f"Unexpected status code. Expected list: {str(expected_status)} Actual: {response.status_code}"
        else:
            assert response.status_code == expected_status, \
                f"Unexpected status code. Expected: {expected_status} Actual: {response.status_code}"
