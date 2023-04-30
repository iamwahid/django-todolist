from django.shortcuts import render

# Create Todolist with rest framework
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from .serializers import TodoSerializer
from .models import Todo

# Create your views here.
class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    # lookup_field = 'todo_id'
    lookup_url_kwarg = 'todo_id'

    def get_queryset(self):
        queryset = Todo.objects.all()
        activity_group_id = self.request.query_params.get('activity_group_id', None)
        if activity_group_id is not None:
            queryset = queryset.filter(activity_group_id=activity_group_id)
        return queryset

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = TodoSerializer(queryset, many=True)
        response = {
            "status": "Success",
            "message": "Success",
            "data": serializer.data,
        }
        return Response(response)

    def retrieve(self, request, todo_id=None):
        queryset = self.filter_queryset(self.get_queryset())
        todo = queryset.filter(id=todo_id).first()
        if not todo:
            response = {
                "status": "Not Found",
                "message": f"Todo with ID {todo_id} Not Found"
            }
            return Response(response, 404)
        else:
            serializer = TodoSerializer(todo)
            response = {
                "status": "Success",
                "message": "Success",
                "data": serializer.data,
            }
            return Response(response)

    def create(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "status": "Success",
                "message": "Success",
                "data": serializer.data,
            }
            return Response(response, 201)
        else:
            msg = list(serializer.errors.values())[0]
            response = {
                "status": "Bad Request",
                "message": msg,
            }
            return Response(response, 400)

    def update(self, request, todo_id=None, *args, **kwargs):
        queryset = self.get_queryset()
        todo = queryset.filter(id=todo_id).first()
        if not todo:
            response = {
                "status": "Not Found",
                "message": f"Todo with ID {todo_id} Not Found"
            }
            return Response(response, 404)
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "status": "Success",
                "message": "Success",
                "data": serializer.data,
            }
            return Response(response)
        else:
            msg = list(serializer.errors.values())[0]
            response = {
                "status": "Bad Request",
                "message": msg
            }
            return Response(response, 400)

    def destroy(self, request, todo_id=None):
        queryset = self.get_queryset()
        todo = queryset.filter(id=todo_id).first()
        if not todo:
            response = {
                "status": "Not Found",
                "message": f"Todo with ID {todo_id} Not Found"
            }
            return Response(response, 404)
        todo.delete()
        response = {
            "status": "Success",
            "message": "Success",
            "data": {},
        }
        return Response(response, 200)
