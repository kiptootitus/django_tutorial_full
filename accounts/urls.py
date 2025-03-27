from django.urls import path

from .views import RegisterCreateAPIView, SignInAPIView, home, AccountsListView, logout_view, register_page, sign_in

urlpatterns = [
    path('', home, name="home"),
    path('profiles/', AccountsListView.as_view(), name="profiles_list"),
    path('api/register/', RegisterCreateAPIView.as_view(), name='register'),
    path('register/', register_page, name='register-page'),
    path('signin/', SignInAPIView.as_view(), name='signin'),
    path('login/', sign_in, name='login'),
    path('logout/', logout_view, name='logout'),

]

