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
    
class Sources:
  """
  Article class to define article source objects
  """
  def __init__(self,id,name,description,url,category,language,country):
    self.id = id
    self.name = name
    self.description = description
    self.url = url
    self.category = category
    self.language = language
    self.country = country