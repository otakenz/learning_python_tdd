#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : test_app.py
# Author            : leejhunhong <jhunhong.lee@outlook.com>
# Date              : 07.05.2021
# Last Modified Date: 07.05.2021
# Last Modified By  : leejhunhong <jhunhong.lee@outlook.com>

import pytest

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_home(client):
    response = client.get("/")

    assert response.status_code == 200
