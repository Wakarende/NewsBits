import urllib.request, json
from .models import Sources, Articles


api_key = None
base_url = None
base_article_url = None

def configure_request(app):
  global api_key,base_url,base_article_url
  #Getting api key
  api_key = app.config['NEWS_API_KEY']

  #Getting the article sources base url
  base_url = app.config['NEWS_API_BASE_URL']

  #Getting the top articles from specific article source
  base_article_url = app.config['NEWS_ARTICLES_URL']

  # search_url = app.config["SEARCH_API_URL"]

def get_sources(category):
  """
  Function that gets the json response to our url request
  """
  get_sources_url = base_url.format(category,api_key)
  print(get_sources_url)
  with urllib.request.urlopen(get_sources_url) as url:
    get_sources_data = url.read()
    get_sources_response = json.loads(get_sources_data)

    sources_results = None

    if get_sources_response['sources']:
      sources_results_list = get_sources_response['sources']
      sources_results = process_sources_results(sources_results_list)

  return sources_results

def process_sources_results(sources_list):
  """
  Function that processes the article-sources result and transforms them to a list of Objects

  Args:
    article_list: A list of dictionaries containing the article source details
  
  Returns:
    article_results: A list of article source objects
  """
  sources_results = []
  for source_item in sources_list:
    id = source_item.get('id')
    name = source_item.get('name')
    description = source_item.get('description')
    url = source_item.get('url')
    category = source_item.get('category')
    language = source_item.get('language')
    country = source_item.get('country')

    source_object = Sources(id, name, description, url, category, language, country)
    sources_results.append(source_object)

  return sources_results

def get_articles(id):
  '''
  Function that gets the json Articles response to our url request
  '''
  get_articles_url = base_article_url.format(id,api_key)
  print(get_articles_url)
  with urllib.request.urlopen(get_articles_url) as url:
    get_articles_data = url.read()
    get_articles_response = json.loads(get_articles_data)

    articles_results = None

    if get_articles_response['articles']:
      articles_results_list = get_articles_response['articles']
      articles_results = process_articles_results(articles_results_list)

  return articles_results

def process_articles_results(articles_list):
  """
  Function  that processes the articles result and transform them to a list of Objects
  Args:
    articles_list: A list of dictionaries that contain sources details
  Returns :
    articles_results: A list of source objects
    """
    
  articles_results = []
  for article_item in articles_list:
    author = article_item.get('author')
    title = article_item.get('title')
    description = article_item.get('description')
    url = article_item.get('url')
    urlToImage = article_item.get('urlToImage')
    publishedAt = article_item.get('publishedAt')
    content = article_item.get('content')

    if urlToImage:
      article_object = Articles(author, title, url, urlToImage, publishedAt, content, description)
      articles_results.append(article_object)

  return articles_results


