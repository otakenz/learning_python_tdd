#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : test_another_sum.py
# Author            : leejhunhong <jhunhong.lee@outlook.com>
# Date              : 01.05.2021
# Last Modified Date: 01.05.2021
# Last Modified By  : leejhunhong <jhunhong.lee@outlook.com>

from sum.another_sum import another_sum

def test_another_sum():
    assert another_sum(3, 2) == 5
