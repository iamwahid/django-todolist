from django.shortcuts import render

# Create Activitylist with rest framework
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from .serializers import ActivitySerializer
from .models import Activity

# Create your views here.
class ActivityView(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all()
    lookup_url_kwarg = 'activity_id'

    def get_queryset(self):
        queryset = Activity.objects.all()
        activity_group_id = self.request.query_params.get('activity_group_id', None)
        if activity_group_id is not None:
            queryset = queryset.filter(activity_group_id=activity_group_id)
        return queryset

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = ActivitySerializer(queryset, many=True)
        response = {
            "status": "Success",
            "message": "Success",
            "data": serializer.data,
        }
        return Response(response)

    def retrieve(self, request, activity_id=None):
        queryset = self.filter_queryset(self.get_queryset())
        activity = queryset.filter(id=activity_id).first()
        if not activity:
            response = {
                "status": "Not Found",
                "message": f"Activity with ID {activity_id} Not Found"
            }
            return Response(response, 404)
        else:
            serializer = ActivitySerializer(activity)
            response = {
                "status": "Success",
                "message": "Success",
                "data": serializer.data,
            }
            return Response(response)

    def create(self, request):
        serializer = ActivitySerializer(data=request.data)
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

    def update(self, request, activity_id=None, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        activity = queryset.filter(id=activity_id).first()
        if not activity:
            response = {
                "status": "Not Found",
                "message": f"Activity with ID {activity_id} Not Found"
            }
            return Response(response, 404)
        serializer = ActivitySerializer(activity, data=request.data)
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
                "message": msg,
            }
            return Response(response, 400)

    def destroy(self, request, activity_id=None):
        queryset = self.get_queryset()
        activity = queryset.filter(id=activity_id).first()
        if not activity:
            response = {
                "status": "Not Found",
                "message": f"Activity with ID {activity_id} Not Found"
            }
            return Response(response, 404)
        activity.delete()
        response = {
            "status": "Success",
            "message": "Success",
            "data": {},
        }
        return Response(response, 200)
