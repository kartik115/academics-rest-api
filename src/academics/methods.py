from django.contrib.auth.models import Group
from .serializers import *


def add_user_role(user_id, role_id):
    user_group = Group.objects.filter(id=role_id).first()
    user_group.user_set.add(user_id)
    return user_group.name


def add_user(data):
    user_serializer = UserSerializer(data=data)
    user_serializer.is_valid(raise_exception=True)
    user = user_serializer.save()
    response = user_serializer.data
    del response['password']
    return response, user.id


def student_profile(data, user_id):
    data['user'] = user_id
    student_serializer = StudentSerializer(data=data)
    student_serializer.is_valid(raise_exception=True)
    student = student_serializer.save()
    return student_serializer.data


def professor_profile(data, user_id):
    data['user'] = user_id
    professor_serializer = ProfessorSerializer(data=data)
    professor_serializer.is_valid(raise_exception=True)
    professor = professor_serializer.save()
    return professor_serializer.data


def add_course(data):
    course_serializer = CourseSerializer(data=data)
    course_serializer.is_valid(raise_exception=True)
    course = course_serializer.save()
    return course_serializer.data
