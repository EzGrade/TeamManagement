from django.urls import path
from .views import UserView, TeamView

urlpatterns = [
    path('user/<int:pk>/', UserView.as_view({'get': 'retrieve'})),
    path('user/', UserView.as_view({'post': 'create'})),
    path('team/<int:pk>/', TeamView.as_view({'get': 'retrieve', 'put': 'update'})),
    path('team/<int:pk>/users/', TeamView.as_view({'get': 'get_users'})),
    path('team/', TeamView.as_view({'post': 'create'})),
]
