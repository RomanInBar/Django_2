from django.urls import path

import pagesapp.views as pagesapp

from .apps import PagesappConfig

app_name = PagesappConfig.name

urlpatterns = [
    path("", pagesapp.products, name="index"),
    path("category/<int:pk>/", pagesapp.products, name="category"),
    path("category/<int:pk>/page/<int:page>/", pagesapp.products, name="page"),
    path("product/<int:pk>/", pagesapp.product, name="product"),
]
