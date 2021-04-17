import unittest
from models import stories
Stories = stories.Stories

class StoriesTest(unittest.TestCase):
  """
  Test class to test behaviour of the stories class
  """
  def setUp(self):
    """
    Set up method that will run before every test

    """
    self.new_story = Stories("New York Times", "Megan Specia", "Prince Philip's Funeral Live Updates: Streaming and Start Time - The New York Times", "The Duke of Edinburgh, the husband of Queen Elizabeth II and patriarch of the House of Windsor, died last week at age 99.", "https://www.nytimes.com/live/2021/04/17/world/prince-philip-funeral", "https://static01.nyt.com/images/2021/04/17/world/17philip-funeral-promo5/17philip-funeral-promo5-facebookJumbo.jpg", "2021-04-17T10:25:09Z")

  def test_instance(self):
    self.assertTrue(isinstance(self.new_story, Stories))

if __name__ == '__main__':
  unittest.main()