import urllib.request, json
from .models import Sources, Articles


apiKey = None
base_url = None
articles_url = None

def configure_request(app):
  global apiKey,base_url,articles_url,search_url
  #Getting api key
  apiKey = app.config['NEWS_API_KEY']

  #Getting the article sources base url
  base_url = app.config["NEWS_API_BASE_URL"]

  #Getting the top articles from specific article source
  articles_url = app.config["NEWS_ARTICLES_URL"]

  search_url = app.config["SEARCH_API_URL"]

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
      source_results = process_sources_results(source_results_list)

  return source_results

def process_sources_results(source_list):
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

def search_article(article_name):
  """
  get json request to our url request

  """
  search_article_url = search_url.format(article_name,apiKey)
  print(search_article_url)

  with urllib.request.urlopen(search_article_url) as url:
    search_article_data = url.read()
    serach_article_response = json.loads(search_article_data)

    search_article_results = None

    if serach_article_response['articles']:
      search_article_results_list = serach_article_response['articles']
      search_article_results = process_articles_results(search_article_results_list)

  return search_article_results
  

def get_articles(id):
  '''
  Function that gets the json Articles response to our url request
  '''
  get_articles_url = articles_url.format(id,apiKey)

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
    id = article_item.get('id')
    author = article_item.get('author')
    title = article_item.get('title')
    description = article_item.get('description')
    url = article_item.get('url')
    urlToImage = article_item.get('urlToImage')
    publishedAt = article_item.get('publishedAt')
    content = article_item.get('content')

    if urlToImage:
      article_object = Articles(id, author, title, url, urlToImage, publishedAt, content)
      articles_results.append(article_object)

  return articles_results

def date_convert(date):
  dd=date[8:10]
  mm=date[5:7]
  yyyy=date[0:4]    
  time=date[11:16]
  date_new_format= dd+"-"+mm+"-"+yyyy+"  "+time+" hrs"
  return date_new_format