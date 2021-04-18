from app import app
import urllib.request, json
from .models import sources,articles

Articles = articles.Articles
Sources = sources.Sources

#Getting api key
apiKey = app.config['NEWS_API_KEY']

#Getting the article sources base url
base_url = app.config["NEWS_API_BASE_URL"]

#Getting the top articles from specific article source
articles_url = app.config['NEWS_API_TOP_STORIES_URL']

def get_sources(category):
  """
  Function that gets the json response to our url request
  """
  get_sources_url = base_url.format(category,apiKey)

  with urllib.request.urlopen(get_sources_url) as url:
    get_sources_data = url.read()
    get_sources_response = json.loads(get_sources_data)

    source_results = None

    if get_sources_response['sources']:
      source_results_list = get_sources_response['sources']
      source_results = process_results(source_results_list)

  return source_results

def process_results(source_list):
  """
  Function that processes the article-sources result and transforms them to a list of Objects

  Args:
    article_list: A list of dictionaries containing the article source details
  
  Returns:
    article_results: A list of article source objects
  """
  source_results = []
  for source_item in source_list:
    id = source_item.get('id')
    name = source_item.get('name')
    description = source_item.get('description')
    url = source_item.get('url')
    category = source_item.get('category')
    language = source_item.get('language')
    country = source_item.get('country')

    source_object = Sources(id, name, description, url, category, language, country)
    source_results.append(source_object)

  return source_results

def get_articles(id):
  """
  Function that returns the top stories for each news source
  """
  get_articles_url = articles_url.format(id, apiKey)
  
  with urllib.request.urlopen(get_articles_url) as url:
    get_articles_data = url.read()
    get_articles_response = json.loads(get_articles_data)

    articles_results = None

    if get_articles_response['articles']:
      articles_results_list = get_articles_response['articles']
      articles_results = process_article_results(articles_results_list)
  
  return articles_results

def process_article_results(articles_list):
  """
  Function that processes the top stories results for a article source
  """
  articles_results = []

  for article_item in articles_list:
    id = article_item.get('id')
    name = article_item.get('name')
    author = article_item.get('author')
    title = article_item.get('title')
    url = article_item.get('url')
    description= article_item.get('description')
    publishedAt = article_item.get('publishedAt')
    image = article_item.get('image')
    content = article_item.get('content')

    if image:
      article_object = Articles(id, name, author,title,url,description,publishedAt,image, content)
      articles_results.append(article_object)

  print(articles_results)
  return articles_results