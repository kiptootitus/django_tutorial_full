from django.urls import path

from .views import RegisterCreateAPIView, SignInAPIView, home, AccountsListView, logout_view, register_page, sign_in
from accounts.views import ProfilesUpdateView

urlpatterns = [
    path('', home, name="home"),
    path('profiles/', AccountsListView.as_view(), name="profiles_list"),
    path('api/register/', RegisterCreateAPIView.as_view(), name='register'),
    path('register/', register_page, name='register-page'),
    path('signin/', SignInAPIView.as_view(), name='signin'),
    path('accounts/login/', sign_in, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profiles/update/<int:pk>/', ProfilesUpdateView.as_view(), name='profile_update'),
]

