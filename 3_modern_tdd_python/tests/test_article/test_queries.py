#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : test_queries.py
# Author            : leejhunhong <jhunhong.lee@outlook.com>
# Date              : 02.05.2021
# Last Modified Date: 02.05.2021
# Last Modified By  : leejhunhong <jhunhong.lee@outlook.com>

from blog.models import Article
from blog.queries import ListArticlesQuery, GetArticleByIDQuery


def test_list_articles():
    """
    GIVEN 2 articles stored in the database
    WHEN the execute method is called
    THEN it should return 2 articles
    """
    Article(
            author = 'jane@doe.com',
            title = 'New Article',
            content = 'SUper extra awesome article'
            ).save()
    Article(
            author = 'jane@doe.com',
            title = 'Another Article',
            content = 'SUper awesome article'
            ).save()

    query = ListArticlesQuery()

    assert len(query.execute()) == 2


def test_get_article_by_id():
    """
    GIVEN ID of article stored in the database
    WHEN the execute method is called on GetArticleByIDQuery with id set
    THEN it should return the article with the same id
    """
    article = Article(
            author = 'jane@doe.com',
            title = 'New Article',
            content = 'Super extra awesome article'
            ).save()

    query = GetArticleByIDQuery(
            id = article.id
            )

    assert query.execute().id == article.id
