#! /usr/bin/env python3

import requests
import os
import argparse

from lib.conf import getConfig

config = getConfig()
foremApi = config.get("DEVTO", "API")
perPage = config.get("DEVTO", "PER_PAGE")
destFolder = config.get("LOCAL", "DEST_FOLDER")
fileFormat = config.get("LOCAL", "FORMAT")

parser = argparse.ArgumentParser(description="Fetches articles from Dev.to APIs")
parser.add_argument("username", metavar="U", type=str,
                    help="the username to fetch")
parser.add_argument("-p", "--page", type=int, help="Set the page to download", default=1)
parser.add_argument("-l", "--limit", type=int, help="Limit of articles to fetch per request", default=perPage)

class MissingIdException(Exception):
    pass

'''
Add html comment as meta information about the article
'''
def addArticleMeta(article, file):
    articleId = article["id"]
    url = article["url"]
    published_at = article["published_at"]
    tags = article["tags"]

    file.write("<!-- ID:{} -->\n".format(articleId))
    file.write("<!-- url:{} -->\n".format(url))
    file.write("<!-- published_at:{} -->\n".format(published_at))
    file.write("<!-- tags:{} -->\n".format(tags))

'''
Take the article JSON data, and save it in a file, by default in MarkDown
'''
def saveArticle(article):
    body = "body_markdown"
    extension = "md"
    if fileFormat != "markdown":
        body = "body_html"
        extension = "html"
    if not os.path.exists(destFolder):
        print("Createing missing folder {}".format(destFolder))
        os.mkdir(destFolder)
    with open("{}/{}-{}.{}".format(destFolder, article["id"], article["slug"], extension), "w") as outFile:
        addArticleMeta(article, outFile)
        outFile.write("# {}\n\r".format(article['title']))
        outFile.write(article[body])
        outFile.close()

'''
Take the article ID as input and fetch the data from the API
'''
def fetchArticle(articleId):
    try:
        if articleId is None and not articleId.isNumeric():
            raise MissingIdException

        articleUrl = "{}articles/{}".format(foremApi, articleId)
        response = requests.get(articleUrl)
        article = response.json()
        print("Fetching article: {}".format(article["slug"]))
        saveArticle(article=article)
    except MissingIdException:
        print("ID is not passed")
    except:
        print("Cannot load article id {}".format(articleId))

'''
Fetches all the articles from Dev.to for a given account
'''
def fetchArticles():
    try:
        args = parser.parse_args()
        username = args.username
        page = args.page
        limit = args.limit
        print("Fetching data from Dev.to APIs")
        allArticlesUrl = "{}articles?username={}&page={}&per_page={}".format(foremApi, username, page, limit)
        response = requests.get(allArticlesUrl)
        listArticles = response.json()
        print("Downloading articles")
        for article in listArticles:
            fetchArticle(article['id'])
        print("Done!")
    except argparse.ArgumentError:
        print("Missing some parameters")
    except:
        print("Something went wrong, maybe you mispelled something?")

if __name__ == "__main__":
    fetchArticles()