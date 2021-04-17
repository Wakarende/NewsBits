from flask import render_template
from app import app
from .request import get_articles

#Index page view function
@app.route('/')
def index():
  """
  View root page function that returns the index page and its data
  """
  sport_articles = get_articles('sports')
  print(sport_articles)
  title = "NewsBits"
  return render_template('index.html', title=title, sports = sport_articles)

@app.route('/sources/<int:sources_id>')
def articles(sources_id):
  """
  View Articles page function and returns the article page and its data
  """
  title = 'Articles'
  return render_template('articles.html',title = title)