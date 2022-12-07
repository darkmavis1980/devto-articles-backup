import sys
import requests
import os
from lib.conf import getConfig

config = getConfig()
foremApi = config.get('DEVTO', 'API')
perPage = config.get('DEVTO', 'PER_PAGE')
destFolder = config.get('LOCAL', 'DEST_FOLDER')
fileFormat = config.get('LOCAL', 'FORMAT')

class MissingIdException(Exception):
    pass

def addArticleMeta(article, file):
    articleId = article["id"]
    url = article["url"]
    published_at = article["published_at"]
    tags = article["tags"]

    file.write("<!-- ID:{} -->\n".format(articleId))
    file.write("<!-- url:{} -->\n".format(url))
    file.write("<!-- published_at:{} -->\n".format(published_at))
    file.write("<!-- tags:{} -->\n".format(tags))

def fetchPost(articleId):
    try:
        if articleId is None and not articleId.isNumeric():
            raise MissingIdException

        articleUrl = "{}articles/{}".format(foremApi, articleId)
        response = requests.get(articleUrl)
        article = response.json()
        print("Fetching article: {}".format(article["slug"]))
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
    except MissingIdException:
        print("ID is not passed")
    except:
        print("Cannot load article id {}".format(articleId))


def fetchPosts():
    username = sys.argv[1]
    allArticlesUrl = "{}articles?username={}&page=1&per_page={}".format(foremApi, username, perPage)
    response = requests.get(allArticlesUrl)
    listArticles = response.json()
    for article in listArticles:
        fetchPost(article['id'])
    print("Done!")

if __name__ == "__main__":
    fetchPosts()