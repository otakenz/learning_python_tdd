#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : loan.py
# Author            : leejhunhong <jhunhong.lee@outlook.com>
# Date              : 06.05.2021
# Last Modified Date: 06.05.2021
# Last Modified By  : leejhunhong <jhunhong.lee@outlook.com>

from dataclasses import dataclass
from enum import Enum


class LoanStatus(str, Enum):
    PENDING = "PENDING"
    ACCEPTED = "ACCEPTED"
    REJECTED = "REJECTED"


@dataclass
class Loan:
    amount: float
    status: LoanStatus = LoanStatus.PENDING

    def reject(self):
        self.status = LoanStatus.REJECTED

    def rejected(self):
        return self.status == LoanStatus.REJECTED
