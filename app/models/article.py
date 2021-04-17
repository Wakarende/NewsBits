class Article:
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