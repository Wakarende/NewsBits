import unittest
from app.models import Sources


class SourcesTest(unittest.TestCase):
  """
  Test class to test behaviour of the article class
  """
  def setUp(self):
    """
    Set up method that will run before every test

    """
    self.new_article = Article("abc-news", "ABC News", "Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.","https://abcnews.go.com", "general", "en", "us")

  def test_instance(self):
    self.assertTrue(isinstance(self.new_article, Sources))

if __name__ == '__main__':
  unittest.main()