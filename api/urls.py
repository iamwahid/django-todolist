"""
URL configuration for api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path, include
from api.router import router as api_router
from todo import views as todo_views
from activity import views as activity_views

api_router.register(r'todo-items', todo_views.TodoView, basename="todo-items")
api_router.register(r'activity-groups', activity_views.ActivityView, basename="activity-groups")


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include(api_router.urls)),
]
