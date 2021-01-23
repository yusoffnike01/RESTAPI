from django.contrib import admin
from django.urls import path,include
from .views import   ArticleViewSet
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('article',ArticleViewSet,basename='article')
urlpatterns = [
    path('viewset/',include(router.urls)),
    path('viewset/<int:id>/',include(router.urls)),
    # path('article/',article_list, name='article'),
    # path('details/<int:pk>/',article_detail, name='details'),
    # path('details/<int:id>/',ArticleDetails.as_view()),
    # path('generic/article/<int:id>/',GenericAPIView.as_view()),
     
              ]
