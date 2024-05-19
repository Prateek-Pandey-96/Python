from .models import Task
from rest_framework import viewsets, serializers
from django.contrib.auth import get_user_model

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(
            queryset=get_user_model().objects.all())
    class Meta:
        model = Task
        fields = ['user_id', 'title', 'description', 'created_at', 'updated_at']

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()