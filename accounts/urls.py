from django.urls import path

from .views import signup
from .views import SignUpView
from . import views

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', views.profile_view, name='profile'),

    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]