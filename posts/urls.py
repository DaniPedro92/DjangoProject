from django.urls import path
#from . import views
from .views import Home, CreatePost
"""
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
"""
app_name = 'posts'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('add/', CreatePost.as_view(), name='add'),
]