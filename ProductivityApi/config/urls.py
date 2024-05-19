from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('apps.task.urls')),
    path('lists/', include('apps.list.urls')),
    path('users/', include('apps.user.urls'))
]
