from .user import user_views
from .index import index_views 
from .form import form_views

views = [user_views, index_views,form_views]

def init_app(app):
    form_views.register_blueprint(app)