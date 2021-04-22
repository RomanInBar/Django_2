from django.urls import path
from django.views.decorators.cache import cache_page

import pagesapp.views as pagesapp

from .apps import PagesappConfig

app_name = PagesappConfig.name

urlpatterns = [
    path("", pagesapp.products, name="index"),
    path("category/<int:pk>/", cache_page(3600) (pagesapp.products), name="category"),
    path('category/<int:pk>/ajax/', cache_page(3600)(pagesapp.products_ajax)),
    path("category/<int:pk>/page/<int:page>/", pagesapp.products, name="page"),
    path("category/<int:pk>/page/<int:page>/ajax/", cache_page(3600)(pagesapp.products_ajax)),
    path("product/<int:pk>/", pagesapp.product, name="product"),
]
