from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework.urls import app_name

from usefulthings.apps import UsefulthingsConfig
from usefulthings.views import (WontViewSet, PublishedWontListView, )

app_name = UsefulthingsConfig.name

router = SimpleRouter()
router.register("", WontViewSet)

urlpatterns = [
    path('wont/create/', WontViewSet.as_view({'post': 'create'}), name='wont-create'),
    path('wont/', WontViewSet.as_view({'get': 'list'}), name='wont-list'),
    path('wont/<int:pk>/', WontViewSet.as_view({'get': 'retrieve'}), name='wont-retrieve'),
    path('wont/<int:pk>/', WontViewSet.as_view({'patch': 'partial_update'}), name='wont-partial-update'),
    path("wont/<int:pk>/delete/", WontViewSet.as_view({'delete': 'destroy'}), name='wont-delete'),
    path('published-wonts/', PublishedWontListView.as_view(), name='published-wonts-list'),
]
urlpatterns += router.urls
