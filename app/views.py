from flask import render_template
from app import app
from .request import get_sources,get_articles
from .models import articles

#Index page view function
@app.route('/')
def index():
  """
  View root page function that returns the index page and its data
  """
  sport_sources = get_sources('sports')
  business_sources = get_sources('business')
  technology_sources = get_sources('technology')
  general_sources = get_sources('general')
  entertainment_sources = get_sources('entertainment')
  title = "NewsBits"

  return render_template('index.html', title=title, general = general_sources)
 
@app.route('/articles/<id>')
def newsarticles(id):
  """
  View top stories page function and returns
  top stories 
  """
  title = f'{id}'
  articles_items = get_articles(id)
  print(get_articles(id))

  return render_template('articles.html',title = title, articles= articles_items)