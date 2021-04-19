class Articles:
  """
  Article class to define Top Stories object
  """
  def __init__(self,author, title, url, publishedAt, urlToImage,description,content):
    self.author = author
    self.title = title
    self.description = description
    self.url = url
    self.publishedAt = publishedAt
    self.urlToImage = urlToImage
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