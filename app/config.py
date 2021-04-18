class Config:
  """
  General configuration parent class
  """
  # NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey=NEWS_API_KEY'
  # NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey=256d91dfd02f4e82a29bd3ad22a4b56b'
  NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
  NEWS_API_TOP_STORIES_URL = 'http://newsapi.org/v2/top-headlines?sources={}&apiKey={}'

class ProdConfig(Config):
  """
  Production configuration class

  Args:
    Config: The parent configuration class with General configuration settings
  """
  pass

class DevConfig(Config):
  """
  Development configuration child class
  Args:
    Config: The parend configuration class with General configuration settings
  """
  DEBUG = True
