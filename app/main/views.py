from flask import render_template
from . import main
from ..request import get_sources,get_articles
# from .models import articles

#Index page view function
@main.route('/')
def index():
  """
  View root page function that returns the index page and its data
  """
  # sport_sources = get_sources('sports')
  # business_sources = get_sources('business')
  # technology_sources = get_sources('technology')
  general_sources = get_sources('general')
  # entertainment_sources = get_sources('entertainment')
  title = "NewsBits"

  return render_template('index.html', title=title, general = general_sources)
 
@main.route('/articles/<source_id>')
def articles(source_id):
  """
  View top stories page function and returns
  top stories 
  """
  title = f'{source_id}'
  articles_items = get_articles(source_id)


  return render_template('articles.html',title = title, articles= articles_items, name = source_id)