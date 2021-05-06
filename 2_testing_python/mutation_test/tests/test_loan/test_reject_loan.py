#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : test_reject_loan.py
# Author            : leejhunhong <jhunhong.lee@outlook.com>
# Date              : 06.05.2021
# Last Modified Date: 06.05.2021
# Last Modified By  : leejhunhong <jhunhong.lee@outlook.com>

from loan import Loan
from reject_loan import reject_loan


def test_reject_loan():
    loan = Loan(amount=100_000)
    assert not reject_loan(loan).rejected()

    loan = Loan(amount=250_001)
    assert reject_loan(loan).rejected()

    loan = Loan(amount=250_000)
    assert not reject_loan(loan).rejected()
