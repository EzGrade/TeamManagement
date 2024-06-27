from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from team_management.models import Team, UserProfile
from team_management.serializers import (
    UserSerializer,
    TeamSerializer,
    TeamUsersSerializer
)


class UserView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserProfile.objects.all()


class TeamView(ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()

    @action(detail=True, methods=['get'])
    def get_users(self, request, pk=None):
        users = TeamUsersSerializer(
            self.get_object()
        )
        return Response(users.data)
