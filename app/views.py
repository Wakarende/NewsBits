from flask import render_template
from app import app
from .request import get_articles,get_top_stories
from .models import stories

#Index page view function
@app.route('/')
def index():
  """
  View root page function that returns the index page and its data
  """
  sport_sources = get_articles('sports')
  business_sources = get_articles('business')
  technology_sources = get_articles('technology')
  general_sources = get_articles('general')
  entertainment_sources = get_articles('entertainment')
  title = "NewsBits"

  return render_template('index.html',  general = general_sources,sports = sport_sources, business =  business_sources, entertainment = entertainment_sources, technology = technology_sources)
 
@app.route('/stories/<id>')
def stories(id):
  """
  View top stories page function and returns
  top stories 
  """
  title = f'{stories.title}'
  stories = get_top_stories(id)
  display

  return render_template('articles.html',title = title, stories=stories)