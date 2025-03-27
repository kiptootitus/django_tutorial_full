from django.urls import path
from .views import RegisterCreateAPIView, home, AccountsListView, register_page

urlpatterns = [
    path('', home, name="home"),
    path('profiles/', AccountsListView.as_view(), name="profiles_list"),
    path('api/register/', RegisterCreateAPIView.as_view(), name='register'),
    path('register/', register_page, name='register-page'),  # Serves the HTML form
]
