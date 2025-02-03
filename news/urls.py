from django.urls import path
from . import views

app_name = 'news'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('weather/', views.weatherView.as_view(), name='weather'),
    path('sports/', views.sportsView.as_view(), name='sports'),
    path('living/', views.livingView.as_view(), name='living'),
    path('politics/', views.politicsView.as_view(), name='politics'),
    path('business/', views.businessView.as_view(), name='business'),
    path('post/',views.CreatePostView.as_view(),name='post'),
    path('post_done/',views.PostSuccessView.as_view(),name='post_done'),
]
