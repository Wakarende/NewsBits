from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources,get_articles, search_article
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
  search_article = request.args.get('article_query')

  if search_article:
    return redirect(url_for('search',aritcle_name = search_article))
  else:
    return render_template('index.html', title=title, general = general_sources)

  
 
@main.route('/articles/<id>')
def articles(id):
  """
  View  page function and returns
  articles
  """
  title = f'{id}'
  articles_source = get_articles(id)

  return render_template('articles.html',title = title, articles= articles_source, name = id)

# @main.route('/search/<article_name>')
# def search(article_name):
#   """
#   View function that displays articles search results
#   """
#   article_name_list = article_name.split("")
#   article_name_format = "+".join(article_name_list)
#   searched_article = search_article(article_name_format)
#   title = f"{article_name} search results"

#   return render_template('search.html', articles=searched_article)

# @main.route('/article/<id>')
# def article(id):

#   '''
#   View article page function that returns the article details page and its data
#   '''
#   articles_items = get_articles(sourcesId)
#   title = f'{id} | News Articles'
#   return render_template('articles.html',title = title,articles = articles_items)
