from django.urls import path
from user import views

urlpatterns = [
    path('', views.MeView.as_view()),
    path('charge/', views.UserViewSet.as_view()),
]