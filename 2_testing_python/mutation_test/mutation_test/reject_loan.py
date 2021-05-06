#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : reject_loan.py
# Author            : leejhunhong <jhunhong.lee@outlook.com>
# Date              : 06.05.2021
# Last Modified Date: 06.05.2021
# Last Modified By  : leejhunhong <jhunhong.lee@outlook.com>

def reject_loan(loan):
    if loan.amount > 250_000:
        loan.reject()

    return loan
