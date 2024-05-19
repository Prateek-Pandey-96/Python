from .models import List, ListItem
from rest_framework import viewsets, serializers
from django.contrib.auth import get_user_model

class ListSerializer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(
            queryset=get_user_model().objects.all())
    class Meta:
        model = List
        fields = ['user_id', 'name', 'description', 'created_at', 'updated_at']

class ListViewSet(viewsets.ModelViewSet):
    serializer_class = ListSerializer
    queryset = List.objects.all()

class ListItemSerializer(serializers.HyperlinkedModelSerializer):
    list_id = serializers.PrimaryKeyRelatedField(
            queryset=List.objects.all())
    class Meta:
        model = ListItem
        fields = ['list_id', 'text']

class ListItemViewSet(viewsets.ModelViewSet):
    serializer_class = ListItemSerializer
    queryset = ListItem.objects.all()