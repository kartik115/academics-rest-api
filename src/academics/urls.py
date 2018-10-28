from .views import *
from rest_framework import routers
from django.urls import path, include
from django.conf.urls import url

router = routers.SimpleRouter()
router.register(r'grading', CourseGradingViewSet)

urlpatterns = [
    url(r'^user/$', user),
    url(r'^user-roles/$', user_roles),
    url(r'^user-profile/$', user_profile),
    url(r'^courses/$', course),
    url(r'^', include(router.urls)),
]

