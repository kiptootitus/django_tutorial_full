from django.urls import path
from .views import home, AccountsListView

urlpatterns = [
    path('', home, name="home"),
    path('profiles/', AccountsListView.as_view(), name="profiles_list"),
]
