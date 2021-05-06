#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : init_db.py
# Author            : leejhunhong <jhunhong.lee@outlook.com>
# Date              : 06.05.2021
# Last Modified Date: 06.05.2021
# Last Modified By  : leejhunhong <jhunhong.lee@outlook.com>

if __name__ == '__main__':
    from blog.models import Article
    Article.create_table()
