import json
from.models import Student_Data,Group_Data
from .serializers import StudentSerializer,GroupSerializer,Student1Serializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

# Create your views here.

@api_view(['GET'])
def details(request):
    student = Student_Data.objects.all()
    serializer = StudentSerializer(student, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



@api_view(['POST'])
def update(request, id):
    student = Student_Data.objects.get(id=id)
    serializer = StudentSerializer(instance=student, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete(request, id):
    event = Student_Data.objects.get(id=id)
    event.delete()
    return Response('Deleted')


@api_view(['POST'])
def create1(request):
    groupserializer = GroupSerializer(data=request.data)
    if groupserializer.is_valid():
        group = groupserializer.save()
    request.data['Group_Data'] = group.id
    studentserializer = StudentSerializer(data=request.data)
    if studentserializer.is_valid():
         studentserializer.save()
    #print('errors', studentserializer.errors)
    return Response(studentserializer.data)
    #return Response(serializer.data,'data saved successfully')



@api_view(['POST'])
def update(request, id):
    group = Group_Data.objects.get(id=id)
    serializer = GroupSerializer(instance=group, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete(request, id):
    group = Group_Data.objects.get(id=id)
    group.delete()
    return Response('Deleted')


@api_view(['GET'])
def details(request):
    group = Group_Data.objects.all()
    serializer = GroupSerializer(group, many=True)
    return Response(serializer.data)

class GroupAPI(APIView):
    def details(self, request):
        group = Group_Data.objects.all()
        serializer = GroupSerializer(group, many=True)
        return Response(serializer.data)

    def create1(self, request):
        grpserializer = GroupSerializer(data=request.data)
        if grpserializer.is_valid():
            Group = grpserializer.save()
        request.data['Group_Data'] = Group.id
        stuserializer = Student1Serializer(data=request.data)
        if stuserializer.is_valid():
            stuserializer.save()
        return Response(stuserializer.data)

    def update(self, request, id):
        group = Group_Data.objects.get(id=id)
        serializer = GroupSerializer(instance=group, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        group = Group_Data.objects.get(id=id)
        group.delete()
        return Response('Deleted')



class StudentAPI(APIView):
    def details(self, request):
        student = Student_Data.objects.all()
        data = StudentSerializer(student, many=True, context={'request': request}).data
        return Response(data)

    def delete(self, request, id):
        student = Student_Data.objects.get(id=id)
        student.Branch.delete()
        return Response('Deleted')

    def update(self, request, id):
        student = Student_Data.objects.get(id=id)
        serializer = Student1Serializer(instance=student, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)



