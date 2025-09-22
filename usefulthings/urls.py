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
    path('published-wonts/', PublishedWontListView.as_view(), name='published-wonts-list'),
]
urlpatterns += router.urls