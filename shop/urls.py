from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

import pagesapp.views as pagesapp

urlpatterns = [
    path("admin/", include("adminapp.urls", namespace="admin")),
    path("", pagesapp.main, name="main"),
    path("contact/", pagesapp.contact, name="contact"),
    path("products/", include("pagesapp.urls", namespace="products")),
    path("user/", include("Userapp.urls", namespace="user")),
    path("basket/", include("basketapp.urls", namespace="basket")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
