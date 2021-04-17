class Stories:
  """
  Article class to define Top Stories object
  """
  def __init__(self, name, author, title, url, description, publishedAt, image):
    self.name = name
    self.author = author
    self.title = title
    self.description = description
    self.url = url
    self.publishedAt = publishedAt
    self.image = image
    
  # @classmethod
  # def disp_stories(cls,id):

  #   response = []

  #   for stories in

