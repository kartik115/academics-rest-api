from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from .methods import *
from rest_framework.decorators import api_view, permission_classes
from config.permissions import *
from rest_framework import viewsets


# Create your views here.


@api_view(['POST', 'PUT'])
def user(request):
    if request.method == "POST":
        response, user_id = add_user(request.data)
        response['user_id'] = user_id
        response['role'] = add_user_role(user_id, request.data['role'])
        return Response(status=status.HTTP_200_OK, data=response)


@api_view(['GET'])
def user_roles(request):
    print(request.user.groups.values().first())
    response = Group.objects.values()
    return Response(status=status.HTTP_200_OK, data=response)


@api_view(['GET', 'PUT', 'POST'])
def user_profile(request):
    user_group = request.user.groups.values().first()
    if user_group.get('name') == "Student":
        if request.method == "POST":
            response = student_profile(request.data, request.user.id)
        if request.method == "GET":
            response = Student.objects.filter(user=request.user).values().first()
    elif user_group.get('name') == "Professor":
        if request.method == "POST":
            response = professor_profile(request.data, request.user.id)
        if request.method == "GET":
            response = Professor.objects.filter(user=request.user).values().first()
    return Response(status=status.HTTP_200_OK, data=response)


@api_view(['GET', 'POST'])
@permission_classes((SuperUserAccess,))
def course(request):
    if request.method == 'GET':
        response = Course.objects.values()
    if request.method == 'POST':
        response = add_course(request.data)
    return Response(status=status.HTTP_200_OK, data=response)


class CourseGradingViewSet(viewsets.ModelViewSet):
    queryset = CourseGrading.objects.all()
    serializer_class = CourseGradingSerializer
    permission_classes = [SuperUserAccess]
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('course',)

