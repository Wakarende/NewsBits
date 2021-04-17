from app import app
import urllib.request, json
from .models import article,stories

Stories = stories.Stories
Article = article.Article

#Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting the article sources base url
base_url = app.config["NEWS_API_BASE_URL"]

#Getting the top articles from specific article source
articles_url = app.config['NEWS_API_TOP_STORIES_URL']

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

def get_top_stories(id):
  """
  Function that returns the top stories for each news source
  """
  get_top_stories_url = articles_url.format(id, api_key)
  
  with urllib.request.urlopen(get_top_stories_url) as url:
    get_stories_data = url.read()
    get_stories_response = json.loads(get_stories_data)

    stories_results = None

    if get_stories_response['stories']:
      stories_results_list = get_stories_response['stories']
      stories_results = process_results(stories_results_list)
  
  return stories_results

def process_stories(stories_list):
  """
  Function that processes the top stories results for a article source
  """
  stories_results = []

  for stories_item in stories_list:
    name = stories_item.get('name')
    author = stories_item.get('author')
    title = stories_item.get('title')
    url = stories_item.get('url')
    description= stories_item.get('description')
    publishedAt = stories_item.get('publishedAt')
    image = stories_item.get('image')

    if image:
      stories_object = Stories(author,title,url,description,publishedAt,image)
      stories_results.append(stories_object)

  return stories_results