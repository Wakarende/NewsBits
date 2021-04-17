from flask import render_template
from app import app
from .request import get_articles

#Index page view function
@app.route('/')
def index():
  """
  View root page function that returns the index page and its data
  """
  # sport_sources = get_articles('sports')
  # business_sources = get_articles('business')
  # technology_sources = get_articles('technology')
  general_sources = get_articles('general')
  # entertainment_sources = get_articles('entertainment')
  title = "NewsBits"

  return render_template('index.html',  general = general_sources)
 
@app.route('/sources/<int:sources_id>')
def articles(sources_id):
  """
  View Articles page function and returns the article page and its data
  """
  title = 'Articles'
  return render_template('articles.html',title = title)