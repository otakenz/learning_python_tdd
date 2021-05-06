#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : app.py
# Author            : leejhunhong <jhunhong.lee@outlook.com>
# Date              : 07.05.2021
# Last Modified Date: 07.05.2021
# Last Modified By  : leejhunhong <jhunhong.lee@outlook.com>

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "OK"


if __name__ == "__main__":
    app.run()
