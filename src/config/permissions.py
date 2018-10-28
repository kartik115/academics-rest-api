from rest_framework.permissions import BasePermission, IsAuthenticated


class SuperUserAccess(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser or request.method in ['GET']


class StudentAccess(BasePermission):
    def has_permission(self, request, view):
        is_student = False
        user_group = request.user.groups.values().first()
        if user_group.get('name') == "Student":
            is_student = True
        return is_student or request.method in ['GET']


class ProfessorAccess(BasePermission):
    def has_permission(self, request, view):
        is_professor = False
        user_group = request.user.groups.values().first()
        if user_group.get('name') == "Professor":
            is_professor = True
        return is_professor or request.method in ['GET']