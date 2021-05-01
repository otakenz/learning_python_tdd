#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : conftest.py
# Author            : leejhunhong <jhunhong.lee@outlook.com>
# Date              : 01.05.2021
# Last Modified Date: 01.05.2021
# Last Modified By  : leejhunhong <jhunhong.lee@outlook.com>

import os
import tempfile

import pytest

from blog.models import Article

@pytest.fixture(autouse=True)
def database():
    # do something before your test
    _, file_name = tempfile.mkstemp()
    os.environ['DATABASE_NAME'] = file_name
    Article.create_table(database_name=file_name)
    yield # tests runs here
    # do something after your test
    os.unlink(file_name)
