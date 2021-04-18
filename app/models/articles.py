class Articles:
  """
  Article class to define Top Stories object
  """
  def __init__(self, id, name, author, title, url, description, publishedAt, image,content):
    self.id = id
    self.name = name
    self.author = author
    self.title = title
    self.description = description
    self.url = url
    self.publishedAt = publishedAt
    self.image = image
    self.content = content
    
  # @classmethod
  # def disp_stories(cls,id):

  #   response = []

  #   for stories in

