#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : queries.py
# Author            : leejhunhong <jhunhong.lee@outlook.com>
# Date              : 02.05.2021
# Last Modified Date: 02.05.2021
# Last Modified By  : leejhunhong <jhunhong.lee@outlook.com>

from typing import List

from pydantic import BaseModel

from blog.models import Article


class ListArticlesQuery(BaseModel):

    def execute(self) -> List[Article]:
        articles = Article.list()

        return articles

class GetArticleByIDQuery(BaseModel):
    id: str

    def execute(self) -> Article:
        article = Article.get_by_id(self.id)

        return article
