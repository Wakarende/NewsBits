from app import app
import urllib.request, json
from .models import article

Article = article.Article

#Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting the article sources base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_articles(category):
  """
  Function that gets the json response to our url request
  """
  get_articles_url = base_url.format(category,api_key)

  with urllib.request.urlopen(get_articles_url) as url:
    get_articles_data = url.read()
    get_articles_response = json.loads(get_articles_data)

    article_results = None

    if get_articles_response['sources']:
      article_results_list = get_articles_response['sources']
      article_results = process_results(article_results_list)

  return article_results

def process_results(article_list):
  """
  Function that processes the article-sources result and transforms them to a list of Objects

  Args:
    article_list: A list of dictionaries containing the article source details
  
  Returns:
    article_results: A list of article source objects
  """
  article_results = []
  for article_item in article_list:
    id = article_item.get('id')
    name = article_item.get('name')
    description = article_item.get('description')
    url = article_item.get('url')
    category = article_item.get('category')
    language = article_item.get('language')
    country = article_item.get('country')

    article_object = Article(id, name, description, url, category, language, country)
    article_results.append(article_object)

  return article_results