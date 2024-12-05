from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from App.models import Student
from App.serializers import StudentSerializers

# Create your views here.

# Table - add data - post
class GetView(APIView):  # Renamed to follow naming convention
    def get(self, request, *args, **kwargs):
        result = Student.objects.all()
        serializer = StudentSerializers(result, many=True)
        return Response({'status': 'success', 'students': serializer.data}, status=200)

class StudentList(APIView):
    def post(self, request):
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'students': serializer.data}, status=status.HTTP_201_CREATED)  # Using 201 for created
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)  # Changed to serializer.errors for clarity

class DeleteView(APIView):
    def delete(self, request, id):
        try:
            student = Student.objects.get(id=id)
            student.delete()
            return Response({'status': 'success'}, status=200)
        except Student.DoesNotExist:
            return Response({'status': 'fail', 'message': 'Student not found'}, status=404)

class PutView(APIView):
    def put(self, request, id, *args, **kwargs):
        try:
            student = Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response({'status': 'fail', 'message': 'Student not found'}, status=404)
        serializer = StudentSerializers(student, data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the updated data
            return Response({'status': 'success', 'students': serializer.data}, status=200)
        return Response({'status': 'fail', 'errors': serializer.errors}, status=400)

class PatchView(APIView):
    def patch(self, request, id, *args, **kwargs):
        try:
            student = Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response({'status': 'fail', 'message': 'Student not found'}, status=404)
        serializer = StudentSerializers(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()  # Save the partially updated data
            return Response({'status': 'success', 'students': serializer.data}, status=200)
        return Response({'status': 'fail', 'errors': serializer.errors}, status=400)
