from django.urls import path

from .views import RegisterCreateAPIView, SignInAPIView, home, ProfilesListAPIView, logout_view, register_page, sign_in, ProfilesUpdateAPIView

urlpatterns = [
    path('home/', home, name="home"),
    path('profiles/', ProfilesListAPIView.as_view(), name="profiles_list"),
    path('register/', RegisterCreateAPIView.as_view(), name='register'),
    path('signup/', register_page, name='signup'),
    path('signin/', SignInAPIView.as_view(), name='signin'),
    path('login/', sign_in, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profiles/update/<int:pk>/', ProfilesUpdateAPIView.as_view(), name='profile_update'),
]

