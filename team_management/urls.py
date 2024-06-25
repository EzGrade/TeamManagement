from django.urls import path
from .views import UserView, TeamView, GetUserView, GetTeamView

urlpatterns = [
    path('user/<int:pk>', GetUserView.as_view()),
    path('user/', UserView.as_view()),
    path('team/<int:pk>', GetTeamView.as_view()),
    path('team/', TeamView.as_view())
]
