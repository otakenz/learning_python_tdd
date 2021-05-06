#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : commands.py
# Author            : leejhunhong <jhunhong.lee@outlook.com>
# Date              : 01.05.2021
# Last Modified Date: 01.05.2021
# Last Modified By  : leejhunhong <jhunhong.lee@outlook.com>

from pydantic import BaseModel, EmailStr

from blog.models import Article, NotFound


class AlreadyExists(Exception):
    pass

class CreateArticleCommand(BaseModel):
    author: EmailStr
    title: str
    content: str

    def execute(self) -> Article:
        try:
            Article.get_by_title(self.title)
            raise AlreadyExists
        except NotFound:
            pass

        article = Article(
                author=self.author,
                title=self.title,
                content=self.title
                ).save()

        return article
