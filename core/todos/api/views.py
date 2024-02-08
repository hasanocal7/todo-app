from rest_framework.permissions import IsAuthenticated
from todos.models import UserProfile, Todo
from todos.api.serializers import ProfileSerializer, TodoSerializer
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework import mixins 
from .permissions import IsHisOwnProfileOrReadOnly, IsHisOwnTodoOrReadOnly

class ProfileListViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet
):
    queryset=UserProfile.objects.all()
    serializer_class=ProfileSerializer
    permission_classes=[IsAuthenticated, IsHisOwnProfileOrReadOnly]

class TodoModelViewSet(ModelViewSet):
    serializer_class=TodoSerializer
    permission_classes=[IsAuthenticated, IsHisOwnTodoOrReadOnly]

    def get_queryset(self):
        queryset=Todo.objects.filter(isDone=False)
        user = self.request.query_params.get('user', None)
        if user is not None:
            queryset = queryset.filter(user__user__username=user)
        return queryset
    
    def perform_create(self, serializer):
        user = self.request.user.profile
        serializer.save(user=user)
