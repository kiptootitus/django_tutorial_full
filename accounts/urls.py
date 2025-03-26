from django.urls import path
from .views import RegisterCreateAPIView, home, AccountsListView

urlpatterns = [
    path('', home, name="home"),
    path('profiles/', AccountsListView.as_view(), name="profiles_list"),
    path('register/', RegisterCreateAPIView.as_view(), name='register')
]
