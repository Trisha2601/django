from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated

from rest_framework import status,generics
from App.models import Student,StudentContactInfo
from App.serializers import StudentSerializers,StudentContactInfoSerializer

def students_list(request):
    # You can pass any context here if needed
    context = {
        'message': 'Welcome to the students list page!'
    }
    return render(request, 'students_list.html', context)

@api_view(['POST'])
def create_student(request):
    serializer = StudentSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_all_students_and_contact_info(request):
    students = Student.objects.prefetch_related('contact_info').all()
    return render(request, 'students_list.html', {'students': students})# Get all students
    #serializer = StudentSerializers(students, many=True)  # Serialize the students data with contact info
    #return Response({"status": "success", "students": serializer.data},status=200)
# Create your views here.
# def home(request):
#     return HttpResponse("<h1>Welcome to the Student API<h1>")

# Table - add data - post
class StudentContactInfoListCreate(generics.ListCreateAPIView):
    queryset = StudentContactInfo.objects.all()
    serializer_class = StudentContactInfoSerializer

    def perform_create(self, serializer):
        # You can add custom logic here if needed, for example, you can use
        serializer.save(student=self.request.user) #to associate with a user.
        serializer.save()

class StudentContactInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentContactInfo.objects.all()
    serializer_class = StudentContactInfoSerializer

class GetView(APIView):  # Renamed to follow naming convention
    def get(self, *args, **kwargs):
        result = Student.objects.all()
        serializer = StudentSerializers(result, many=True)
        return Response({'status': 'success', 'students': serializer.data}, status=200)
        
class StudentList(APIView):
    def post(self, request):
        is_multiple = isinstance(request.data, list)
        serializer = StudentSerializers(data=request.data,many=is_multiple)
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
class ContactInfoDelete(APIView):
    def delete(self, request, contact_id):
        try:
            contact_info = StudentContactInfo.objects.get(id=contact_id)
            contact_info.delete()
            return Response({"message": "Contact info deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except StudentContactInfo.DoesNotExist:
            return Response({"error": "Contact info not found"}, status=status.HTTP_404_NOT_FOUND)
#updates the entire resource,it replaces the existing resource with this new representation.
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
# Updates only specified fields in a resource without affecting other fields.
#When you send a PATCH request, you only provide the 
# fields you want to update, and the other fields remain unchanged.
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
